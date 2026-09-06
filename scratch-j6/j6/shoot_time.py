import time, numpy as np, sys
sys.argv=['x']
exec(open('complexcaps.py').read().split("e=1.0; a1=3.0")[0])
e=1.0; a1=3.0
Tsph=np.pi/2+1j*np.arccosh(a1)
for rt in (1e-10,1e-8,1e-6):
    t0=time.time()
    C5,C7=c5f(-1/6,e),c7f(-1/6,e); s0=1e-3; tt0=s0*Tsph
    y0=np.array([tt0+(-1/6)*tt0**3+C5*tt0**5+C7*tt0**7, 1+3*(-1/6)*tt0**2+5*C5*tt0**4+7*C7*tt0**6, 6*(-1/6)*tt0+20*C5*tt0**3+42*C7*tt0**5, 6*(-1/6)+60*C5*tt0**2+210*C7*tt0**4, 0.0],dtype=complex)
    def rhs(s,y):
        A,B,C,D,I=y
        return Tsph*np.array([B,C,D,FE(A,B,C,D,e),2*np.pi**2*Lreg(A,B,C,e)/A],dtype=complex)
    sol=solve_ivp(rhs,(s0,1.0),y0,method='DOP853',rtol=rt,atol=rt*1e-3)
    print(f"rtol={rt}: {time.time()-t0:.2f}s, nfev={sol.nfev}, status={sol.status}, a(T)={sol.y[0,-1]:.6f} a'(T)={sol.y[1,-1]:.6f} I/a={sol.y[4,-1]:.6f}")
