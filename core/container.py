def pack_files(files):
    data = b''

    for name, content in files:
        name_bytes = name.encode()
        data += len(name_bytes).to_bytes(2, 'big')
        data += name_bytes
        data += len(content).to_bytes(4, 'big')
        data += content

    return data


def unpack_files(data):
    files = []
    i = 0

    while i < len(data):
        name_len = int.from_bytes(data[i:i+2], 'big')
        i += 2

        name = data[i:i+name_len].decode()
        i += name_len

        size = int.from_bytes(data[i:i+4], 'big')
        i += 4

        content = data[i:i+size]
        i += size

        files.append((name, content))

    return files