#COMFIX FUNCTIONS code
#TYLER BROOKS
#12/8/17

import numpy as np
from astro import constants

def ela2ecef(lat, longit, h, N):
    e = 0.08182
    Recef = np.matrix([[(N+h)*np.cos(longit)*np.cos(lat)],[(N+h)*np.sin(longit)*np.cos(lat)],[((1-e**2)*N+h)*np.sin(lat)]])
    return(Recef)

def ecef2eci(lat, longit, recef, gst):
    gst = gst*-1
    R = np.matrix([[np.cos(gst), np.sin(gst), 0],[-np.sin(gst), np.cos(gst), 0],[0, 0, 1]])
    #print(R)
    Reci = R*recef
    return(Reci)

def rvtopos(rho, azm, ele, rhor, azmr, eler):
    rsez = np.matrix([[-rho*np.cos(ele)*np.cos(azm)],[rho*np.cos(ele)*np.sin(azm)],[rho*np.sin(ele)]])
    #print(rsez)
    vsez = np.matrix([[-rhor*np.cos(ele)*np.cos(azm) + rho*eler*np.sin(ele)*np.cos(azm) + rho*azmr*np.cos(ele)*np.sin(azm)],
                       [rhor*np.cos(ele)*np.sin(azm) -rho*eler*np.sin(ele)*np.sin(azm) +  rho*azmr*np.cos(ele)*np.cos(azm)],
                       [rhor*np.sin(ele) + rho*eler*np.cos(ele)]])
    #print(vsez)
    return(rsez, vsez)

def sez2eci(lat, lst, rsez, vsez):
    D = np.matrix([[np.sin(lat)*np.cos(lst), np.sin(lat)*np.sin(lst), -np.cos(lat)],
                    [-np.sin(lst), np.cos(lst), 0],
                    [np.cos(lat)*np.cos(lst), np.cos(lat)*np.sin(lst), np.sin(lat)]])
    #print(D)
    reci = np.transpose(D)*rsez
    veci = np.transpose(D)*vsez

    
    return(reci, veci)


def finish(Reci, reci, veci):
        #note-- the operation here __.getA1() flattens a matrix out into an array
        #inside of numpy for the sake of ensuring that all matrices are printed
        #and handled correctly for operations.
    rfeci = Reci + reci
    vfeci = veci.getA1() + np.cross(np.array([0, 0, constants.earth.omega]),(rfeci.getA1()), axis=0)

    return(rfeci, vfeci)
