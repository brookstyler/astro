#PROPOGATE TEST code
#TYLER BROOKS
#11/12/17


from Astro import PROPOGATEfunctions as func
import numpy as np
from Astro import constants


def test_updatenewton():
    #This test serves as an effective test of not only update,
    #but also newton, and as such they are bundled together in this test.
    #One would not work without the other, and their outputs are identical.

    #provided information:
    r = np.array([8840.,   646.,  5455.])
    r_mag = np.linalg.norm(r)
    t = 0.00
    a = 8697.502747761597
    e = 0.2801921056054277
    i = 33.998739827020664
    raan = 250.02867617596
    argp = 255.53716210550525
    nu = 214.85475290637697

    #adaptation to fit function formatting
    i = i* (np.pi/180)
    raan = raan* (np.pi/180)
    argp = argp* (np.pi/180)

    #Ef taken from hand calculation for this nu
    Ef_exp = 3.9345155448

    #Run function
    (nuf, Ef, count) = func.update(r_mag, a, e, i, raan, argp, nu, t)

    #Calculate nuf_exp using formula in function
    nuf_exp = 2* (np.arctan( ((1+e)/(1-e))**(1/2) * np.tan(Ef/2)))
    if nuf_exp < 0:
        nuf_exp = 2*np.pi + nuf_exp
    #note: nuf_exp == nu
    np.testing.assert_allclose(Ef, Ef_exp)
    np.testing.assert_allclose(nuf, nuf_exp)


def test_coe2rv():
    #Provided information
    a = 8697.502747761597
    e = 0.2801921056054277
    i = 33.998739827020664
    raan = 250.02867617596
    argp = 255.53716210550525
    nuf = 214.85475290637697*(np.pi/180)

    #Adapting values to function
    i = i* (np.pi/180)
    raan = raan* (np.pi/180)
    argp = argp* (np.pi/180)

    #Expected values
    r_exp = np.array([8840.,   646.,  5455.])
    v_exp = np.array([-0.695,  5.25,  -1.65 ])

    #Call function
    (rvec_new, vvec_new) = func.coe2rv(a, e, i, raan, argp, nuf)

    np.testing.assert_allclose(rvec_new, r_exp)
    np.testing.assert_allclose(vvec_new, v_exp)
