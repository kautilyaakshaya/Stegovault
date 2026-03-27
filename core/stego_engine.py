import random
from PIL import Image
from core.crypto import encrypt, decrypt
from core.container import pack_files, unpack_files
from Utils.capacity import check_capacity

EOF = "1111111111111110"


def to_bin(data):
    return ''.join(format(b, '08b') for b in data)


def from_bin(binary):
    return bytes(int(binary[i:i+8], 2) for i in range(0, len(binary), 8))


def generate_positions(width, height, seed):
    random.seed(seed)
    positions = [(x, y, c) for y in range(height) for x in range(width) for c in range(3)]
    random.shuffle(positions)
    return positions


def hide_data(image_path, files, password, output_path):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()

    container = pack_files(files)
    encrypted = encrypt(container, password)

    binary = to_bin(encrypted) + EOF

    positions = generate_positions(img.width, img.height, password)

    if not check_capacity(img, len(binary)):
        raise ValueError("Data too large for image")

    for i, bit in enumerate(binary):
        x, y, c = positions[i]
        pixel = list(pixels[x, y])
        pixel[c] = pixel[c] & ~1 | int(bit)
        pixels[x, y] = tuple(pixel)

    img.save(output_path)


def extract_data(image_path, password):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()

    positions = generate_positions(img.width, img.height, password)

    binary = ""

    for x, y, c in positions:
        binary += str(pixels[x, y][c] & 1)
        if binary.endswith(EOF):
            break

    binary = binary[:-len(EOF)]
    data = from_bin(binary)

    decrypted = decrypt(data, password)
    if decrypted is None:
        return None

    return unpack_files(decrypted)