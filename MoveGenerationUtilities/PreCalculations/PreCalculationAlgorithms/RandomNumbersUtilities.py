from ctypes import c_uint32, c_uint64

random_state = 1804289383


def get_32b_rand_no() -> c_uint32:
    global random_state
    number = c_uint32(random_state).value
    number ^= c_uint32(number << 13).value
    number ^= c_uint32(number >> 17).value
    number ^= c_uint32(number << 5).value
    random_state = number
    return c_uint32(random_state)


def get_64b_rand_no() -> c_uint64:
    n1 = c_uint64((c_uint64(get_32b_rand_no().value)).value & 0xFFFF).value
    n2 = c_uint64((c_uint64(get_32b_rand_no().value)).value & 0xFFFF).value
    n3 = c_uint64((c_uint64(get_32b_rand_no().value)).value & 0xFFFF).value
    n4 = c_uint64((c_uint64(get_32b_rand_no().value)).value & 0xFFFF).value
    return c_uint64(n1 | (n2 << 16) | (n3 << 32) | (n4 << 48))
