import sys
import utils
from PIL import Image

MAINTAIN_WIDTH = 0
MAINTAIN_HEIGHT = 1

def resize(image, card_count, card_dim, maintain):
    width, height = image.size

    if maintain == MAINTAIN_HEIGHT:
        c = height / (card_dim[1] * card_count[1])
        width = int(card_dim[0] * card_count[0] * c)
    elif maintain == MAINTAIN_WIDTH:
        c = width / (card_dim[0] * card_count[0])
        height = int(card_dim[1] * card_count[1] * c)

    new_size = (width, height)
    return image.resize(new_size, Image.BICUBIC)

if __name__ == "__main__":
    if (len(sys.argv) == 1 or sys.argv[1] == "--help"):
        print("Usage: resize.py [filename] [card_count] [card_dim] [maintain {width = 0 | height = 1}")
        print("Example: resize.py cards.png 5 5 63 88 0")
        print("  this means: \"image 'cards.png' has cards in a 5x5 grid, and the cards have 63mm x 88mm dimensions irl. Resize the image to fix the dimensions, but keep its current width.\"")
        exit(1)
    
    try:
        filename = str(sys.argv[1])
        card_count = (int(sys.argv[2]), int(sys.argv[3]))
        card_dim = (int(sys.argv[4]), int(sys.argv[5]))
        maintain = int(sys.argv[6])
    except:
        print("Type \"resize.py --help\" to see usage.")
        exit(1)

    # filename = "aliens1.png"
    # card_count = (5, 5)
    # card_dim = (63, 88)
    # maintain = MAINTAIN_WIDTH

    im = Image.open(filename)
    im = resize(im, card_count, card_dim, maintain)

    new_filename = utils.get_filename_with_preffix_suffix(filename, "resized_")
    im.save(new_filename)