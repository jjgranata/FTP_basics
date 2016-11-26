
def checksum(st):
    return reduce(lambda x, y: x + y, map(ord, st))


def checksum256(st):
    return reduce(lambda x, y: x + y, map(ord, st)) % 256
