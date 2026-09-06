# Item 3.3: regular caps with complex shooting parameter c3, continued along a straight path in the complex tau-plane to a
# complex endpoint T, with the (regularized) Euclidean action integrated along the path. Saddles of the Ostrogradsky
# wave function Psi(a1, K1) are the isolated (c3, T) with a(T) = a1, a'(T) = K1.  Units H0 = 1, action per a_anom.
import sympy as sp, pickle, numpy as np, sys
from scipy.integrate import solve_ivp
d=pickle.load(open('curv.pkl','rb')); tau=sp.symbols('tau'); a=sp.Function('a')(tau)
R,E4,boxR=d['R'],d['E4'],d['boxR']; eps=sp.symbols('epsilon')
A0,A1,A2,A3,A4=sp.symbols('A0 A1 A2 A3 A4')
rep={sp.Derivative(a,(tau,4)):A4,sp.Derivative(a,(tau,3)):A3,sp.Derivative(a,(tau,2)):A2,sp.Derivative(a,tau):A1}
odeE=sp.numer(sp.together(R-sp.Rational(1,2)*E4-eps*boxR)).subs(rep).subs(a,A0)
FE=sp.lambdify((A0,A1,A2,A3,eps),sp.solve(odeE,A4)[0],'numpy')
Rf=sp.lambdify((A0,A1,A2),R.subs(rep).subs(a,A0),'numpy')
c3s=sp.symbols('c3'); c5=c3s*(6*c3s*eps+6*c3s+1)/(20*eps)
c7=sp.solve(60*c3s**3*eps+36*c3s**3+9*c3s**2-136*c3s*c5*eps+120*c3s*c5+10*c5-448*sp.Symbol('c7')*eps,sp.Symbol('c7'))[0]
c5f=sp.lambdify((c3s,eps),c5); c7f=sp.lambdify((c3s,eps),sp.simplify(c7))
def Lreg(A,A1,A2,e):   # regularized Lagrangian per unit eta, per a_anom (J-1 sec 3.1-3.2)
    sp1=A1; sp2=A*A2
    return (-(6/(16*np.pi**2))*A**2*(1+sp1**2) + (1/(16*np.pi**2))*(2*sp2**2+8*(sp1**2-1)) + 36*(-(3*e+1)/(288*np.pi**2))*(1-sp2-sp1**2)**2)
def shoot(c3,T,e,s0=1e-3):
    """integrate from tau0 = s0*T to T along the straight segment; state y=(a,a',a'',a''',I). returns y(T)."""
    C5,C7=c5f(c3,e),c7f(c3,e); t0=s0*T
    y0=np.array([t0+c3*t0**3+C5*t0**5+C7*t0**7, 1+3*c3*t0**2+5*C5*t0**4+7*C7*t0**6, 6*c3*t0+20*C5*t0**3+42*C7*t0**5, 6*c3+60*C5*t0**2+210*C7*t0**4, 0.0],dtype=complex)
    # action from 0 to tau0 along the series: I ~ 2pi^2 int L/a dtau, with L/a -> (1/(16pi^2))*8*(a'^2-1)/a + ... small; include leading term numerically via small-tau expansion of the integrand (finite): use trapezoid on the series
    ss=np.linspace(1e-6,1,200)*t0; aa_=ss+c3*ss**3+C5*ss**5+C7*ss**7; a1_=1+3*c3*ss**2+5*C5*ss**4+7*C7*ss**6; a2_=6*c3*ss+20*C5*ss**3+42*C7*ss**5
    y0[4]=2*np.pi**2*np.trapz(Lreg(aa_,a1_,a2_,e)/aa_,ss)
    def rhs(s,y):
        A,B,C,D,I=y
        return T*np.array([B,C,D,FE(A,B,C,D,e),2*np.pi**2*Lreg(A,B,C,e)/A],dtype=complex)
    sol=solve_ivp(rhs,(s0,1.0),y0,method='DOP853',rtol=1e-10,atol=1e-13)
    return sol.y[:,-1]
def newtonT(c3,T0,e,a1,it=40):
    T=T0
    for k in range(it):
        y=shoot(c3,T,e); f=y[0]-a1
        if abs(f)<1e-11: return T,y
        T=T-f/y[1]     # da/dT = a'(T)
    return T,y
def newton2(c3,T,e,a1,K1,it=60):
    z=np.array([c3,T],dtype=complex)
    for k in range(it):
        y=shoot(z[0],z[1],e); F=np.array([y[0]-a1,y[1]-K1])
        if np.max(np.abs(F))<1e-10: return z,y,True
        h=1e-6; J=np.zeros((2,2),dtype=complex)
        for j in range(2):
            zp=z.copy(); zp[j]+=h; yp=shoot(zp[0],zp[1],e); J[:,j]=(np.array([yp[0]-a1,yp[1]-K1])-F)/h
        try: dz=np.linalg.solve(J,F)
        except np.linalg.LinAlgError: return z,y,False
        if np.max(np.abs(dz))>2: dz=dz*2/np.max(np.abs(dz))
        z=z-dz
    return z,y,np.max(np.abs(F))<1e-8
e=1.0; a1=3.0
Tsph=np.pi/2+1j*np.arccosh(a1)
print("=== sphere check: c3=-1/6, T = pi/2 + i arccosh(3) ===")
y=shoot(-1/6,Tsph,e); print(f"a(T)={y[0]:.6f}  a'(T)={y[1]:.6f}  R(T)={Rf(y[0],y[1],y[2]):.6f}  I/a={y[4]:.6f}   analytic I/a = {(5/2)*(np.cos(Tsph)-1)-e*(np.cos(Tsph)-1)**2*(np.cos(Tsph)+2):.6f}")
print("=== saddles of Psi(a1=3, K1) for the de Sitter-history data K1 = a'(T) = -i sqrt(8) [and +i sqrt(8)] ===")
K1=np.cos(Tsph)
starts=[(-1/6,Tsph),(-0.349489,Tsph),(-0.349489,2.106+1j*1.76),(-0.349489,2.2-1.5j),(-0.3,1.2+2.0j),(0.0,1.0+1.0j),(0.1,0.8+0.5j),(-0.5,2.5+1.0j),(-0.25,1.9+1.4j),(-0.1,1.5+1.8j),(-0.4,1.0-1.6j),(0.05,2.0+2.5j)]
sols=[]
for c30,T0 in starts:
    z,y,ok=newton2(c30,T0,e,a1,K1)
    if ok and np.isfinite(y[4]):
        new=all(abs(z[0]-s[0])>1e-6 or abs(z[1]-s[1])>1e-6 for s in sols)
        if new: sols.append((z[0],z[1],y[4],Rf(y[0],y[1],y[2])))
        print(f"start c3={c30:+.3f},T={T0:.3f} -> {'NEW ' if new else 'dup '}c3={z[0]:.6f}  T={z[1]:.6f}  I/a={y[4]:.5f}  R(T)={Rf(y[0],y[1],y[2]):.4f}")
    else:
        print(f"start c3={c30:+.3f},T={T0:.3f} -> no convergence (c3={z[0]:.3f}, T={z[1]:.3f})")
print("=== the double bubble's complex continuation to a = 3 (c3* fixed at -0.349489): does it reach the dS data? ===")
for T0 in (2.106+1.5j,2.106-1.5j,2.106+2.5j,1.0+1.5j,3.0+1.0j,0.8+2.5j):
    T,y=newtonT(-0.349489,T0,e,a1)
    print(f"  T0={T0:.3f}: T={T:.5f}  a(T)={y[0]:.5f}  a'(T)={y[1]:.5f} (dS data would be {K1:.4f} or {np.conj(K1):.4f})  R(T)={Rf(y[0],y[1],y[2]):.4f}  I/a={y[4]:.5f}")
pickle.dump(sols,open('saddles.pkl','wb'))
