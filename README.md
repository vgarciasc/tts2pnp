# print n' play scripts
Easily transforming files with tons of cards into pages of printable A4

![](./process.png)

## Usage
Put your images in `data` folder and edit `files.json` accordingly. Then, just run `script.py`.

## Settings

These are the settings configurable in `files.json`:

- `a4_pix`: the size (in pixels) of the final A4 file that you want. All final files will have these dimensions. Should be proportional to `a4_dim`. Example: `[2480, 3508]`.
- `a4_dim`: the size (in millimeters) of an A4 paper. Trivially the value is `[210, 297]`, but you may want to change this if printing in another kind of paper.
- `output_path`: the folder in which the processed files will be exported, relative to current path. Example: `data/exported`.
- `card_files`: array with information pertaining to groups of files.
  - `name`: name of the group of files. This will be used in the saving step: if `name` is "characters", then the exported files will be "characters_0.png", "characters_1.png", etc.
  - `rotate`: boolean. If true, cards will be positioned horizontally instead of vertically. Only relevant if `bestFit` is set to false.
  - `bestFit`: boolean. If true, will try to fit as many cards as possible in each A4 page, rotating them if necessary. Useful to save space. Overrides `rotate`.
  - `margin_mm`: makes sure that the cards will be offset by a certain margin in the final A4 file. For example, if `margin_mm` equals `[10, 10]`, there will be empty 10mm in each of the four borders of the final A4 files.
  - `padding_mm`: sets the space in millimeters between the cards themselves. A value of `[1, 2]` means a space of 1mm between horizontally adjacent cards, and 2mm between vertically adjacent cards. Should be set to `[0, 0]` if original cards file already has some padding.
  - `card_dim`: the dimensions (in millimeters) that the cards should have. For a standard deck of cards, this should be `[63, 88]`. When you print the final A4 files, the cards *will* have these dimensions (if you make sure the printer doesn't add any additional margins).
  - `fileData`: array with information pertaining to individual files.
    - `filename`: path to file.
    - `card_count`: the distribution of cards in the file. Example: if the file has 20 cards spread in 4 columns and 5 rows, this should be `[4, 5]`.
    - `instances`: how many instances should this file have in the final A4 files? Trivially it should be `1`, but there are many situations where the back of the cards is provided in a separate file, and you want to print this not only once, but N times (N being the number of cards). In these cases, `instances` is the parameter you want to tweak.
    - `maintain_w_or_h`: controls how the file will be scaled. If you want to scale it vertically, set it to 0. Otherwise, if you want to scale it horizontally, set it to 1. This has practically no effect in the final result, but it changes the resolution with which the file will be treated internally. If not sure, set this to 1.
    
