# Attack check: the real regular family at eps=1 reaching a1=3 at real proper length, with (i) J-1's ESU-scheme action
# (position T's table) and (ii) the corrected S^4-reference action of PR #222 (position H's ccaps.py density, pole-anchored
# frame theta ~ tau at the pole).  Reports sup and inf of I along the family, and the curvature at the cut vs Mbar_P^2.
import numpy as np, sys
sys.argv=['x']
exec(open('ccaps.py').read().split('if __name__')[0])
from scipy.integrate import solve_ivp
e=1.0; a1=3.0
def Lreg(A,A1,A2,e):   # J-1 scheme density per unit eta (per a_anom)
    return (-(6/(16*np.pi**2))*A**2*(1+A1**2) + (1/(16*np.pi**2))*(2*(A*A2)**2+8*(A1**2-1)) + 36*(-(3*e+1)/(288*np.pi**2))*(1-A*A2-A1**2)**2)
def realcap(c3,e,a1=3.0,t0=2e-3):
    y=y0_of(c3,e,t0); y=np.concatenate([y,[0j]])   # append J-1 action accumulator
    ss=np.linspace(1e-6,1,400)*t0
    C5,C7=c5f(c3,e),c7f(c3,e)
    aa_=ss+c3*ss**3+C5*ss**5+C7*ss**7; a1_=1+3*c3*ss**2+5*C5*ss**4+7*C7*ss**6; a2_=6*c3*ss+20*C5*ss**3+42*C7*ss**5
    y[8]=2*np.pi**2*np.trapz(Lreg(aa_,a1_,a2_,e)/aa_,ss)
    def rhs(s,Y):
        d=dens(Y[:8],e); return np.concatenate([d,[2*np.pi**2*Lreg(Y[0],Y[1],Y[2],e)/Y[0]]])
    hit=lambda s,Y: (Y[0]-a1).real; hit.terminal=True; hit.direction=1
    turn=lambda s,Y: Y[1].real; turn.terminal=True; turn.direction=-1
    sol=solve_ivp(rhs,(t0,80),y,method='DOP853',rtol=1e-10,atol=1e-13,events=[hit,turn])
    if len(sol.t_events[0]): return sol.t_events[0][0],sol.y_events[0][0]
    return None,(sol.y_events[1][0] if len(sol.t_events[1]) else None)
MbarP2=1e6/(1440*np.pi**2)
print(f"eps={e}, a1={a1}; Mbar_P^2 (H0=1, a2=1e6) = {MbarP2:.1f}")
print("   c3        T        K1=a'(T)   R(T)      theta(T)   I_J1/a     I_EH+R2/a   Gamma/a    I_corr/a   dI(corr-J1)")
grid=np.concatenate([[-0.0049,-0.004,-0.003,-0.002,-0.001],np.linspace(0,0.02,11)[1:],[0.03,0.05,0.07,0.1,0.15,0.2,0.3,0.5,0.7,1.0,2.0,3.0,10.0]])
grid=np.concatenate([[0.0],grid]); grid=np.unique(grid)
rows=[]
for c3 in grid:
    T,y=realcap(c3,e)
    if T is None: print(f"{c3:+.4f}  never reaches 3; a_max={y[0].real if y is not None else float('nan'):.4f}"); continue
    Ic=(y[5]+y[6]).real; IJ=y[8].real
    rows.append((c3,T,y[1].real,Rf(y[0],y[1],y[2]).real,y[4].real,IJ,y[5].real,y[6].real,Ic))
    print(f"{c3:+.4f}  {T:7.4f}  {y[1].real:8.4f}  {Rf(y[0],y[1],y[2]).real:9.3f}  {y[4].real:7.4f}  {IJ:9.4f}  {y[5].real:10.4f}  {y[6].real:9.4f}  {Ic:10.4f}  {Ic-IJ:+8.4f}")
rows=np.array(rows)
i=np.argmax(rows[:,8]); j=np.argmin(rows[:,8])
print(f"\ncorrected scheme: sup I/a over scanned real family = {rows[i,8]:.4f} at c3={rows[i,0]:+.4f}; inf = {rows[j,8]:.1f} at c3={rows[j,0]:+.3f} (unbounded below as c3 -> inf)")
i=np.argmax(rows[:,5]); print(f"J-1 scheme:       sup I/a = {rows[i,5]:.4f} at c3={rows[i,0]:+.4f}")
k=rows[np.abs(rows[:,3])<MbarP2]; print(f"|R(T)| < Mbar_P^2 up to c3 = {k[:,0].max():+.3f}")
# sphere half at the Lorentzian data for reference (corrected): -(10/3+4e)/2
print(f"sphere half-action (corrected) = {-(10/3+4*e)/2:.4f}; flat ball GH term -(3/4) a1^2 = {-(3/4)*a1**2:.4f}")
