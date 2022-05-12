import numpy as 
def function_name(h, Qout):
    p = 1000

    u = (1 * 10 ** (-3))

    g = 9.81

    Area = (Qout / C * numpy.sqrt(g * h))

    D = numpy.sqrt((4 * Area) / numpy.pi)

    return(Area, D)

Area1, D1 = function_name(2, 2)
print(Area1, D1)
