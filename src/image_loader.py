import cv2


def load_image(path):
    image = cv2.imread(path)

    if image is None:
        raise FileNotFoundError(f"Could not load image: {path}")

    return image
