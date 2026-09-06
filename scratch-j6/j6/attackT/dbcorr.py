# Attack check: corrected-scheme (S^4-reference, pole-anchored frame) actions of the four real saddles the position found
# at the double-bubble data (a1=0.5585, K1=0), eps=1, and of the sphere's half cap at its equator, for the ordering under e^{+I}.
import numpy as np, sys
sys.argv=['x']
exec(open('ccaps.py').read().split('if __name__')[0])
from scipy.integrate import solve_ivp
e=1.0
def cap_to_T(c3,T):
    y,_=integrate_path(c3,e,[T]); return y
def Lreg(A,A1,A2,e):
    return (-(6/(16*np.pi**2))*A**2*(1+A1**2) + (1/(16*np.pi**2))*(2*(A*A2)**2+8*(A1**2-1)) + 36*(-(3*e+1)/(288*np.pi**2))*(1-A*A2-A1**2)**2)
def IJ1(c3,T,t0=2e-3):
    C5,C7=c5f(c3,e),c7f(c3,e)
    y0=[t0+c3*t0**3+C5*t0**5+C7*t0**7, 1+3*c3*t0**2+5*C5*t0**4+7*C7*t0**6, 6*c3*t0+20*C5*t0**3+42*C7*t0**5, 6*c3+60*C5*t0**2+210*C7*t0**4, 0.0]
    ss=np.linspace(1e-6,1,400)*t0; aa_=ss+c3*ss**3+C5*ss**5+C7*ss**7; a1_=1+3*c3*ss**2+5*C5*ss**4+7*C7*ss**6; a2_=6*c3*ss+20*C5*ss**3+42*C7*ss**5
    y0[4]=2*np.pi**2*np.trapz(Lreg(aa_,a1_,a2_,e)/aa_,ss)
    sol=solve_ivp(lambda s,y:[y[1],y[2],y[3],FE(y[0],y[1],y[2],y[3],e),2*np.pi**2*Lreg(y[0],y[1],y[2],e)/y[0]],(t0,T),y0,method='DOP853',rtol=1e-10,atol=1e-13)
    return sol.y[4,-1]
print("saddle (c3, T)            a(T)     a'(T)     R(T)     I_J1/a    I_loc/a   Gamma/a   I_corr/a")
for lab,c3,T in (("sym. double bubble half",-0.349817,2.104599),("asym. double bubble",-0.381120,1.989454),("small cap",-0.605654,0.948418),("large cap",-0.253912,3.140067),("sphere half (equator)",-1/6,np.pi/2)):
    y=cap_to_T(c3,T); ij=IJ1(c3,T)
    print(f"{lab:24s} c3={c3:+.4f} T={T:.4f}: a={y[0].real:.4f} a'={y[1].real:+.4f} R={Rf(y[0],y[1],y[2]).real:7.3f}  {ij:8.4f}  {y[5].real:8.4f}  {y[6].real:8.4f}  {(y[5]+y[6]).real:8.4f}")
