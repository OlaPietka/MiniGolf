from config import sheet_offset, sheet_size


def indexes_2_pixels(i, j, offset=0):
    return i * (sheet_size + offset), j * (sheet_size + offset)


def indexes_2_rect(i, j, with_offset=False):
    x, y = indexes_2_pixels(i, j, sheet_offset)
    xo, yo = int(with_offset) * x + sheet_size, int(with_offset) * y + sheet_size
    return x, y, xo, yo


def pixels_2_indexes(x, y):
    return int(x // sheet_size), int(y // sheet_size)
