import numpy as np, pickle, sys
exec(open('complexcaps.py').read().split("e=1.0; a1=3.0")[0])
from scipy.integrate import solve_ivp
def shoot2(c3,T,e,s0=1e-3):
    C5,C7=c5f(c3,e),c7f(c3,e); t0=s0*T
    y0=np.array([t0+c3*t0**3+C5*t0**5+C7*t0**7, 1+3*c3*t0**2+5*C5*t0**4+7*C7*t0**6, 6*c3*t0+20*C5*t0**3+42*C7*t0**5, 6*c3+60*C5*t0**2+210*C7*t0**4, 0.0],dtype=complex)
    ss=np.linspace(1e-6,1,200)*t0; aa_=ss+c3*ss**3+C5*ss**5+C7*ss**7; a1_=1+3*c3*ss**2+5*C5*ss**4+7*C7*ss**6; a2_=6*c3*ss+20*C5*ss**3+42*C7*ss**5
    y0[4]=2*np.pi**2*np.trapz(Lreg(aa_,a1_,a2_,e)/aa_,ss)
    def rhs(s,y):
        A,B,C,D,I=y
        return T*np.array([B,C,D,FE(A,B,C,D,e),2*np.pi**2*Lreg(A,B,C,e)/A],dtype=complex)
    small=lambda s,y: abs(y[0])-0.02; small.terminal=True; small.direction=-1
    big=lambda s,y: abs(y[0])-40.0; big.terminal=True
    sol=solve_ivp(rhs,(s0,1.0),y0,method='DOP853',rtol=1e-9,atol=1e-12,events=[small,big])
    if sol.status!=0 or len(sol.t_events[0]) or len(sol.t_events[1]): return None
    return sol.y[:,-1]
def Tnewton(c3,T,e,a1,it=25):
    y=None
    for k in range(it):
        y=shoot2(c3,T,e)
        if y is None: return None,None
        f=y[0]-a1
        if abs(f)<1e-11: return T,y
        dT=-f/y[1]
        if abs(dT)>1.0: dT=dT/abs(dT)
        T=T+dT
    return (T,y) if (y is not None and abs(y[0]-a1)<1e-8) else (None,None)
def find(c3,T,e,a1,K1,it=30):
    for k in range(it):
        T,y=Tnewton(c3,T,e,a1)
        if T is None: return None
        g=y[1]-K1
        if abs(g)<1e-9: return (c3,T,y[4],Rf(y[0],y[1],y[2]),y[1])
        h=1e-6
        T2,y2=Tnewton(c3+h,T,e,a1)
        if T2 is None: return None
        dg=(y2[1]-K1-g)/h
        dc=-g/dg
        if abs(dc)>0.1: dc=0.1*dc/abs(dc)
        c3=c3+dc
    return None
