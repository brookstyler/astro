#MAIN SCRIPT code-- COMFIX
#TYLER BROOKS
#12/8/17

from astro import RV2COEfunctions as rf
from astro import COMFIXfunctions as cf
from astro import time
import numpy as np
rad2deg = 180/np.pi
deg2rad = np.pi/180

eartha = 6378.137
earthe = 0.08182

#This text file "COMFIX_results" will carry the same results as
#are shown in the window, simply to test the functionality as
#it is written of creating and printing to a .txt file. The double
#open-close functionality ended up being necessary to produce consistent
#results across MacOS and Windows 10.

create = open("COMFIX_results.txt", "w")
create.close()

results = open("COMFIX_results.txt", "w")
results.write("File Start\n\n")

line = open("COMFIX_tle_measurement.txt")
#Read one line of the text file to get initial 7 values
l1 = line.readline()
l2 = line.readline()
countl = 1

#Priming the conditional "while"-loop ending-- loop will default without
#an initial condition
var = "False"

while var != "True":
    print("\n\nTest Line {}".format(countl))

    #Create 'string' of individual float values
    readarray1 = [float(n) for n in l1.split()]
    #Create arrays of 3 values each through numpy
    lat = np.array(readarray1[0]) * deg2rad
    longit = np.array(readarray1[1]) * deg2rad
    alt = np.array(readarray1[2]) * (0.001)

    t = np.array(readarray1[3])
    #print(longit, lat, alt, t)

    (gst, lst) = time.gstlst(t, longit)
    #print(gst, lst)
    N = (eartha)/(1 - (earthe**2 * (np.sin(lat))**2))**.5
    #print(N)

    readarray2 = [float(n) for n in l2.split()]
    IDN = np.array(readarray2[0])
    rho = np.array(readarray2[1])
    azm = np.array(readarray2[2]) * deg2rad
    ele = np.array(readarray2[3]) * deg2rad
    rhor = np.array(readarray2[4])
    azmr = np.array(readarray2[5]) * deg2rad
    eler = np.array(readarray2[6]) * deg2rad
    #print(IDN, rho, azm, ele, rhor, azmr, eler)

    Recef = cf.ela2ecef(lat, longit, alt, N)
    #print(Recef)

    Reci = cf.ecef2eci(lat, longit, Recef, gst)
    #print(Reci)

    (rsez, vsez) = cf.rvtopos(rho, azm, ele, rhor, azmr, eler)
    #print(vsez.getA1())
    (reci, veci) = cf.sez2eci(lat, lst, rsez, vsez)

    (rfeci, vfeci) = cf.finish(Reci, reci, veci)
    rfecia = rfeci.getA1()
    #print(rfeci.getA1())
    #print(vfeci)

    (rfecia, vfeci, h, n, e) = rf.intermediaries(rfecia, vfeci)

    (a, inc, raan, argp, nu) = rf.rv2coe(rfecia, vfeci, h, n, e)

    (r_a, r_p, sme, period) = rf.optional(rfecia, vfeci, a, e)



    print("r_p (km)        = {}".format(r_p))
    print("r_a (km)        = {}".format(r_a))
    print("sme (km^2/sec^2)= {}".format(sme))
    print("P   (hrs)       = {}".format(period/3600))
    
    print("a   (km)        = {}".format(a))
    print("ecc             = {}\n".format(np.linalg.norm(e)))

    print("inc  (deg)= {}".format(inc))
    print("raan (deg)= {}".format(raan))
    print("argp (deg)= {}".format(argp))
    print("trua (deg)= {}".format(nu))
    """
    v_mag = np.linalg.norm(vfeci)
    r_mag = np.linalg.norm(rfecia)
    """

    #Writing all results into RV2COEresults.txt, formatted
    results.write("----------Result Line {} ----- Obs ID # {}-------------------------------\n".format(countl, IDN))
    results.write("---Satellite RV in ECI frame:\n")
    results.write("\tR = {} (km)        \n\t mag = {}\n".format(rfecia, np.linalg.norm(rfecia)))
    results.write("\tV = {} (km/s)      \n\t mag = {}\n".format(vfeci, np.linalg.norm(vfeci)))
    results.write("---Satellite COEs:\n")
    results.write("\ta   (km)  = {}\n".format(a))
    results.write("\tecc       = {}\n".format(np.linalg.norm(e)))
    results.write("\tinc  (deg)= {}\n".format(inc))
    results.write("\traan (deg)= {}\n".format(raan))
    results.write("\targp (deg)= {}\n".format(argp))
    results.write("\ttrua (deg)= {}\n".format(nu))


    results.write("\tr_p  (km)         = {}\n".format(r_p))
    results.write("\tr_a  (km)         = {}\n".format(r_a))
    results.write("\tsme  (km^2/sec^2) = {}\n".format(sme))
    results.write("\tP    (hrs)        = {}\n".format(period/3600))
    results.write("\t     (s)          = {}\n".format(period))
    results.write("----------------------------------------------------------------------------\n\n\n\n\n\n")



    #Read next lines in order to utilize
    #file ending check, which still works
    #in this twoline read situation
    l1 = line.readline()
    l2 = line.readline()

    countl = countl+1

    #if-else check to determine if the previously
    #read new line is valid, or if loop must stop
    if l1 == (""):
        var = "True"
    else:
        var = "False"

#close file after loop ending
results.close()
