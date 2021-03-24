from astro import constants
#import matplotlib.pyplot as plt
import numpy as np

###DOES NOT WORK
re = constants.earth.radius
mu = constants.earth.mu

def update(r0, v0, a, e, i, raan, argp, nu, t):
    """
    r0 = np.linalg.norm([ 8840.,   646.,  5455.])
    v0 = np.linalg.norm([-0.695,  5.25,  -1.65 ])
    t = 12.0
    a = 8697.502747761597
    e = 0.2801921056054277
    i = 33.998739827020664
    raan = 250.02867617596
    argp = 255.53716210550525
    nu0 = 214.85475290637697
    """

    #r0n = np.linalg.norm(r0)
    #print("r0 = {}".format(r0))
    #print("a = {}".format(a))

    E0 = np.arccos((a-r0)/(a*e))
    print("E0 = {}".format(E0))
    #print("E0 = {}".format(E0))
    M0 = E0 - e*(np.sin(E0))
    print("M0 = {}".format(M0))
    n = (mu/(r0**3))**(1/2)
    Mf = n*t + M0
    print("Mf = {}".format(Mf))
    (nuf, Ef, count) = newton(Mf, e)

    return (nuf, Ef, count)

def newton(Mf, e):
    Ef = 2
    Efg = Mf
    err = 10**-10
    delE = 1
    #print(err)
    count = 0
    while (np.absolute(delE) > err):
        #print(Efg)
        Ef = (Efg + (Mf - (Efg - e*np.sin(Efg)))/(1-e*np.cos(Efg)))
        #print(Ef)
        delE = Ef - Efg
        #print(delE)
        #print("\n")
        count = count+1
        #print(count)
        Efg = Ef
    #if ((Efnew - Ef) < err):
    #    Ef = Efnew
    print("Ef = {}".format(Ef))
    nufi = (np.arctan( ((1+e)/(1-e))**(1/2) * np.tan(Ef/2)))

    if (0<= Ef <= np.pi/2):
        nuf = 2*nufi
        print("branch 1")
    if (np.pi/2 <= Ef <= np.pi):
        nuf = 2*(np.pi-nufi)
        print("branch 2")
    if (np.pi <= Ef <= np.pi*(3/2)):
        nuf = 2*(np.pi + nufi)
        print("branch 3")
    if (-np.pi/2 <= Ef < 0):
        nuf = 2*(2*np.pi - nufi)
        print("branch 4")
    print("nuf = {}".format(nuf))

    return(nuf, Ef, count)


def coe2rv(a, e, i, raan, argp, nuf):
    #Running eq pulled from sheet, not current version of alg)
    N_hat = np.array([np.cos(raan), np.sin(raan)])
    #print(N_hat)
    N_hat_add = np.array([N_hat[0], N_hat[1], 0])
    #print(N_hat_add)
    h_hat = np.array([np.sin(i)*np.cos(raan), -np.sin(i)*np.cos(raan), np.cos(i)])
    #print(h_hat)
    Nt_hat = np.array([-np.sin(raan)*np.cos(i), np.cos(raan)*np.cos(i), np.sin(i)])
    #print(Nt_hat)
    #Nt_hat_add = np.array([Nt_hat[0], Nt_hat[1], 0])
    #Nt_had_sol = np.array([0, 0, Nt_hat[2]])
    #print(Nt_hat_add)
    #print(Nt_had_sol)

    ur_hat = np.cos(nuf+argp)*N_hat_add + np.sin(nuf+argp)*Nt_hat
    #print(ur_hat)
    un_hat = -np.sin(nuf+argp)*N_hat_add + np.cos(nuf+argp)*Nt_hat
    #print(un_hat)

    rnew = (a*(1-e**2))/(1+e*np.cos(nuf))
    smee = -mu/(2*a)
    vnew = (2*(smee + mu/rnew))**(1/2)
    #print(mu)
    fpa_new = np.arctan((e*np.sin(nuf))/(1+(e*np.cos(nuf))))
    rvec_new = rnew*ur_hat
    vvec_new = vnew*np.cos(fpa_new)*un_hat + vnew*np.sin(fpa_new)*ur_hat

    print("rnew = {}".format(rnew))
    print("smee = {}".format(smee))
    print("vnew = {}".format(vnew))
    print("fpa_new = {}".format(fpa_new))
    print("rvec_new = {}".format(rvec_new))
    print("vvec_new = {}".format(vvec_new))



    return(rvec_new, vvec_new)

def test():
    print(6)
    return 1
