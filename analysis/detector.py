import numpy as np
from PIL import Image

def analyze_image(path):
    img = np.array(Image.open(path))
    lsb = img & 1

    ones = np.sum(lsb)
    zeros = lsb.size - ones

    ratio = ones / (zeros + 1)

    if 0.48 < ratio < 0.52:
        return "⚠️ Suspicious (Possible hidden data)"
    return "✅ Likely clean"