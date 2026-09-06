# Wider-|T| search at the dS data (a1=3, K1=-i sqrt8): does Re I over the complex saddle set grow without bound?
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
c3grid=(-0.3+0.1j,-0.1-0.1j,0.0+0.05j,0.05-0.05j,-0.05+0.15j,0.02+0.02j)
Tgrid=(3.0-10j,-3.0-10j,3.0+6j,1.0+9j,-2.0+5j,6.0-12j,-6.0-12j,2.0-14j,8.0+4j,-8.0+8j,4.0-4j,-4.0+4j)
for c30 in c3grid:
    for T0 in Tgrid:
        r=newton2(c30,T0,e,a1,K1)
        if r is None: continue
        z,y=r
        if all(abs(z[0]-s[0])>1e-5 or abs(np.exp(1j*z[1])-np.exp(1j*s[1]))>1e-4 for s in sols):
            sols.append((z[0],z[1],y[4]))
            print(f"NEW from c3={c30:.2f},T={T0:.1f}: c3={z[0]:.6f}  T={z[1]:.6f}  I/a={y[4]:.5f}  R(T)={Rf(y[0],y[1],y[2]):.4f}",flush=True)
print("distinct saddles:",len(sols))
re=[s[2].real for s in sols]
if re: print(f"Re I/a range over found saddles: [{min(re):+.3f}, {max(re):+.3f}]")
