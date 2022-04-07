import math
import os
from pathlib import Path
from typing import List, Dict, Any

from pygame import image as pyg_image
from pygame import Rect

_BASE_DIR = Path(os.path.dirname(os.path.realpath(__file__))).parent

SPRITES_PATH = str(_BASE_DIR / 'assets/images')

ship_size = (40, 99)
fort_size = (20, 20)
ship_missile_size = (5, 8)
fort_missile_size = (5, 8)

# 防守方的陆地为一个半圆，半径为224
beach_rect = (224, 0, 448, 224)
# 放置炮台的半圆，处于防守方陆地内，比陆地略小的同心圆，半径为210
fort_beach_rect = Rect(238, 0, 420, 210)


"""
(x - 448)^2 + y^2 = 210^2
from x to y
"""
def get_y_by_x(x):
    y = math.sqrt(210**2 - (x - 448)**2)
    return int(y)


def get_center_rect(rect):
    """
    surface 的坐标(0,0)位于右上角，在发射或瞄准时需要调整至surface中央
    """
    return [i + j / 2 for i, j in zip(rect[:2], rect[2:])]


def pixel_collision2(rect1: Rect,
                     rect2: Rect):
    rect = rect1.clip(rect2)
    if rect.width == 0 or rect.height == 0:
        return False

    return True


def pixel_collision(rect1: Rect,
                    rect2: Rect,
                    hitmask1: List[List[bool]],
                    hitmask2: List[List[bool]]) -> bool:
    rect = rect1.clip(rect2)
    if rect.width == 0 or rect.height == 0:
        return False

    x1, y1 = rect.x - rect1.x, rect.y - rect1.y
    x2, y2 = rect.x - rect2.x, rect.y - rect2.y

    for x in range(rect.width):
        for y in range(rect.height):
            if hitmask1[x1 + x][y1 + y] and hitmask2[x2 + x][y2 + y]:
                return True
    return False


def get_hitmask(image) -> List[List[bool]]:
    mask = []
    for x in range(image.get_width()):
        mask.append([])
        for y in range(image.get_height()):
            mask[x].append(bool(image.get_at((x, y))[3]))
    return mask


def _load_sprite(filename, convert, alpha=True):
    img = pyg_image.load(f"{SPRITES_PATH}/{filename}")
    return (img.convert_alpha() if convert and alpha
            else img.convert() if convert
    else img)


def load_images(convert: bool = True) -> Dict[str, Any]:
    images = {}

    try:
        images["ship"] = _load_sprite("ship.png", convert=convert, alpha=True)
        images["fort"] = _load_sprite("fort.png", convert=convert, alpha=True)
        images["background"] = None
        images["ship_missile"] = _load_sprite("ship_missile.png", convert=convert, alpha=True)
        images["fort_missile"] = _load_sprite("fort_missile.png", convert=convert, alpha=True)

    except FileNotFoundError as ex:
        raise FileNotFoundError("Can't find the sprites folder! No such file or"
                                f"directory: {SPRITES_PATH}") from ex
    return images


def load_image(filename, convert: bool = True) -> Any:
    try:
        image = _load_sprite(f"{filename}.png", convert=convert, alpha=True)
    except FileNotFoundError as ex:
        raise FileNotFoundError("Can't find the sprites folder! No such file or"
                                f"directory: {SPRITES_PATH}") from ex
    return image


if __name__ == '__main__':
    img1 = load_image('ship', False)
    mask1 = get_hitmask(img1)
    img2 = load_image('fort_missile', False)
    mask2 = get_hitmask(img2)
    c = pixel_collision(Rect(11, 0, 5, 8), Rect(0, 0, 40, 99), mask2, mask1)
    print(c)