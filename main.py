import numpy as np
print('###########ZAD1############')

a = np.arange(3, 3*15+1, 3)
print(a)

print('###########ZAD2############')

a = np.array([3.1, 5.3, 51.2, 8.56, 43.52, 51.09, 4.23])
print(a)
b = a.astype('int64')
print(b)

print('###########ZAD3############')


def foo(n):
    c = np.arange(1, n*n+1, 1)
    c = c.reshape((n, n))
    return c


print('\nPierwsza macierz testowa\n')
print(foo(4))
print('\nDruga macierz testowa\n')
print(foo(3))
print('\nTrzecia macierz testowa\n')
print(foo(8))

print('###########ZAD4###########')


def macpoteg(m, n):
    mpoteg = np.logspace(1, n, num=n, base=m)
    return np.array(mpoteg, dtype=int)


print(macpoteg(2, 16))
print(macpoteg(3, 16))
print(macpoteg(2, 6))
print(macpoteg(5, 7))
print('###########ZAD5###########')


def macdiagonal(m):
    wek = np.arange(m, 0, -1)
    macdiag = np.diag(wek)
    return macdiag


print('\nPierwsza macierz diag testowa\n')
print(macdiagonal(6))
print('\nDruga macierz diag testowa\n')
print(macdiagonal(10))
print('\nTrzecia macierz diag testowa\n')
print(macdiagonal(3))

print('###########ZAD6###########')

s1 = np.array(['W', 'A', 'R', 'S', 'Z', 'A', 'W', 'A'])
macdiagn = np.diag(s1)
macdiagn[:, 2] = ['P', 'E', 'R', 'K', 'U', 'S', 'J', 'A']
macdiagn[7, :] = ['O ', 'D', 'A', 'C', 'O', 'W', 'A', '']
print(macdiagn)

print('###########ZAD7##########')
n=2
s2 = np.arange(n*n)
s3 = s2.reshape((n,n))
print(s3)