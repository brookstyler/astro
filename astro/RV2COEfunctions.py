from astro import constants
#import matplotlib.pyplot as plt
import numpy as np


re = constants.earth.radius
mu = constants.earth.mu


def intermediaries(r, v):


    h = np.cross(r, v)

    h_hat = h / np.linalg.norm(h)

    n = np.cross(np.array([0, 0, 1]), h_hat)

    e = 1 / mu * (( np.linalg.norm(v)**2 - mu / np.linalg.norm(r)) * r - r.dot(v) * v)
    #print(e)
    #print(np.linalg.norm(e))
    #print(e/np.linalg.norm(e))
    #print(np.linalg.norm(e/np.linalg.norm(e)))
    return(r, v, h, n, e)

def rv2coe(r, v, h, n, e):

    #These values, while in another version of this code
    #spread out towards the top, were most useful here
    #for calculations in this format
    v_mag = np.linalg.norm(v)
    r_mag = np.linalg.norm(r)
    v_hat = v / v_mag
    #print("Test")
    #print("|r| = {}".format(r_mag))
    #print("|v| = {}".format(v_mag))
    r_hat = r / r_mag
    h_hat = h / np.linalg.norm(h)
    n_hat = n / np.linalg.norm(n)
    e_hat = e / np.linalg.norm(e)

    p = np.linalg.norm(h)**2 / mu

    ecc = np.linalg.norm(e)

    a = p / (1-ecc**2)

    inc = np.arccos(np.dot(np.array([0, 0, 1]), h_hat)) * 180 / np.pi

    raan_guess = np.arccos(np.dot(np.array([1, 0, 0]), n_hat)) * 180 / np.pi
    #The system I used here, with a "guess" and "check"
    #in the form of if-else statements, was easiest to
    #implement with my current understanding of python
    #logic. The check determines what modification, if any,
    #would be done to the initial "guess".
    raancheck = np.dot(([0,1,0]), n_hat)
    if raancheck < 0:
        if raan_guess > 180:
            raan = raan_guess
        else:
            raan = 360 - raan_guess
    elif raan_guess > 180:
        raan = raan_guess - 180
    else:
        raan = raan_guess


    argp_guess = np.arccos(np.dot(n_hat, e_hat))*180 / np.pi
    argpcheck= np.dot(e_hat, ([0,0,1]))
    if argpcheck < 0:
        if argp_guess > 180:
            argp = argp_guess
        else:
            argp = 360 - argp_guess
    elif argp_guess > 180:
        argp = argp_guess - 180
    else:
        argp = argp_guess

    nu_guess = np.arccos(np.dot(r_hat, e_hat)) * 180 / np.pi
    nucheck = np.dot(r_hat, v_hat)
    if nucheck < 0:
        if nu_guess > 180:
            nu = nu_guess
        else:
            nu = 360 - nu_guess
    elif nu_guess > 180:
        nu = nu_guess - 180
    else:
        nu = nu_guess


    return(a, inc, raan, argp, nu)

def optional(r, v, a, e):
    #optional function, which must only compute two
    #of the minor values based on r and v vectors,
    #so don't need to include other values for calc.
    v_mag = np.linalg.norm(v)
    r_mag = np.linalg.norm(r)

    r_a = a* (1 + np.linalg.norm(e))

    r_p = a* (1 - np.linalg.norm(e))

    specific_mechanical_energy = v_mag**2 / 2 - mu/r_mag

    period = 2*np.pi*(a**3 / mu)**.5

    return(r_a, r_p, specific_mechanical_energy, period)
