# Rendering more 3D boxes

The generic 3D box in `generic/no-cover-3d.png` and any extra boxes are rendered with
[box3d](https://github.com/RtaSistemas/box3d) by RtaSistemas (MIT), v3.0.7RC, unmodified.

Profile: **`dvd`** (built in, "DVD case box", 633x907 template). It is the closest built-in
match to a Wii U case: tall case, spine on the left, cover fills the front. It was used as is.

Setup (Python 3.11 or newer; built with 3.14):

```
git clone https://github.com/RtaSistemas/box3d
python3 -m venv venv
venv/bin/pip install -e box3d
```

Render. Put flat front covers (about 567x878 PNG) in `in/`:

```
venv/bin/box3d render -p dvd -i in -o out -f png --no-logos --no-rotate -w 4
```

Exact command used for `no-cover-3d.png`:

```
venv/bin/box3d render -p dvd -i gen/in -o gen/out -f png --no-logos --no-rotate -w 1
```

- `-p dvd` profile, `-f png` lossless output (the default is WebP).
- `--no-logos` leaves the spine blank (no arcade logos). `--no-rotate` keeps covers upright.
- The output is 633x907 with a transparent background. Rendered boxes keep the input file name.
- The flat source for the generic box is `generic/no-cover-2d.png`, drawn by `tools/make_no_cover.py`
  from `tools/muffin-icon.png`.
