from astro import RV2COEfunctions as func
import numpy as np
from astro import constants
print(constants.mars.mu)

#This text file "RV2COEreults" will carry the same results as
#are shown in the window, simply to test the functionality as
#it is written of creating and printing to a .txt file. The double
#open-close functionality ended up being necessary to produce consistent
#results across MacOS and Windows 10.
create = open("RV2COEresults.txt", "w")
create.close()

results = open("RV2COEresults.txt", "w")
results.write("File Start\n\n")

line = open("RV2.txt")
#Read one line of the text file to get initial 6 values
l = line.readline()

count = 1

#Priming the conditional while loop ending, loop defaulted without
#an initial condition
var = "False"

while var != "True":
    print("\n\n Test Line {}".format(count))

    #Create 'string' of individual float values
    readarray = [float(n) for n in l.split()]
    #Create arrays of 3 values each through numpy
    r = np.array(readarray[0:3])
    v = np.array(readarray[3:6])
    print("R = {}".format(r))
    print("V = {}\n".format(v))
    print(np.linalg.norm(r))
    print(np.linalg.norm(v))

    #Simply calling each function in the RV2COEfunctions
    #file, storing values localy to input to RV2COEresults.txt
    (r, v, h, n, e) = func.intermediaries(r, v)

    (a, inc, raan, argp, nu) = func.rv2coe(r, v, h, n, e)

    (r_a, r_p, sme, period) = func.optional(r, v, a, e)

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
    v_mag = np.linalg.norm(v)
    r_mag = np.linalg.norm(r)
    #print("Test")
    #print("|r| = {}".format(r_mag))
    #print("|v| = {}".format(v_mag))

    #Writing all results into RV2COEresults.txt, formatted
    results.write("Test Line {}\n".format(count))
    results.write("R = {}\n".format(r))
    results.write("V = {}\n".format(v))
    results.write("r_p (km)        = {}\n".format(r_p))
    results.write("r_a (km)        = {}\n".format(r_a))
    results.write("sme (km^2/sec^2)= {}\n".format(sme))
    results.write("P   (hrs)       = {}\n".format(period/3600))
    results.write("a   (km)        = {}\n".format(a))
    results.write("ecc             = {}\n".format(np.linalg.norm(e)))
    results.write("inc  (deg)= {}\n".format(inc))
    results.write("raan (deg)= {}\n".format(raan))
    results.write("argp (deg)= {}\n".format(argp))
    results.write("trua (deg)= {}\n\n".format(nu))

    #Read next line in order to utilize
    #file ending check
    l = line.readline()

    count = count+1

    #if-else check to determine if the previously
    #read new line is valid, or if loop must stop
    if l == (""):
        var = "True"
    else:
        var = "False"

#close file after loop ending
results.close()
