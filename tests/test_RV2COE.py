from Astro import RV2COEfunctions as func
import numpy as np
from Astro import constants
#import pdb

def test_intermediaries():
    r = np.array([8840.,   646.,  5455.])
    v = np.array([-0.695,  5.25,  -1.65 ])
    #pdb.set_trace()
    h_exp = np.cross(r, v)
    h_hat = h_exp/(np.linalg.norm(h_exp))
    n_exp = np.cross(np.array([0, 0, 1]), h_hat)
    mu = constants.earth.mu
    e_exp = 1 / mu * (( np.linalg.norm(v)**2 - mu / np.linalg.norm(r)) * r - r.dot(v) * v)

    (r, v, h, n, e) = func.intermediaries(r, v)

    np.testing.assert_allclose(h_exp,h)
    np.testing.assert_allclose(n_exp,n)
    np.testing.assert_allclose(e_exp,e)

def test_rv2coe():
    r = np.array([ 8840.,   646., 5455.])
    v = np.array([-0.695,  5.25,  -1.65 ])
    h_exp = np.cross(r, v)
    h_hat = h_exp/(np.linalg.norm(h_exp))
    n = np.cross(np.array([0, 0, 1]), h_hat)
    mu = constants.earth.mu
    #pdb.set_trace()
    e = 1 / mu * ((np.linalg.norm(v)**2 - mu / np.linalg.norm(r)) * r - r.dot(v) * v)

    a_exp = 8697.5027477616
    inc_exp = 33.9987398270207
    raan_exp = 250.02867617596
    argp_exp = 255.537162105505
    nu_exp = 214.854752906377
    (a, inc, raan, argp, nu) = func.rv2coe(r, v, h_exp, n, e)

    np.testing.assert_allclose(a, a_exp)
    np.testing.assert_allclose(inc, inc_exp)
    np.testing.assert_allclose(raan, raan_exp)
    np.testing.assert_allclose(argp, argp_exp)
    np.testing.assert_allclose(nu, nu_exp)

def test_optional():
    r = np.array([ 8840.,   646., 5455.])
    v = np.array([-0.695,  5.25,  -1.65 ])
    #h = np.cross(r, v)
    a = 8697.5027477616
    #h_hat = h/(np.linalg.norm(h))
    #n = np.cross(np.array([0, 0, 1]), h)
    mu = constants.earth.mu
    e = 1 / mu * (( np.linalg.norm(v)**2 - mu / np.linalg.norm(r)) * r - r.dot(v) * v)

    r_a_exp = 11134.4743561659
    r_p_exp = 6260.53113935728
    sme_exp = -22.9146521455589
    period_exp = 2.24233404065916
    (r_a, r_p, sme, period) = func.optional(r, v, a, e)

    np.testing.assert_allclose(r_a, r_a_exp)
    np.testing.assert_allclose(r_p, r_p_exp)
    np.testing.assert_allclose(sme, sme_exp)
    np.testing.assert_allclose(period/3600, period_exp)
