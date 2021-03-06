from scipy import *
from scipy.linalg import *

def solution( ) :
    print( "Here are the answers of Aiya Yegenberdiyeva:" )

    m1 = array( [ [ 1/2, 1/3 ], [ -2/7, 2/ 8 ]] )
    m2 = array( [ [ -1/3, 2/7 ], [ 2/5, -1/7 ]] )
    m3 = array( [ [ -1/5,2/3], [1/8, 3/11] ] )

    p = array( [ [ -1/30, 2/21 ], [ 41/210, -23/196 ] ] )
    I = array( [ [ 42, -56 ], [ 48, 84 ]] ) / 37

    print( "This is part 1\n" )
    print( "The product of m1 and m2 is:" )
    print( dot(m1,m2) )
    print( "We can show that dot product of m1 and m2 indeed equals to matrice p, by subtracting p from the dot product:" )
    print( dot(m1, m2) - p )
    print( "------------------" )

    print( "This is part 2\n" )
    print( "The inverse of m1 is:" )
    print( inv(m1) )
    print( "We can show that the inverse of m1 indeed equals to matrice I, by subtracting I from the inverse:")
    print( inv(m1) - I )
    print( "------------------")

    print( "This is part 3\n" )
    print( "The product of (m1.m2).m3 is:" )
    print( dot(dot(m1, m2), m3) )
    print( "The product of m1.(m2.m3) is:" )
    print( dot(m1, dot(m2, m3)) )
    print( "The above two matrices are almost equal:" )
    print( dot(dot(m1, m2), m3) - dot(m1, dot(m2, m3)) )
    print( "Thus, matrix multiplication is associative." )
    print( "------------------")

    print( "This is part 4\n" )
    print( "1) The expression m1.(m2 + m3) is equal to:" )
    print( dot(m1, (m2 + m3)) )
    print( "The expression m1.m2 + m1.m3 is equal to:")
    print( dot(m1, m2) + dot(m1, m3) )
    print( "The above two matrices are almost equal:" )
    print( dot(m1, (m2 + m3)) - (dot(m1, m2) + dot(m1, m3)) )
    print( "2) The expression (m1 + m2).m3 is equal to:")
    print( dot((m1 + m2), m3) )
    print( "The expression m1.m3 + m2.m3 is equal to:")
    print( dot(m1, m3) + dot(m2, m3) )
    print( "The above two matrices are almost equal:" )
    print( dot((m1 + m2), m3) - (dot(m1, m3) + dot(m2, m3)) )
    print( "Thus, matrix multiplication is distributive on both sides." )
    print( "------------------")

    print( "This is part 5\n" )
    v = array( [ 3.0, -1 ] )
    print( "The expression m1(m2(v)) is equal to:" )
    print( dot(m1, dot(m2, v)) )
    print( "The expression (m1.m2)(v) is equal to:" )
    print( dot(dot(m1, m2), v) )
    print( "The above two expressions are almost equal:")
    print( dot(m1, dot(m2, v)) - dot(dot(m1, m2), v) )
    print( "Thus, matrix multiplication corresponds to composition of application." )
    print( "------------------")

    print( "This is part 6\n" )
    print( "The expression det(m1).det(m2) is equal to:" )
    print( dot(det(m1), det(m2)) )
    print( "The expression det(m1.m2) is equal to:" )
    print( det(dot(m1, m2)) )
    print( "The above two expressions are equal:" )
    print( dot(det(m1), det(m2)) - det(dot(m1, m2)) )
    print( "Thus, determinant commutes over multiplication.")
    print( "------------------")

    print( "This is part 7\n" )
    print( "The expression m1.inv(m1) is equal to:" )
    print( dot(m1, inv(m1)) )
    print( "The expression inv(m1).m1 is equal to:" )
    print( dot(inv(m1), m1) )
    print( "The above to matrices are approximately equal to the identity matrix, and by subtracting them, we get:" )
    print( dot(m1, inv(m1)) - dot(inv(m1), m1) )
    print( "Thus, the inverse of matrix is indeed inverse." )
    print( "------------------")
