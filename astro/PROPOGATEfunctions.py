#Functions code
#TYLER BROOKS
#11/12/17

from astro import constants
import numpy as np

re = constants.earth.radius
mu = constants.earth.mu
def update(r0, a, e, i, raan, argp, nu, t):
    nur = nu * (np.pi/180)
    E0 = np.arccos((a-r0)/(a*e))
    #Quadrant check for E0-- necessary as arccos only
    #Produces values from 0 to pi
    if nur > np.pi:
        if E0 < np.pi:
            E0 = 2*np.pi - E0
        else:
            print("impossible")
    else:
        0
    M0 = E0 - e*(np.sin(E0))
    n = (mu/(r0**3))**(1/2)
    Mf = n*t + M0
    #Call Newton function, defined below
    (nuf, Ef, count) = newton(Mf, e)
    return (nuf, Ef, count)

def newton(Mf, e):
    Ef = 2
    #above value is simply to prime the variable:
    # not doing so resulted in occasional errors
    Efg = Mf
    err = 10**-12
    delE = 1
    count = 0
    #Conditional in while loop ensures that values are approaching a single values
    #With a precision of +- 10^(-12)
    while (np.absolute(delE) > err):
        Ef = (Efg + (Mf - (Efg - e*np.sin(Efg)))/(1-e*np.cos(Efg)))
        delE = Ef - Efg
        count = count+1
        Efg = Ef
    nuf = 2* (np.arctan( ((1+e)/(1-e))**(1/2) * np.tan(Ef/2)))



    #Below is to ensure that final value of nu is always positive,
    #measured from periapsis (even if later computation would work with
    #negative values)
    if nuf < 0:
        nuf = 2*np.pi + nuf

    return(nuf, Ef, count)

def coe2rv(a, e, i, raan, argp, nuf):
    N_hat = np.array([np.cos(raan), np.sin(raan)])
    #The below 3-value array is necessary
    #to make the later computations
    #of ur_hat and un_hat possible
    N_hat_add = np.array([N_hat[0], N_hat[1], 0])

    h_hat = np.array([np.sin(i)*np.cos(raan), -np.sin(i)*np.cos(raan), np.cos(i)])
    Nt_hat = np.array([-np.sin(raan)*np.cos(i), np.cos(raan)*np.cos(i), np.sin(i)])

    ur_hat = np.cos(nuf+argp)*N_hat_add + np.sin(nuf+argp)*Nt_hat
    un_hat = -np.sin(nuf+argp)*N_hat_add + np.cos(nuf+argp)*Nt_hat

    rnew = (a*(1-e**2))/(1+e*np.cos(nuf))
    smee = -mu/(2*a)
    vnew = (2*(smee + mu/rnew))**(1/2)
    fpa_new = np.arctan((e*np.sin(nuf))/(1+(e*np.cos(nuf))))
    rvec_new = rnew*ur_hat
    vvec_new = vnew*np.cos(fpa_new)*un_hat + vnew*np.sin(fpa_new)*ur_hat

    return(rvec_new, vvec_new)
