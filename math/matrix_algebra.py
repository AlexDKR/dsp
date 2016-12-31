# Matrix Algebra

import numpy as np
import sys

A = np.array([[ 1, 2, 3], [ 2, 7, 4]])
B = np.array([[1, -1], [0, 1]])
C = np.array([[5, -1], [9, 1], [6, 0]])
D = np.array([[3, -2, -1], [1, 2, 3]])

u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.array([[1], [8], [0], [5]])

alpha = np.array(6)

print 'A:'
print A
print
print 'B: '
print B
print
print 'C: '
print C
print
print 'D: '
print D
print
print
print
print 'u: '
print u
print 
print 'v: '
print v
print
print 'w: '
print w
print
print
print
print 'alpha = %s' % str(alpha)
print
print
print
print '1. Matrix Dimensions'
print '1.1 A: %s' % str(A.shape)
print '1.2 B: %s' % str(B.shape)
print '1.3 C: %s' % str(C.shape)
print '1.4 D: %s' % str(D.shape)
print '1.5 u: %s' % str(u.shape)
print '1.6 w: %s' % str(w.shape)
print 
print '2. Vector Operations'
print '2.1 u + v'
print u + v
print
print '2.2 u - v'
print u - v
print
print '2.3 alpha u'
print alpha * u
print
print '2.4 u dot v'
print np.dot(u, v)
print
print '2.5 ||u|| '
print np.linalg.norm(u)
print 
print
print
print '3. Matrix Operations'
print '3.1 A + C'
try:
    print A + C
except:
    print 'not possible, %s' % sys.exc_info()[1]
print
print '3.2 A - C(T)'
print A - np.matrix.transpose(C)
print
print '3.3 C(T) + 3D'
print np.matrix.transpose(C) + 3 * D
print
print '3.4 BA'
try:
    print B * A 
except:
    print 'not possible, %s' % sys.exc_info()[1]
print
print '3.5 BA(T)'
try:
    print B * np.matrix.transpose(A)
except:
    print 'not possible, %s' % sys.exc_info()[1]
print
print
print
print 'Optional'
print '3.6 BC'
try:
    print B * C
except:
    print 'not possible, %s' % sys.exc_info()[1]
print
print '3.7 CB'
try:
    print C * B
except:
    print 'not possible, %s' % sys.exc_info()[1]
print
print '3.8 B^4'
print B ^ 4
print
print '3.9 AA(T)'
try:
    print A * (np.matrix.transpose(A))
except:
    print 'not possible, %s' % sys.exc_info()[1]
print
print '3.10 D(T)D'
try:
    print (np.matrix.transpose(D)) * D
except:
    print 'not possible, %s' % sys.exc_info()[1]

