# https://www.codewars.com/kata/5908242330e4f567e90000a3/train/python
# def circleIntersection(a,b,r):
#     d=hypot(a[0]-b[0], a[1]-b[1])
#     st=d*(r*r-.25*d*d)**.5
#     sarc=acos(d*d/r/r/2-1)*r*r
#     S=int(sarc-st)
#     print(S)


# note: sin2a = 2*sina*cosa

# js answer
# with(Math)circleIntersection=([a,b],[c,d],r)=>(-sin(x=2*acos(hypot(a-c,b-d)/2/r))+x)*r*r|0
# def circleIntersection(a,b,r):from math import *;d=hypot(a[0]-b[0],a[1]-b[1]);return int(acos(d/r/2)*r*r*2-d*(r*r-d*d/4)**.5)
# circleIntersection=lambda a,b,r:[int(acos(d/r/2)*r*r*2-d*(r*r-d*d/4)**.5)for d in[hypot(a[0]-b[0],a[1]-b[1])]][0]
# def circleIntersection(a,b,r):import math as m;a=2*m.acos(m.hypot(a[0]-b[0],a[1]-b[1])/r/2);return int((a-m.sin(a))*r*r)
# def circleIntersection(a,b,r):import cmath as m;c=complex;d=abs(c(*a)-c(*b));return int(m.acos(d/r/2)*r*r*2-d*(r*r-d*d/4)**.5)
def circleIntersection(a,b,r):from cmath import *;c=complex;o=2*acos(abs(c(*a)-c(*b))/r/2);return int((o-sin(o)).real*r*r)


if __name__ == "__main__":
    print(circleIntersection([0,0],[7,0],5))
    print(circleIntersection([38, -18],[46, -29],10))