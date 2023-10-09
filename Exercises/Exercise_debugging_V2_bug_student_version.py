#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Run line : python3 Exercise_debbuging_V2_bug_student_version.py

# --------------------------------------------------------------------------
# The following code has several errors that you should detect and correct.
# --------------------------------------------------------------------------


"""
The goal of this code is to compute and print the orbit of a planet.
The user can define the basic parameters for the planet (mass, semi-major axis, eccentricity) and the star (mass)
"""
import matplotlib.pyplot as plt

# -----------------------------------------------------------------
# User defined parameters:
Star_mass = 3 # M_Sun
Planet_mass = 0.6 # M_Earth

a = 0.02 # Planet's semi-major axis, in AU.
e = 0.4 # Planet's eccentricity (within [0;1[) (0 = circular, 1 = parabolic)

# -----------------------------------------------------------------
# Conversion to SI
Star_mass = Star_mass * 1.9891E+030 # Sun's mass in [kg]
Planet_mass = Planet_mass * 5.9736E+024 # Earth mass in [kg].

# Other parameters.
G = 0,000000000066743 # m³.kg-¹.s-²

# Using Kepler's third law :
# a^3 / T^2 = GM / (4 pi^2)
# => T = sqrt((4 pi^2 a^3) / GM)

T = np.sqrt((4 * np.pi**2 * a**3) / G * Star_mass)
print("T [s] : ", T, "   T [yr] : ", T/(3600*24*365))

i = 0

# -----------------------------------------------------------------
pos_x = ()
pos_y = ()

# -----------------------------------------------------------------
# Operations
sampling = 4 # Number of points in on the orbit.
print(int(T), int(T/sampling))

# We calculate radius for different points along the orbit / for different fractions of the period
#for i in range(0, int(T), int(T/sampling)):
for i in range(0, sampling):

    mean_anomaly = (360 / T) * (i*T/sampling)
    eccentric_anomaly = Get_eccentric_anomaly(e, mean_anomaly)
    True_anomaly = 2 * np.arctan(np.sqrt((1+e)/(1-e)) * np.tan(eccentric_anomaly / 2))

    r = a * (1-e*np.cos(eccentric_anomaly))

pos_x.append(r * np.cos(true_anomaly))
pos_y.append(r * np.sin(true_anomaly))

print(i, pos_x[-1], pos_y[-1])

f, ax = plt.subplots(nrows=1, ncols=1, subplot_kw={'aspect':'equal'})
plt.plot(pos_x, pos_y, color='blue')
plt.title("Orbit of the planet")
plt.xlabel("[m]")
plt.ylabel("[m]")

plt.plot(0,0,'ro') # star
plt.show()


def Get_eccentric_anomaly(eccentricity, in_mean_anomaly):    # argument2 = 2 par défaut
    """
    This function computes the eccentric_anomaly by iterating over a formula.
    """
    i = 0

    for i in range(0, 6):
        in_eccentric_anomaly = in_mean_anomaly + eccentricity * sin(in_eccentric_anomaly)
        #print("   i:", i, "     E:", in_eccentric_anomaly)
