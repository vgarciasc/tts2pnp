from PIL import Image
import json

import resize
import resize_a4
import crop_cards
import composite
import utils

if __name__ == "__main__":
    with open('data\\files.json') as f:
        data = json.load(f)

    card_files = data['card_files']

    for group in card_files:
        cards = []

        for cdata in group:
            im = Image.open(cdata['filename'])
            
            im = resize.resize(im, cdata['card_dim'], cdata['card_count'], cdata['maintain_w_or_h'])
            im = resize_a4.resize_a4(im, cdata['card_count'], cdata['card_dim'], data['a4_dim'], data['a4_pix'])
            cropped_cards = crop_cards.crop_cards(im, cdata['card_count'], cdata['card_dim'], data['a4_dim'], data['a4_pix'])
            cards.extend(cropped_cards)
        
        pages = composite.composite(cards, cdata['card_dim'], data['a4_dim'], data['a4_pix'], cdata['margin_mm'], cdata['padding_mm'])

        for i in range(0, len(pages)):
            pagename = utils.get_filename_with_preffix_suffix(group[0]['filename'], "", "_" + str(i))
            pages[i].save(pagename)

