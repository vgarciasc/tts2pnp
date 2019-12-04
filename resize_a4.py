import sys
import utils
from PIL import Image

def resize_a4(image, card_count, card_dim, a4_dim, a4_pix):
    new_cards_w = int(((card_count[0] * card_dim[0]) * a4_pix[0]) / a4_dim[0])
    new_cards_h = int(((card_count[1] * card_dim[1]) * a4_pix[1]) / a4_dim[1])
    new_size = (new_cards_w, new_cards_h)

    return image.resize(new_size, Image.BICUBIC)

if __name__ == "__main__":
    if (len(sys.argv) == 1 or sys.argv[1] == "--help"):
        print("Usage: resize_a4.py [filename] [card_count] [card_dim] [a4 dim] [a4 pix]")
        print("Example: resize_a4.py resized_cards.png 5 5 63 88 210 297 2480 3508")
        print("  this means: \"image 'resized_cards.png' has cards in a 5x5 grid, and the cards have 63mm x 88mm dimensions irl. Resize it so that its dimensions are proportional to an A4 image with 2480px x 3508px.\"")
        exit(1)
    
    try:
        filename = str(sys.argv[1])
        card_count = (int(sys.argv[2]), int(sys.argv[3]))
        card_dim = (int(sys.argv[4]), int(sys.argv[5]))
        a4_dim = (int(sys.argv[6]), int(sys.argv[7]))
        a4_pix = (int(sys.argv[8]), int(sys.argv[9]))
    except:
        print("Type \"resize_a4.py --help\" to see usage.")
        exit(1)

    # filename = "resized_aliens1.png"
    # card_count = (5, 5)
    # card_dim = (63, 88)
    # a4_dim = (210, 297)
    # a4_pix = (2480, 3508)

    im = Image.open(filename)
    im = resize_a4(im, card_count, card_dim, a4_dim, a4_pix)

    new_filename = utils.get_filename_with_preffix_suffix(filename, "a4_")
    im.save(new_filename)