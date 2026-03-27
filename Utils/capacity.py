def check_capacity(image, data_bits):
    max_bits = image.size[0] * image.size[1] * 3
    return data_bits <= max_bits