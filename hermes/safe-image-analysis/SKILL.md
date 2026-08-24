---
name: safe-image-analysis
description: "Use when about to call look_at or Read on a local image file (screenshot, photo, diagram). Checks file size and dimensions first, auto-resizes large images to a temp JPEG to prevent provider context limit failures."
---

# Safe Image Analysis

## Overview

Large image files cause `look_at` and `Read` tools to silently fail. When an image is too large (e.g. an 11 MB, 3771×2009 PNG screenshot), the base64 encoding required to send it as a media attachment adds ~33% overhead — pushing the payload well past the provider's context limit. The conversation gets compacted, the media attachment is stripped, and the tool returns garbage or a stale summary instead of actual image analysis.

This skill prevents that failure by checking file size and dimensions **before** calling `look_at` or `Read` on any image. If either threshold is exceeded, the image is auto-resized to a temp JPEG file, analyzed, and the temp file is immediately cleaned up. The original file is never modified.

---

## Constants

| Constant | Value | Description |
|----------|-------|-------------|
| MAX_FILE_SIZE | 3 MB (3,145,728 bytes) | Files larger than this trigger resize |
| MAX_DIMENSION | 2000 px | Longest side above this triggers resize |
| RESIZE_TARGET | 1500 px | Longest side of resized output (below MAX_DIMENSION for safety margin) |
| OUTPUT_FORMAT | JPEG | Temp file format — small, universally supported |
| OUTPUT_QUALITY | 85 | JPEG quality (good balance of size vs detail) |
| ALLOWED_EXTENSIONS | .png .jpg .jpeg .gif .bmp .tiff .tif .webp | Raster image formats only |

> **Why JPEG output?** A 1500px PNG of a complex photo can still be 2–4 MB. JPEG at quality 85 stays well under 500 KB for any 1500px image, guaranteeing the resized file is safe regardless of content complexity.

> **Why RESIZE_TARGET < MAX_DIMENSION?** Resizing to exactly 2000px and saving as JPEG could still produce a large file for very complex images. The 1500px target provides a safety margin.

---

## Trigger Conditions

**This skill activates when:**
- Agent is about to call `look_at` with a `file_path` pointing to an image file
- Agent is about to call `Read` on a file with an extension from ALLOWED_EXTENSIONS
- Agent is asked to visually analyze, describe, or inspect a screenshot, photo, or diagram stored as a local file

**This skill does NOT apply to:**
- SVG files — text-based vector format, `Read` handles them as plain text
- PDF files — handled by dedicated PDF tools
- The `image_data` base64 parameter of `look_at` — no file path to pre-check (v2 concern)
- Non-image files (code, config, markdown, etc.)

---

## Procedure

### Step 0: Check file extension

Extract the extension and verify it is in ALLOWED_EXTENSIONS. If not, skip this skill entirely and proceed normally.

```bash
IMAGE_PATH="/path/to/your/image.png"
file_ext="${IMAGE_PATH##*.}"
# Allowed: png jpg jpeg gif bmp tiff tif webp
# If extension is NOT in this list → skip skill, proceed normally
```

### Step 1: Check Pillow availability

```bash
python3 -c "from PIL import Image; print('Pillow available')" 2>/dev/null
```

**If Pillow is NOT available:**
- Warn the user: *"Pillow is not installed. Cannot safely check image dimensions. Install with: `pip install Pillow`"*
- Still proceed to Step 2 for the file size check
- If file size exceeds MAX_FILE_SIZE → **ABORT** analysis, warn user the image is too large and Pillow is required to resize it
- If file size is under MAX_FILE_SIZE → proceed with `look_at`/`Read` on the original, but **warn** that dimensions were not verified and a large-dimension image could still cause failure

### Step 2: Check file size

```bash
stat -f%z "$IMAGE_PATH" 2>/dev/null || stat -c%s "$IMAGE_PATH"
# Compare result against 3145728 (3 MB in bytes)
# Record: SIZE_EXCEEDS=true if result > 3145728
```

### Step 3: Check dimensions

```bash
python3 -c "
from PIL import Image
img = Image.open('$IMAGE_PATH')
w, h = img.size
print(f'{w}x{h}')
print('EXCEEDS' if max(w, h) > 2000 else 'OK')
"
```

Record: `DIMS_EXCEEDS=true` if the longest side exceeds 2000 px.

### Step 4: Decision gate

`<HARD-GATE>`: Evaluate both results using **logical OR**:

- If **EITHER** `SIZE_EXCEEDS` **OR** `DIMS_EXCEEDS` is true → proceed to **Step 5** (resize)
- If **BOTH** are false → skip to **Step 6**, use the original file directly

> **Why OR, not AND?** A 500 KB file at 6000×4000 px is still dangerous when decoded. A 5 MB file at 800×600 px is also dangerous due to base64 overhead. Either condition alone is sufficient to cause failure.

### Step 5: Resize to temp file

Run this self-contained Python script. The image path must be passed as an argument — do NOT use a quoted heredoc, as that prevents variable expansion.

```bash
python3 -c "
import sys, tempfile, os
from PIL import Image

IMAGE_PATH = sys.argv[1]
TARGET = 1500
QUALITY = 85

img = Image.open(IMAGE_PATH)

# Resize maintaining aspect ratio, never upscale
img.thumbnail((TARGET, TARGET), Image.LANCZOS)

# Flatten alpha/palette transparency to white background for JPEG output
# Handles: RGBA, LA, PA (palette with alpha), P (palette — may have transparency metadata)
if img.mode in ('RGBA', 'LA'):
    background = Image.new('RGB', img.size, (255, 255, 255))
    background.paste(img, mask=img.split()[-1])
    img = background
elif img.mode == 'PA':
    img = img.convert('RGBA')
    background = Image.new('RGB', img.size, (255, 255, 255))
    background.paste(img, mask=img.split()[-1])
    img = background
elif img.mode == 'P':
    img = img.convert('RGBA')
    background = Image.new('RGB', img.size, (255, 255, 255))
    background.paste(img, mask=img.split()[-1])
    img = background
elif img.mode != 'RGB':
    img = img.convert('RGB')

# Save to a unique temp file (collision-safe)
fd, tmp_path = tempfile.mkstemp(suffix='.jpg', prefix='safe-img-')
os.close(fd)
img.save(tmp_path, 'JPEG', quality=QUALITY)

size_kb = os.path.getsize(tmp_path) / 1024
print(f'Resized to: {img.size[0]}x{img.size[1]}, {size_kb:.0f} KB')
print(f'TEMP_PATH={tmp_path}')
" "$IMAGE_PATH"
```

> **Note on animated GIFs:** PIL loads only the first frame of animated GIFs. The resized JPEG will represent the first frame only — animation is not preserved. This is acceptable for visual analysis purposes.

Parse `TEMP_PATH` from the last line of output (format: `TEMP_PATH=/tmp/safe-img-XXXX.jpg`).

### Step 6: Analyze the image

Call `look_at` (or `Read`) using:
- `file_path` = `TEMP_PATH` (the resized temp file, from Step 5), OR the original path (if Step 4 skipped resize)
- `goal` = the original analysis goal the agent intended

### Step 7: Cleanup

```bash
rm "$TEMP_PATH"
```

Run this **immediately** after analysis completes — do not defer, do not keep the file for later use. If analysis is interrupted, clean up on the next available opportunity.

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `ModuleNotFoundError: No module named 'PIL'` | `pip install Pillow` (user must run manually) |
| `Permission denied` writing to `/tmp` | Try `TMPDIR=/var/tmp python3 ...` |
| `cannot identify image file` | Run `file "$IMAGE_PATH"` — the file may be corrupted or not actually an image |
| Resized image still causes failure | Lower RESIZE_TARGET to 1000 and/or OUTPUT_QUALITY to 70 |
| `stat` command not found | Use `python3 -c "import os; print(os.path.getsize('$IMAGE_PATH'))"` instead |

---

## Must NOT Do

- **NEVER** call `look_at` or `Read` on the original file if it exceeds either threshold — always use the resized temp file
- **NEVER** modify, overwrite, or delete the original image file
- **NEVER** install Pillow or any other dependency — only check availability and warn the user
- **NEVER** cache or persist resized temp files beyond the immediate analysis step
- **NEVER** apply this skill to SVG, HEIC, PDF, or non-raster formats
- **NEVER** skip the size/dimension check because the image "looks small" or "is probably fine"
- **NEVER** proceed with analysis if the image exceeds thresholds and the resize step failed
- **NEVER** save the resized temp file as PNG — always JPEG to guarantee a small output size
