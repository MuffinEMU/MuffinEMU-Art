# MuffinEMU-Art

Downloadable cover art packs for [MuffinEMU](https://github.com/MuffinEMU/Muffin-EMU), a Wii U emulator for iOS.

The packs are hosted here, separately from the app, as GitHub Release assets (they total several GB). Nothing in this repository is needed to run MuffinEMU. Cover art is optional.

## How MuffinEMU uses the packs

1. The app fetches `manifest.json` from this repository (raw URL: `https://raw.githubusercontent.com/MuffinEMU/MuffinEMU-Art/main/manifest.json`).
2. You pick a pack. MuffinEMU downloads its zip file(s) from the `packs-v1` release.
3. The app checks each download against the `sha256` and `size` in the manifest, unzips it and installs the images.
4. Images are matched to your games by normalized title using the `index` in the manifest.

## Packs

| Pack | Style | Contents |
|---|---|---|
| `3d-boxes` | 3D | Wii U 3D boxes |
| `2d-eshop` | 2D | eShop 2D boxes |
| `2d-disc` | disc | Disc 2D boxes, named like `Title (USA).png` |
| `vc-2d` | 2D | Virtual Console 2D boxes |
| `vc-3d` | 3D | Virtual Console 3D boxes |
| `robin55-3d-8bit` | 3D | Robin55's Wii U 3D Boxes 1.3, 8-bit PNG |
| `robin55-3d-32bit` | 3D | Robin55's Wii U 3D Boxes 1.3, 32-bit PNG |

Sizes, hashes and image counts are in `manifest.json`. File names inside the zips are UTF-8 NFC.

`generic/` holds a no-cover box (3D and 2D) that MuffinEMU can show for games with no art. `tools/render3d.md` explains how to render more 3D boxes.

## Takedown and contact

Box art belongs to its respective publishers. If you are a rights holder and want something removed, open an issue in this repository and the content will be removed. If you made one of the community packs and want to be credited, open an issue as well.

See [CREDITS.md](CREDITS.md) for attribution and [LICENSE](LICENSE) for licensing.
