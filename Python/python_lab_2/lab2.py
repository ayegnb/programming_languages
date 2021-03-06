
#Table for errors:
#+-------+-----------------------+-----------------------+----------------------+
#|   h   |         Euler         |         Heun          | standard Runge-Kutta |
#+=======+=======================+=======================+======================+
#| 0.001 | [-0.00304834          | [-1.03556852e-06      | [-1.67421632e-13     |
#|       | -0.00497444]          | -1.38790976e-06]      | -2.37587727e-13]     |
#+-------+-----------------------+-----------------------+----------------------+
#| 0.002 | [-0.00638668          | [-4.55673849e-06      | [-3.21298543e-12     |
#|       | -0.01041734]          | -6.10582724e-06]      | -4.48974191e-12]     |
#+-------+-----------------------+-----------------------+----------------------+
#| 0.004 | [-0.01242539          | [-1.73155274e-05      | [-4.66873207e-11     |
#|       | -0.02025265]          | -2.32012982e-05]      | -6.54578614e-11]     |
#+-------+-----------------------+-----------------------+----------------------+

#Tables comparing execution time for h = 0.001 and h = 0.002:
#+----------------------+-------+-----------------------+
#|      h = 0.001       |  C++  |        Python         |
#+======================+=======+=======================+
#| Euler                | 0.008 | 0.017733646499982568  |
#+----------------------+-------+-----------------------+
#| Heun                 | 0.008 | 0.037417463200108615  |
#+----------------------+-------+-----------------------+
#| standard Runge-Kutta | 0.008 | 0.06477992860018275   |
#+----------------------+-------+-----------------------+

#+----------------------+-------+-----------------------+
#|      h = 0.002       |  C++  |        Python         |
#+======================+=======+=======================+
#| Euler                | 0.008 | 0.009567251899716212  |
#+----------------------+-------+-----------------------+
#| Heun                 | 0.007 | 0.01858485779957846   |
#+----------------------+-------+-----------------------+
#| standard Runge Kutta | 0.008 | 0.03097252119987388   |
#+----------------------+-------+-----------------------+
#In three different methods C++ was significantly faster than Python.

from scipy import *
from scipy.linalg import *

# runge_kutta1 is Euler's method:
def runge_kutta1( F, x, h ) :
    k1 = F( x )

    return x + h * k1

# runge_kutta21 is Heun's method:
def runge_kutta21( F, x, h ):
    k1 = F( x )
    k2 = F( x + h * k1 )

    return x + h * ( 0.5 * k1 + 0.5 * k2 )

def runge_kutta22( F, x, h ):
    k1 = F( x )
    k2 = F( x + 0.5 * h * k1 )

    return x + h * k2

def runge_kutta31( F, x, h ):
    k1 = F( x )
    k2 = F( x + h * (2.0/3.0) * k1 )
    k3 = F( x + h * ( (1.0/3.0) * k1 + (1.0/3.0) * k2 ) )

    return x + h * ( (1.0/4.0) * k1 + (3.0/4.0) * k3 )

# runge_kutta41 is standard Runge Kutta method:
def runge_kutta41( F, x, h ):
    k1 = F( x )
    k2 = F( x + 0.5 * h * k1 )
    k3 = F( x + 0.5 * h * k2 )
    k4 = F( x + h * k3 )

    return x + ( 1.0 / 6.0 ) * h * ( k1 + 2.0 * k2 + 2.0 * k3 + k4 )

def runge_kutta4_kuntzmann( F, x, h ):
    k1 = F( x )
    k2 = F( x + h * (2.0/5.0) * k1 )
    k3 = F( x + h * ( (-3.0/20.0) * k1 + (3.0/4.0) * k2 ) )
    k4 = F( x + h * ( (19.0/44.0) * k1 + (-15.0/44.0) * k2 +
                     (40.0/44.0) * k3 ) )

    return x + h * ( (55.0/360.0) * k1 + (125.0/360.0) * k2 +
                  (125.0/360.0) * k3 + (55.0/360.0) * k4 )

def runge_kutta5( F, x, h ):
    k1 = f( x )
    k2 = f( x + h * (1.0/4.0) * k1 )
    k3 = f( x + h * ( (1.0/8.0) * k1 + (1.0/8.0) * k2 ) )
    k4 = f( x + h * (1.0/2.0) * k3 )
    k5 = f( x + h * ( (3.0/16.0) * k1 + (-3.0/8.0) * k2 +
                       (3.0/8.0) * k3 + (9.0/16.0) * k4 ) )
    k6 = f( x + h * ( (-3.0/7.0) * k1 + (8.0/7.0) * k2 +
                       (6.0/7.0) * k3 + (-12.0/7.0) * k4 +
                       (8.0/7.0) * k5 ) )

    return x + h * (   ( 7.0 / 90.0 ) * k1 + ( 32.0 / 90.0 ) * k3 +
          ( 12.0 / 90.0 ) * k4 + ( 32.0 / 90.0 ) * k5 +
          ( 7.0 / 90.0 ) * k6 )

def approx( h = 2.1E-3 ) :
    print( "testing Runge-Kutta methods on the catenary" )

    x0 = 0.0
    x1 = 1.0

    mu = 2.0

    s0 = array( [ 1.0 / mu, 0.0 ] )

    p = s0
    x = x0

    def cat( p ) :
        return array( [ p[1], mu * sqrt( 1.0 + p[1] * p[1] ) ] )

    while x + h < x1 :
        p = runge_kutta1( cat, p, h )
        x += h

    p = runge_kutta1( cat, p, x1 - x )
    x = x1

    print( "h = ", h )
    print( "final value = ", p )

    expected = array( [ cosh( mu * x1 ) / mu, sinh( mu * x1 ) ] )
    error = p - expected

    print( "error = ", error )
