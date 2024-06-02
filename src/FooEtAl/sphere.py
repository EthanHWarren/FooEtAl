#gets volume of a sphere from radius using the formula R^3 * pi * 4/3. Since we're using Desmos to check our math, we'll be using pi to the same degree it does, to the 11th place.
def RadVol(radius):
    if(radius > 0):
        return ((radius**3)*(3.14159265359*4))/3
    else:
        return 0