from .basic_transform import BasicTransform
from typing import List
import numpy as np
import random

class Identity(BasicTransform):
    """
    Does not change the input images
    """
    def transform(self, images: List[np.ndarray]):
        self.check_images(images)
        return images

class Transpose(BasicTransform):
    """
     Transposes the image.
     """
    def transform(self, images: List[np.ndarray]):
        self.check_images(images)
        res = []
        for im in images:
            res.append(np.transpose(im, (1, 0, 2)))
        return res


class RandomRotation90(BasicTransform):
    """
     Rotates the image by 90 degrees, from 0 to 3 times

     Parameters
     ----------
     factor : int
         Number of times the image will be rotated. You can choose a value between 0 or 3 or leave it random if you don't specify.
     """

    def __init__(self, factor=random.randint(0, 3)):
        self.factor = factor

    def transform(self, images: List[np.ndarray]):
        self.check_images(images)
        res = []
        for im in images:
            switcher = {
                0: im,
                1: np.transpose(im, (1, 0, 2))[:, ::-1, :],
                2: np.transpose(im, (1, 0, 2))[::-1, :, :],
                3: im[::-1, :, :]
            }
            res.append(switcher.get(self.factor))
        return res
