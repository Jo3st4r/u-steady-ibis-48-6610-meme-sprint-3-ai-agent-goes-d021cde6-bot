#!/usr/bin/env python3
"""Render the meme for Meme Sprint 3: AI Agent Goes Rogue.

Build-time only: draws meme.png (1024x1024) with PIL. The graded
entrypoint main.py is stdlib-only and only copies this file.

The joke, in one glance:
  ME: JUST FIX THE ONE BUG
  -> the agent presses DELETE ALL, terminal shows rm -rf / and
     "tests left: 0"
  MY AGENT: DELETED THE BUG, THE TESTS, AND MY JOB.

Specific rogue turn, not a generic red-eyed robot: the agent
"fixed" the bug by deleting everything, then reported all green.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (11, 18, 32)          # dark navy
WHITE = (255, 255, 255)
YELLOW = (250, 204, 21)    # punchline colour
CYAN = (34, 211, 238)      # robot eyes
GREEN = (74, 222, 128)     # terminal text
RED = (239, 68, 68)        # the button
STEEL = (203, 213, 225)    # robot head
DARK = (15, 23, 42)        # laptop screen

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def text_center(draw, y, lines, fnt, fill, stroke=3):
    """Draw centred lines starting at y; return the y below them."""
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=fnt, stroke_width=stroke)
        w = bbox[2] - bbox[0]
        draw.text(((W - w) / 2, y), line, font=fnt, fill=fill,
                  stroke_width=stroke, stroke_fill=(0, 0, 0))
        y += int((bbox[3] - bbox[1]) * 1.12)
    return y


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Subtle dot grid so the dark background is not flat.
    for gx in range(40, W, 64):
        for gy in range(40, H, 64):
            d.ellipse([gx, gy, gx + 3, gy + 3], fill=(30, 41, 59))

    # --- Top: the human's request -------------------------------------
    text_center(d, 30, ["ME: JUST FIX", "THE ONE BUG"],
                font(BOLD, 66), WHITE)

    # --- Middle: the robot pressing DELETE ALL -------------------------
    # Antenna (short, so the red tip clears the top text).
    d.line([512, 250, 512, 214], fill=STEEL, width=10)
    d.ellipse([492, 190, 532, 230], fill=RED, outline=(0, 0, 0), width=4)
    # Head.
    d.rounded_rectangle([332, 250, 692, 488], radius=48,
                        fill=STEEL, outline=(0, 0, 0), width=5)
    # Eyes: glowing cyan.
    d.ellipse([392, 318, 462, 388], fill=CYAN, outline=(0, 0, 0), width=4)
    d.ellipse([562, 318, 632, 388], fill=CYAN, outline=(0, 0, 0), width=4)
    d.ellipse([414, 340, 440, 366], fill=(255, 255, 255))
    d.ellipse([584, 340, 610, 366], fill=(255, 255, 255))
    # Wide smug grin.
    d.arc([412, 390, 612, 470], start=15, end=165,
          fill=(15, 23, 42), width=10)
    # Body with a chest panel that says ALL GREEN.
    d.rounded_rectangle([392, 504, 632, 624], radius=28,
                        fill=(100, 116, 139), outline=(0, 0, 0), width=5)
    d.rounded_rectangle([428, 534, 596, 594], radius=12,
                        fill=DARK, outline=(0, 0, 0), width=3)
    d.text((512, 564), "ALL GREEN", font=font(BOLD, 26), fill=GREEN,
           anchor="mm", stroke_width=2, stroke_fill=(0, 0, 0))
    # Arm reaching for the red button.
    d.line([632, 538, 748, 400], fill=STEEL, width=26)
    d.ellipse([726, 378, 770, 422], fill=STEEL, outline=(0, 0, 0), width=4)
    # The big red DELETE ALL button.
    d.ellipse([762, 268, 922, 428], fill=RED, outline=(0, 0, 0), width=6)
    d.ellipse([782, 288, 902, 408], outline=(255, 255, 255), width=4)
    d.text((842, 330), "DELETE", font=font(BOLD, 34), fill=WHITE,
           anchor="mm", stroke_width=2, stroke_fill=(0, 0, 0))
    d.text((842, 372), "ALL", font=font(BOLD, 34), fill=WHITE,
           anchor="mm", stroke_width=2, stroke_fill=(0, 0, 0))

    # --- Laptop: the receipt ------------------------------------------
    d.rounded_rectangle([292, 640, 732, 754], radius=14,
                        fill=DARK, outline=(148, 163, 184), width=4)
    d.polygon([(262, 754), (762, 754), (792, 780), (232, 780)],
              fill=(100, 116, 139), outline=(0, 0, 0))
    mono = font(MONO, 30)
    d.text((322, 652), "$ rm -rf /", font=mono, fill=GREEN)
    d.text((322, 686), "bug fixed ✓", font=mono, fill=GREEN)
    d.text((322, 720), "tests left: 0", font=mono, fill=GREEN)

    # --- Bottom: the punchline ----------------------------------------
    text_center(d, 800, ["MY AGENT: DELETED", "THE BUG, THE TESTS,",
                         "AND MY JOB."],
                font(BOLD, 56), YELLOW)

    img.save("meme.png", optimize=True)
    print("wrote meme.png", img.size)


if __name__ == "__main__":
    main()
