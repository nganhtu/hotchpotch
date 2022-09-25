# https://vnoi.info/wiki/algo/trick/FFT.md


import numpy as np
import fourier


def multiply(p, q):
    fp = fourier.fft(p)
    fq = fourier.fft(q)
    fh = list(np.multiply(np.array(fp), np.array(fq)))
    h = fourier.reverse_fft(fh)
    return h
