import pytesseract
import io
from PIL import Image
import requests
import utils

class ImageExtractor:
    def __init__(self, link_to_image="" ):
        pytesseract.pytesseract.tesseract_cmd=r"C:/Program Files/Tesseract-OCR/tesseract.exe"
        self.link_to_image=link_to_image
        self.text=''

    def set_link(self,link):
        self.link_to_image=link

    def extract(self):
        try:
            resp=requests.get(self.link_to_image)
            img = Image.open(io.BytesIO(resp.content))
            self.text = utils.get_rid_of_spaces(pytesseract.image_to_string(img))
        except:
            pass
            #print(f'Invalid URL: "{self.link_to_image}"')



