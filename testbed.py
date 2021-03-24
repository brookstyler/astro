#from Astro import RV2COEfunctions as func
from astro import tfunctions as tf
from astro import PROPOGATEfunctions as pf
import numpy as np
from numpy import linalg as ln
#from Astro import RV2COEfunctions as rf
#import numpy as np



"""
a = 25512.6
e = .5
i = 0
raan = 0
argp = 35
nu = 4.96821
i = i* (np.pi/180)
raan = raan* (np.pi/180)
argp = argp* (np.pi/180)

(rvec_new, vvec_new) = pf.coe2rv(a, e, i, raan, argp, nu)
print(rvec_new, vvec_new)
print(ln.norm(rvec_new), ln.norm(vvec_new))
"""
a = tf.test()
print(a)

"""
#KEEP THIS CHUNK, IT'S THE TWO IMPORTANT TRANFORMATION MATRICES

PERI2ECI = np.matrix([[np.cos(raan)*np.cos(argp)-np.sin(raan)*np.sin(argp)*np.cos(i), -np.cos(raan)*np.sin(argp)-np.sin(raan)*np.cos(argp)*np.cos(i), np.sin(raan)*np.sin(i)],
                      [np.sin(raan)*np.cos(argp)+np.cos(raan)*np.sin(argp)*np.cos(i), -np.sin(raan)*np.sin(argp)+np.cos(raan)*np.cos(argp)*np.cos(i), -np.cos(raan)*np.sin(i)],
                      [np.sin(argp)*np.sin(i), np.cos(argp)*np.sin(i), np.cos(i)]])
ECI2PERI = np.linalg.inv(PERI2ECI)


LVLH2PERI = np.matrix([[np.cos(nu), np.sin(nu), 0],
                       [-np.sin(nu), np.cos(nu), 0],
                       [0, 0, 1]])
PERI2LVLH = np.linalg.inv(LVLH2PERI)


dv = np.matrix([[0.1],[-.25], [.2]])
dvperi = ECI2PERI * dv
dvlvlh = PERI2LVLH * dvperi
#print(PERI2ECI)

#print(ECI2PERI)

#print(PERI2ECI*ECI2PERI)
print(dv)
print(np.linalg.norm(dv))
print(dvperi)

print(np.linalg.norm(dvperi))
print(dvlvlh)

print(np.linalg.norm(dvlvlh))
"""
