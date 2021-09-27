import numpy as np
from scipy.fftpack import dct, idct

def dct2(a):
    return dct( dct( a, axis=0, norm='ortho' ), axis=1, norm='ortho' )

def idct2(a):
    return idct( idct( a, axis=0 , norm='ortho'), axis=1 , norm='ortho')

mat_wht4x4 = np.array([[1, 1, 1, 1],[1, -1, 1, -1],[1, 1, -1, -1],[1, -1, -1, 1]]) / 2

def wht4x4(a):
    return np.dot(a, mat_wht4x4)

def iwht4x4(a):
    return np.dot(a, mat_wht4x4)

def zigzag(N):
    try:
        zz_mtx = np.zeros((N,N))
    except TypeError as err:
        print("N must be an integer, error msg: {0}".format(err))
        return -1
    except ValueError as err:
        print("N must be larger than 0, error msg: {0}".format(err))
        return -1

    for n in range(2,N+2):
        zz_mtx[n-2, 0] = 1/2*((-1)**n)*(n+((-1)**n)*((n-2)*n+2)-2)
    for i in range(1, N+1):
        for j in range(2, N+1):
            if ((i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1)):
                zz_mtx[i-1, j-1] = zz_mtx[i-1, j-2] + (2*i-1)
            else:
                zz_mtx[i-1, j-1] = zz_mtx[i-1, j-2] + (j-1)*2
    zz_mtx = np.fliplr(zz_mtx)
    for i in range(2, N+1):
        for j in range(1, N):
            if i > j:
                zz_mtx[i-1, j-1] = zz_mtx[i-1, j-1] - (i - j) ** 2
    zz_mtx = np.fliplr(zz_mtx)    
    return zz_mtx