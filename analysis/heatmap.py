import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def generate_heatmap(orig, stego, output="heatmap.png"):
    a = np.array(Image.open(orig))
    b = np.array(Image.open(stego))

    diff = np.abs(a - b)
    heat = diff.sum(axis=2)

    plt.imshow(heat, cmap="hot")
    plt.axis("off")
    plt.savefig(output)
    plt.close()

    return output