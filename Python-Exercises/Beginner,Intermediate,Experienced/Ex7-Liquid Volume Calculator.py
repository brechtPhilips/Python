from math import pi
def CalculateLiquidVolume(h,r=10):

    liquidVolume = ((4* pi * r**3) /3) - (pi * h**2 * ( 3*r - h) / 3)
    return liquidVolume


print(CalculateLiquidVolume(2))