from pygame import image, Surface, transform
from os import path


def load_image(image_name: str) -> Surface:
    image_path: str = path.join("images", image_name)
    return image.load(image_path)


def rotate_image(surface: Surface, angle: float | int) -> Surface:
    return transform.rotate(surface, angle)


def scale_image(surface: Surface, size: tuple) -> Surface:
    return transform.scale(surface, size)
