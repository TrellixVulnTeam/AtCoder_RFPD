import math
import numpy as np


def main():
    a1, a2, a3 = map(int, input().split())

    if(a1 - a2 == a2 - a3):
        print("Yes")
    elif(a2 - a1 == a1 - a3):
        print("Yes")
    elif(a1 - a3 == a3 - a2):
        print("Yes")
    else:
        print("No")


if(__name__ == "__main__"):
    main()
