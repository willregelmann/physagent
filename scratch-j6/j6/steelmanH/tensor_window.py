# HHR tensor quadratic form F(p,alpha,beta) (their eq. 3.76/3.82 as transcribed in ../tensorF.py), alpha=-eps/2, in the window 1/4<eps<eps_c
import numpy as np
from scipy.special import digamma as psi
def Psi(p): return p*(p+1)*(p+2)*(p+3)*(psi(p/2+2.5)+psi(p/2+2)-psi(2)-psi(1)) + p**4+2*p**3-5*p**2-10*p-6
def F(p,eps,beta): return p**2+3*p+6 + Psi(p) + 2*beta*p*(p+1)*(p+2)*(p+3) - 4*(-eps/2)*p*(p+3)
ps=np.arange(2,2001)
for eps in (0.2,0.25,0.3,0.355,1.0):
    for beta in (np.log(2)-1,0.0,1.0,-1.0):
        v=F(ps,eps,beta); neg=ps[v<0]
        print(f"eps={eps:5.3f} beta={beta:+.3f}: tensor modes with F<0 (negative modes of I under e^-I): {'none up to p=2000' if len(neg)==0 else f'p in [{neg.min()},{neg.max()}]'}")
