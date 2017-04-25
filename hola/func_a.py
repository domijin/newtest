
import math 

inf = float('inf')  # this is a quick-and-easy way to get the "infinity" value 

def function_a(angle=180):
    anglerad = math.radians(angle)
    return math.sin(anglerad/2)/math.sin(anglerad)