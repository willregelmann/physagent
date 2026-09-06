# Attack check: broader saddle search at the de Sitter-history data (a1=3, K1=-i sqrt8), eps=1, J-1 scheme (existence is
# scheme-independent), with starting c3 in the runaway range and in the small-cap range, using the position's own nested
# Newton (dbdata_lib.find) and its 2D Newton (dbdata.newton2).  Reports every distinct saddle and Re I.
import numpy as np, sys
exec(open('dbdata_lib.py').read())
def newton2(c3,T,e,a1,K1,it=50):
    z=np.array([c3,T],dtype=complex)
    for k in range(it):
        y=shoot2(z[0],z[1],e)
        if y is None: return None
        F=np.array([y[0]-a1,y[1]-K1])
        if np.max(np.abs(F))<1e-10: return z,y
        h=1e-6; J=np.zeros((2,2),dtype=complex)
        for j in range(2):
            zp=z.copy(); zp[j]+=h; yp=shoot2(zp[0],zp[1],e)
            if yp is None: return None
            J[:,j]=(np.array([yp[0]-a1,yp[1]-K1])-F)/h
        try: dz=np.linalg.solve(J,F)
        except np.linalg.LinAlgError: return None
        m=np.max(np.abs(dz))
        if m>0.3: dz=dz*0.3/m
        z=z-dz
    return None
e=1.0; a1=3.0; K1=-1j*np.sqrt(8.0)
sols=[]
c3grid=(-1.0,-0.8,-0.6,-0.45,-0.3,-0.1,0.02,0.05,0.1,0.2,0.3,0.5,0.7,1.0,1.5,2.0,3.0)
Tgrid=(0.3+0.3j,0.5+0.5j,0.7+0.7j,1.0+0.5j,1.0+1.0j,1.0-0.5j,1.0-1.0j,1.5+0.5j,1.5-0.5j,2.0+0.8j,2.0-0.8j,0.5-0.5j,2.5+0.5j,np.pi/2+1.76j,0.3-0.3j)
for c30 in c3grid:
    for T0 in Tgrid:
        r=newton2(c30,T0,e,a1,K1)
        if r is None: continue
        z,y=r
        if all(abs(z[0]-s[0])>1e-5 or abs(z[1]-s[1])>1e-5 for s in sols):
            sols.append((z[0],z[1],y[4]))
            print(f"NEW saddle from start c3={c30:+.2f},T={T0:.2f}: c3={z[0]:.6f}  T={z[1]:.6f}  I/a={y[4]:.5f}  R(T)={Rf(y[0],y[1],y[2]):.4f}  a'(T)={y[1]:.5f}",flush=True)
print("distinct saddles at dS data:",len(sols))
for s in sols: print(f"  c3={s[0]:.6f} T={s[1]:.6f} Re I/a={s[2].real:+.4f} Im I/a={s[2].imag:+.4f}")
