from PIL import Image
import json

import resize
import resize_a4
import crop_cards
import composite
import pdf_finish
import utils

if __name__ == "__main__":
    with open('data\\files.json') as f:
        data = json.load(f)

    card_files = data['card_files']
    pdf_pages = []

    for group in card_files:
        cards = []

        for cdata in group['fileData']:
            im = Image.open(cdata['filename'])
            
            im = resize.resize(im, group['card_dim'], cdata['card_count'], cdata['maintain_w_or_h'])
            im = resize_a4.resize_a4(im, cdata['card_count'], group['card_dim'], data['a4_dim'], data['a4_pix'])
            cropped_cards = crop_cards.crop_cards(im, cdata['card_count'], group['card_dim'], data['a4_dim'], data['a4_pix'])
            
            for i in range(0, int(cdata['instances'])):
                cards.extend(cropped_cards)
        
        images = composite.composite(cards, group['card_dim'], data['a4_dim'], data['a4_pix'], group['margin_mm'], group['padding_mm'], group['rotate'], group['bestFit'])
        pdf_pages.extend(images)

        if not data['save_as_pdf']:
            for i in range(0, len(images)):
                imagename = data['outputPath'] + group['name'] + "_" + str(i) + ".png" 
                images[i].save(imagename)
    
    if data['save_as_pdf']:
        pdf_filename = data['outputPath'] + data['game'] + ".pdf"
        pdf_finish.save_images_as_pdf(pdf_pages, pdf_filename)


