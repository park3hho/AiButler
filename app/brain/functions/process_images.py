from PIL import Image
import io


def process_image(image_bytes_list):
    return [Image.open(io.BytesIO(img_bytes)) for img_bytes in image_bytes_list]

