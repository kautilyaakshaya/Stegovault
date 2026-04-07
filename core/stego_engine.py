import random
from PIL import Image

from core.crypto import encrypt_data, decrypt_data, get_seed
from core.container import pack_files, unpack_files


# =========================
# BIT HELPERS
# =========================

def bytes_to_bits(data):
    return ''.join(format(b, '08b') for b in data)


def bits_to_bytes(bits):
    return bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))


def set_2_lsb(value, bits):
    return (value & 0b11111100) | int(bits, 2)


def get_2_lsb(value):
    return format(value & 0b11, '02b')


# =========================
# HIDE DATA (STABLE)
# =========================

def hide_data(image_path, files, password, output_path):

    packed = pack_files(files)
    encrypted = encrypt_data(packed, password)

    header = len(encrypted).to_bytes(4, 'big')
    final = header + encrypted

    bits = bytes_to_bits(final)

    image = Image.open(image_path).convert("RGB")
    pixels = list(image.getdata())

    # 🔑 Stable random seed
    seed = get_seed(password)
    random.seed(seed)

    indices = list(range(len(pixels)))
    random.shuffle(indices)

    capacity = len(pixels) * 3 * 2

    if len(bits) > capacity:
        raise ValueError("❌ Data too large for this image")

    new_pixels = pixels.copy()
    bit_index = 0

    for idx in indices:
        if bit_index >= len(bits):
            break

        r, g, b = new_pixels[idx]

        for channel in range(3):
            if bit_index >= len(bits):
                break

            bit_pair = bits[bit_index:bit_index+2].ljust(2, '0')
            bit_index += 2

            if channel == 0:
                r = set_2_lsb(r, bit_pair)
            elif channel == 1:
                g = set_2_lsb(g, bit_pair)
            else:
                b = set_2_lsb(b, bit_pair)

        new_pixels[idx] = (r, g, b)

    out = Image.new("RGB", image.size)
    out.putdata(new_pixels)
    out.save(output_path)


# =========================
# EXTRACT DATA (STABLE)
# =========================

def extract_data(image_path, password):

    image = Image.open(image_path).convert("RGB")
    pixels = list(image.getdata())

    seed = get_seed(password)
    random.seed(seed)

    indices = list(range(len(pixels)))
    random.shuffle(indices)

    bits = ""

    for idx in indices:
        r, g, b = pixels[idx]
        bits += get_2_lsb(r)
        bits += get_2_lsb(g)
        bits += get_2_lsb(b)

    # 🔹 Read header
    header_bits = bits[:32]
    length = int(header_bits, 2)

    total_bits = 32 + (length * 8)

    if total_bits > len(bits):
        return None  # corrupted

    data_bits = bits[32:total_bits]
    encrypted = bits_to_bytes(data_bits)

    try:
        decrypted = decrypt_data(encrypted, password)
    except:
        return None

    return unpack_files(decrypted)