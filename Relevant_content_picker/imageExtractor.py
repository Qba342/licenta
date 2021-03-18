import pytesseract
from bs4 import BeautifulSoup
import requests

class ImageExtractor:
    def __init__(self, link_to_image , output_path):
        self.link_to_image = link_to_image
        self.output_path=output_path

    def extract(self):
        print("a")