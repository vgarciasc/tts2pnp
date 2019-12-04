import sys
import utils
from PIL import Image

BG_COLOR = (255, 255, 255, 255)

def crop_cards(image, card_count, card_dim, a4_dim, a4_pix):
    output = []

    mm_to_px = a4_pix[0] / a4_dim[0]

    card_ix = 0

    while card_ix < (card_count[0] * card_count[1]):
        c_col = card_ix % card_count[0]
        c_row = int(card_ix / card_count[0])

        # crop coords
        c_x0 = int(c_col * card_dim[0] * mm_to_px)
        c_y0 = int(c_row * card_dim[1] * mm_to_px)
        c_x1 = c_x0 + int(card_dim[0] * mm_to_px)
        c_y1 = c_y0 + int(card_dim[1] * mm_to_px)

        card = image.crop((c_x0, c_y0, c_x1, c_y1))
        output.append(card)

        card_ix += 1

    return output

if __name__ == "__main__":
    if (len(sys.argv) == 1 or sys.argv[1] == "--help"):
        print("Usage: crop_cards.py [filename] [card_count] [card_dim] [a4 dim] [a4 pix]")
        print("Example: crop_cards.py cards.png 5 5 63 88 210 297 2480 3508")
        print("  this means: \"image 'cards.png' has cards in a 5x5 grid, and the cards have 63mm x 88mm dimensions irl. The destination A4 image is 2480px x 3508px. Crop those cards and give them to me.\"")
        exit(1)
    
    try:
        filename = str(sys.argv[1])
        card_count = (int(sys.argv[2]), int(sys.argv[3]))
        card_dim = (int(sys.argv[4]), int(sys.argv[5]))
        a4_dim = (int(sys.argv[6]), int(sys.argv[7]))
        a4_pix = (int(sys.argv[8]), int(sys.argv[9]))
    except:
        print("Type \"crop_cards.py --help\" to see usage.")
        exit(1)

    # filename = "a4_resized_aliens1.png"
    # card_count = (5, 5)
    # card_dim = (63, 88)
    # a4_dim = (210, 297)
    # a4_pix = (2480, 3508)

    im = Image.open(filename)
    pages = crop_cards(im, card_count, card_dim, a4_dim, a4_pix)
    
    for i in range(0, min(len(pages), 10)):
        pages[i].show()