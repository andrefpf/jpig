from pathlib import Path

import numpy as np
from PIL import Image


class RawImage:
    def __init__(self) -> None:
        self.data = np.array([])
        self.bitdepth = 8

    def width(self):
        if self.data.ndim < 2:
            return 0
        return self.data.shape[1]

    def height(self):
        if self.data.ndim < 2:
            return 0
        return self.data.shape[0]

    def channels(self):
        if self.data.ndim < 3:
            return 1
        return self.data.shape[2]

    def number_of_pixels(self):
        return self.height() * self.width()

    def number_of_samples(self):
        return self.number_of_pixels() * self.channels()

    def get_pixel(self, x: int, y: int) -> np.ndarray:
        return self.data[y, x]

    def get_sample(self, x: int, y: int, channel: int) -> int:
        return self.data[y, x, channel]

    def get_channel(self, channel: int) -> np.ndarray:
        return self.data[:, :, channel]

    def load_file(self, path: str | Path):
        image = Image.open(path)
        self.data = np.array(image)
        return self

    def show(self):
        import matplotlib.pyplot as plt

        plt.imshow(
            self.data,
            vmin=0,
            vmax=(1 << self.bitdepth),
            cmap="gray",
        )
        plt.show()
