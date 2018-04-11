from birdseye import eye
import numpy as np

@eye
def poly(x):
    return 3*x**3-4*x**2+7*x-10

@eye
def main():
    X = np.arange(10)
    Y = poly(X)
    
    for x,y in zip(X,Y):
        print("{0:7d}  {1:7d}\n").format(x,y)

main()

