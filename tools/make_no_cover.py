"""Draw the flat 2D no-cover art (567x878). Usage: python make_no_cover.py icon.png out.png"""
import sys
from PIL import Image, ImageDraw, ImageFont
W, H = 567, 878
im = Image.new("RGB", (W, H), (58, 40, 32)); d = ImageDraw.Draw(im)
d.rectangle([18, 18, W - 19, H - 19], outline=(214, 160, 96), width=4)
ic = Image.open(sys.argv[1]).convert("RGBA").resize((300, 300), Image.LANCZOS)
im.paste(ic, ((W - 300) // 2, 230), ic)
def font(s):
    for p in ["/System/Library/Fonts/Helvetica.ttc", "/System/Library/Fonts/SFNS.ttf"]:
        try: return ImageFont.truetype(p, s)
        except Exception: pass
    return ImageFont.load_default()
for txt, y, s, c in [("NO COVER", 580, 64, (244, 226, 196)), ("MuffinEMU", 670, 36, (214, 160, 96))]:
    f = font(s); w = d.textlength(txt, font=f); d.text(((W - w) / 2, y), txt, font=f, fill=c)
im.save(sys.argv[2])
