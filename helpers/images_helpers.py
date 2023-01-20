from pygame import image, Surface, transform
from os import path


def load_image(folder_path: str, image_name: str) -> Surface:
    image_path: str = path.join("images", folder_path, image_name)
    return image.load(image_path)


def rotate_image(surface: Surface, angle: float | int) -> Surface:
    return transform.rotate(surface, angle)


def scale_image(surface: Surface, size: tuple) -> Surface:
    return transform.scale(surface, size)


def flip_image_x(surface: Surface) -> Surface:
    return transform.flip(surface, True, False)
