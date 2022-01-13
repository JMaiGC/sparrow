from app.layoutlmv2 import process_document
from PIL import Image, ImageDraw, ImageFont


def main():
    image = Image.open('docs/invoice.jpg')
    image = process_document(image)
    image.save('docs/invoice_processed.jpg')

if __name__ == "__main__":
    main()
