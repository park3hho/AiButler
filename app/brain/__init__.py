from PIL import Image


def process_image(img_bytes):
    return Image.open(io.BytesIO(img_bytes))
