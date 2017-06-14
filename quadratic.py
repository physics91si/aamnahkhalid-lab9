#!/usr/bin/python
import sys
import math

#Python script that returns the roots of a quadratic equation
#of the form a*x^2 + b*x + c = 0
#Enter values for a, b, and c in the command line
#e.g. run: >python quadratic.py 1 2 -15


"""EDITED TO REMOVE ERRORS"""
def main():
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = int(sys.argv[3])
        ans = find_roots(a, b, c)
        print ("This is x1: " + str(ans[0]))
        print ("This is x2: " + str(ans[1]))
       
    except (ValueError):
        if 'math' in str(sys.exc_info()[1]):
            print("That's mathematically wrong. Might not have real roots at all. \nDescartes can't help ya")
        else: 
            print("Please enter valid numbers only")
    except (ZeroDivisionError):
        print("Coefficient of x^2 can't be 0. Sorry life ain't fair.")

    except: 
        print("Well, this is awkward. Unexpected error:", sys.exc_info()[0])


def find_roots(a,b,c):
    mid = b*b - 4*a*c
    sqrt_mid = math.sqrt(mid)
    x1 = (-b + sqrt_mid)/(2*a)
    x2 = (-b - sqrt_mid)/(2*a)
    return (x1, x2)


if __name__=="__main__":
        main()
