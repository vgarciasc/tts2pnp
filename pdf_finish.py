import sys 
from PIL import Image

def save_images_as_pdf(images, pdf_filename, resolution=100.0):
    rgb_list = []

    for image in images:
        if image.mode is 'RGB':
            rgb_list.append(image)
        else:
            rgb = Image.new('RGB', image.size, (255, 255, 255))
            rgb.paste(image, mask=image.split()[3])
            rgb_list.append(rgb)

    rgb_list[0].save(pdf_filename, "PDF", resolution=resolution, save_all=True, append_images=rgb_list[1:])

if __name__ == "__main__":
    if (len(sys.argv) == 1 or sys.argv[1] == "--help"):
        print("Usage: pdf_finish.py [pdf_filename] [image_filename]+")
        print("Example: pdf_finish.py cards.pdf cards_0.png cards_1.png")
        print("  this means: \"create a pdf file named 'cards.pdf' with the pages 'cards_0.png' and 'cards_1.png'\"")
        exit(1)
    
    try:
        pdf_filename = str(sys.argv[1])
        image_names = []
        for i in range(2, len(sys.argv)):
            image_names.append(sys.argv[i])
    except:
        print("Type \"pdf_finish.py --help\" to see usage.")
        exit(1)

    im_list = []
    for image_name in image_names:
        im = Image.open(image_name)
        im_list.append(im)
    
    save_images_as_pdf(im_list, pdf_filename)
