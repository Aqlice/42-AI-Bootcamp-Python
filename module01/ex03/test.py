from matrix import *

m1 = Matrix([[1.0, 3.0],
             [4.0, 5.0],
             [1.0, 6.0],
             [6.0, 2.0]], (4, 2))
mfill = Matrix((4, 4))
print(f'matrix initalized by shape, filled zith 0 :{mfill}')
m2 = Matrix([[0.0, 1.0, 2.0, 3.0],
             [0.0, 2.0, 4.0, 7.0]])
m3 = Matrix([[0.0, 1.0, 2.0, 3.0],
             [2.0, 3.0, 4.0, 5.0],
             [4.0, 5.0, 6.0, 7.0],
             [6.0, 7.0, 8.0, 9.0]])
m4 = Matrix([[0.0, 1.0, 2.0, 3.0]])
print(f'm2 + m2 : {m2 + m2}')
print(f'm2 - m2 : {m2 - m2}')
print(f'm4 * m3 : {m4 * m3}')
print(f'm2 * m1 : {m2 * m1}')
print(f'm1 * m2 : {m1 * m2}')
print(f'm3 / 3 : {m3 / 3}')
m10 = Matrix([[0.0, 1.0, 7.0], [0.0, 4.0, 5.0]])
m11 = Matrix([[0.0, 1.0], [0.0, 2.0]])
print(m10 * m11)
