#MAIN SCRIPT code
#TYLER BROOKS
#11/12/17


from astro import RV2COEfunctions as func
from astro import PROPOGATEfunctions as tf
import numpy as np

#This text file "PROPOGATE_reults" will carry the same results as
#are shown in the window, simply to test the functionality as
#it is written of creating and printing to a .txt file. The double
#open-close functionality ended up being necessary to produce consistent
#results across MacOS and Windows 10.
create = open("PROPOGATE_results.txt", "w")
create.close()

results = open("PROPOGATE_results.txt", "w")
results.write("File Start\n\n")

line = open("PROPOGATE_tle_rvt.txt")
#Read one line of the text file to get initial 7 values
l = line.readline()

countl = 1

#Priming the conditional "while"-loop ending-- loop will default without
#an initial condition
var = "False"

while var != "True":
    print("\n\nTest Line {}".format(countl))

    #Create 'string' of individual float values
    readarray = [float(n) for n in l.split()]
    #Create arrays of 3 values each through numpy
    r0V = np.array(readarray[0:3])
    v0V = np.array(readarray[3:6])
    r0 = np.linalg.norm(r0V)
    v0 = np.linalg.norm(v0V)
    t = readarray[6]
    print("Initial Values:\n     R = {}".format(r0V))
    print("     V = {}".format(v0V))
    print("     t = {}".format(t))


    #Simply calling each function in the RV2COEfunctions
    #file, storing values localy to input to RV2COEresults.txt


    #here I will introduce temporary checking procedure
    (r0V, v0V, h, n, e) = func.intermediaries(r0V, v0V)

    (a, inc, raan, argp, nu) = func.rv2coe(r0V, v0V, h, n, e)
    print("     nu_0 = {}".format(nu))
    (r_a, r_p, sme, period) = func.optional(r0V, v0V, a, e)
    #The following conversions are needed for the new
    #PROPOGATE-related functions
    inc = inc* (np.pi/180)
    raan = raan* (np.pi/180)
    argp = argp* (np.pi/180)
    ecc = np.linalg.norm(e)

    (nuf, Ef, count) = tf.update(r0, a, ecc, inc, raan, argp, nu, t)

    (rvec_new, vvec_new) = tf.coe2rv(a, ecc, inc, raan, argp, nuf)
    #Optional block of code which will print neatly
    #formatted results in the command window
    """
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
    v0_mag = np.linalg.norm(v0)
    r0_mag = np.linalg.norm(r0)


    #Writing all results into RV2COEresults.txt, formatted
    results.write("Result Line {}\n".format(countl))
    results.write("R = {} (km)        mag = {}\n".format(r0V, r0))
    results.write("V = {} (km/s)      mag = {}\n".format(v0V, v0))



    results.write("t = {} (s) \n".format(t))
    results.write("r_p (km)        = {}\n".format(r_p))
    results.write("r_a (km)        = {}\n".format(r_a))
    results.write("sme (km^2/sec^2)= {}\n".format(sme))
    results.write("P   (hrs)       = {}\n".format(period/3600))
    results.write("a   (km)        = {}\n".format(a))
    results.write("ecc             = {}\n".format(np.linalg.norm(e)))
    results.write("inc  (deg)= {}\n".format(inc*180/np.pi))
    results.write("raan (deg)= {}\n".format(raan*180/np.pi))
    results.write("argp (deg)= {}\n".format(argp*180/np.pi))
    results.write("trua (deg)= {}\n".format(nu))
    results.write("\nFinal Result:\n")
    results.write("trua_f (deg) = {}\n".format(nuf*(180/np.pi)))
    results.write("R_f    (km)  = {}       mag = {}\n".format(rvec_new, np.linalg.norm(rvec_new)))
    results.write("V_f    (km/s)= {}\n\n\n\n\n".format(vvec_new))
    print("Updated Values:")
    print("     Rf = {}".format(rvec_new))
    print("     Vf = {}".format(vvec_new))
    print("     nu_f = {}".format(nuf*180/np.pi))

    #Read next line in order to utilize
    #file ending check
    l = line.readline()

    countl = countl+1

    #if-else check to determine if the previously
    #read new line is valid, or if loop must stop
    if l == (""):
        var = "True"
    else:
        var = "False"

#close file after loop ending
results.close()
