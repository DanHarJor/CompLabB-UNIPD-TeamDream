import numpy as np

# a nonlinear function of a 2d array x
def f(x,c=1):
    r=0
    if c==1: #TRIANGLE
        if x[0]>-20 and x[1]>-40 and x[0]+x[1] < 40:
            r=1
    if c==2: #COMPLEX SYMMETRIC CIRCULAR
        if (np.sign(x.sum())*np.sign(x[0]))*np.cos(np.linalg.norm(x)/(2*np.pi))>0:
            r=1
    if c==3: #CIRCLE
        if (x[0]**2 + x[1]**2)<400:
            r=1
    if c==4: #FLAG DESIGN
        if 40*np.sin(x[0]) < x[1]:
            r=1
    return r


def filename(s,TYPE=1):
    return "./DATA/"+s+"-for-DNN-"+str(TYPE)+".dat"
