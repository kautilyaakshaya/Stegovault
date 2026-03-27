import struct


def pack_files(files: list):
    container = b""

    for filename, data in files:
        name_bytes = filename.encode()
        container += struct.pack("I", len(name_bytes))
        container += name_bytes
        container += struct.pack("I", len(data))
        container += data

    return container


def unpack_files(data: bytes):
    files = []
    i = 0

    while i < len(data):
        name_len = struct.unpack("I", data[i:i+4])[0]
        i += 4

        name = data[i:i+name_len].decode()
        i += name_len

        size = struct.unpack("I", data[i:i+4])[0]
        i += 4

        file_data = data[i:i+size]
        i += size

        files.append((name, file_data))

    return files