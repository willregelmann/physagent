# Robustness check of the extra complex saddles found at the dS-history data (a1=3, K1=-i sqrt8), eps=1.
# For each: re-shoot with two pole cutoffs and tighter tolerance along the same straight path; polish with Newton; record
# min|a| along the path, the endpoint residuals, the J-1-scheme action, and the corrected-scheme (S^4-ref, pole frame) action.
import numpy as np, sys
sys.argv=['x']
exec(open('ccaps.py').read().split('if __name__')[0])
from scipy.integrate import solve_ivp
e=1.0; a1=3.0; K1=-1j*np.sqrt(8.0)
def Lreg(A,A1,A2,e):
    return (-(6/(16*np.pi**2))*A**2*(1+A1**2) + (1/(16*np.pi**2))*(2*(A*A2)**2+8*(A1**2-1)) + 36*(-(3*e+1)/(288*np.pi**2))*(1-A*A2-A1**2)**2)
def shoot_full(c3,T,e,s0=1e-3,rtol=1e-11):
    t0=s0*T; y=y0_of(c3,e,t0); y=np.concatenate([y,[0j]])
    ss=np.linspace(1e-6,1,400)*t0; C5,C7=c5f(c3,e),c7f(c3,e)
    aa_=ss+c3*ss**3+C5*ss**5+C7*ss**7; a1_=1+3*c3*ss**2+5*C5*ss**4+7*C7*ss**6; a2_=6*c3*ss+20*C5*ss**3+42*C7*ss**5
    y[8]=2*np.pi**2*np.trapz(Lreg(aa_,a1_,a2_,e)/aa_,ss)
    amin=[1e9]
    def rhs(s,Y):
        amin[0]=min(amin[0],abs(Y[0]))
        d=dens(Y[:8],e); return T*np.concatenate([d,[2*np.pi**2*Lreg(Y[0],Y[1],Y[2],e)/Y[0]]])
    sol=solve_ivp(rhs,(s0,1.0),y,method='DOP853',rtol=rtol,atol=1e-14)
    return sol.y[:,-1],amin[0],sol.status
def newton(c3,T,s0):
    z=np.array([c3,T],dtype=complex)
    for k in range(40):
        y,_,_=shoot_full(z[0],z[1],e,s0); F=np.array([y[0]-a1,y[1]-K1])
        if np.max(np.abs(F))<1e-12: break
        h=1e-7; J=np.zeros((2,2),dtype=complex)
        for j in range(2):
            zp=z.copy(); zp[j]+=h; yp,_,_=shoot_full(zp[0],zp[1],e,s0); J[:,j]=(np.array([yp[0]-a1,yp[1]-K1])-F)/h
        dz=np.linalg.solve(J,F); m=np.max(np.abs(dz))
        if m>0.2: dz*=0.2/m
        z=z-dz
    return z
cands=[(-1/6,np.pi/2+1.762747j),(-0.061078-0.074741j,0.958365-7.517934j),(-0.078012-0.080863j,3.646649-7.552073j),(0.011760-0.000057j,-6.007494-4.176755j),(0.006200+0.006758j,4.931966+3.047997j),(-0.160805+0.117255j,-4.089197-8.820504j),(-0.024640+0.090852j,2.969438-8.244251j)]
print("candidate                         s0     |F|        min|a|   I_J1/a                 I_corr/a (S4-ref, pole frame)   R(T)")
for c3,T in cands:
    for s0 in (1e-3,4e-4):
        z=newton(c3,T,s0)
        y,amin,st=shoot_full(z[0],z[1],e,s0)
        F=np.max(np.abs([y[0]-a1,y[1]-K1]))
        print(f"c3={z[0]:.5f} T={z[1]:.4f}  {s0:.0e}  {F:.1e}  {amin:.3f}  {y[8]:+.4f}   {(y[5]+y[6]):+.4f}   R={Rf(y[0],y[1],y[2]):.3f}  status={st}")
