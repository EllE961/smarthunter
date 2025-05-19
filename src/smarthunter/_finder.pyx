# cython: language_level=3, boundscheck=False, wraparound=False
from libc.string cimport memchr
cimport cython

@cython.cfunc
cdef inline bint _is_hex(unsigned char c):
    return (c >= 0x30 and c <= 0x39) or (c | 0x20 >= 0x61 and c | 0x20 <= 0x66)

@cython.ccall
def find_url_sequences(memoryview[const unsigned char] buf):
    cdef Py_ssize_t n = buf.shape[0]
    cdef Py_ssize_t i = 0
    cdef Py_ssize_t start = -1
    cdef list hits = []

    while i < n:
        cdef void* p = memchr(&buf[0] + i, ord('%'), n - i)
        if p == NULL:
            break
        i = <Py_ssize_t>(p - <void*>&buf[0])

        if i + 2 < n and _is_hex(buf[i+1]) and _is_hex(buf[i+2]):
            if start == -1:
                start = i
            i += 3
            continue
        if start != -1 and i - start >= 6:
            hits.append(start)
        start = -1
        i += 1

    if start != -1 and n - start >= 6:
        hits.append(start)
    return hits 