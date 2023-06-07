import pytesseract
import cv2
from pathlib import Path

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convert_image_to_text(image_path):
    image_path = str(image_path)
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU |
                                 cv2.THRESH_BINARY_INV)

    text = pytesseract.image_to_string(thresh1, lang='rus').replace('\xa3', '').replace('\xe9', '')
    with open(f'train/texts/{image_path[13:-4]}.txt', 'w') as text_file:
        text_file.write(text)
    with open(f'train/entities/{image_path[13:-4]}.json', 'w') as entities_file:
        entities_file.write('')




directory = 'train/images'
pathlist = Path(directory).glob('*.*')
for path in pathlist:
    convert_image_to_text(path)
