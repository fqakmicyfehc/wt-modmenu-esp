import numpy as np


class ViewMatrix:
    def __init__(self, matrix: np.ndarray) -> None:
        self.m = matrix.reshape(4, 4)

    def project(self, world: np.ndarray, width: int, height: int):
        clip = self.m @ np.append(world, 1.0)
        if clip[3] <= 0:
            return None
        ndc = clip[:3] / clip[3]
        return (
            (ndc[0] + 1.0) * 0.5 * width,
            (1.0 - ndc[1]) * 0.5 * height,
        )