import math
def s(h, H, S):
    return math.sqrt(h*h+S*S)*H/h


if __name__ == "__main__":
    print(squirrel(4, 16, 3))
    print(squirrel(8, 9, 37))