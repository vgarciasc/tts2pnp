import sys
import math
import utils
import crop_cards
from PIL import Image

BG_COLOR = (255, 255, 255, 255)

def composite(cards, card_dim, a4_dim, a4_pix, margin_mm, padding_mm, rotate=False, bestFit=False):
    if bestFit:
        fit_rotate_0 = math.floor(a4_dim[0] / card_dim[0]) * math.floor(a4_dim[1] / card_dim[1])
        fit_rotate_1 = math.floor(a4_dim[0] / card_dim[1]) * math.floor(a4_dim[1] / card_dim[0])
        rotate = fit_rotate_1 > fit_rotate_0
    if rotate:
        cards = [card.rotate(90, expand=True) for card in cards]
        card_dim = card_dim[::-1]
    
    im_out = Image.new('RGBA', a4_pix, BG_COLOR)
    output = []

    mm_to_px = a4_pix[0] / a4_dim[0]

    p_col = 0
    p_row = 0

    card_ix = 0

    while card_ix < len(cards):
        padding_x = padding_mm[0] if p_col > 0 else 0
        padding_y = padding_mm[1] if p_row > 0 else 0

        # paste coords
        p_x0 = int((p_col * (card_dim[0] + padding_x) + margin_mm[0]) * mm_to_px)
        p_y0 = int((p_row * (card_dim[1] + padding_y) + margin_mm[1]) * mm_to_px)
        p_x1 = p_x0 + int(card_dim[0] * mm_to_px)
        p_y1 = p_y0 + int(card_dim[1] * mm_to_px)

        if p_x1 > a4_pix[0]:
            p_row += 1
            p_col = 0
            continue
        elif p_y1 > a4_pix[1]:
            output.append(im_out)
            im_out = Image.new('RGBA', a4_pix, BG_COLOR)
            p_row = 0
            p_col = 0
            continue

        im_out.paste(cards[card_ix], (p_x0, p_y0))

        p_col += 1
        card_ix += 1

    output.append(im_out)
    return output

if __name__ == "__main__":
    filenames = ["data\\a4_resized_aliens1.png", "data\\a4_resized_aliens2.png"]
    
    card_count = (5, 5)
    card_dim = (63, 88)
    a4_dim = (210, 297)
    a4_pix = (2480, 3508)
    margin_mm = (10, 10)
    padding_mm = (2, 2)

    cards = []
    for filename in filenames:
        im = Image.open(filename)
        cards.extend(crop_cards.crop_cards(im, card_count, card_dim, a4_dim, a4_pix))

    pages = composite(cards, card_dim, a4_dim, a4_pix, margin_mm, padding_mm)
    
    for i in range(0, len(pages)):
        pagename = utils.get_filename_with_preffix_suffix(filename, "", "_" + str(i))
        pages[i].save(pagename)