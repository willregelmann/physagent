import numpy as np
exec(open('dbdata_lib.py').read())
def newton2(c3,T,e,a1,K1,it=40):
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
e=1.0; a1=0.5585; K1=0.0; sols=[]
for c30 in (-0.36,-0.33,-0.25,-1/6,-0.05,0.05,-0.45):
    for T0 in (2.1,2.1+0.5j,2.1-0.5j,0.6,0.6+0.8j,1.2+1.2j,2.8+0.3j,1.5-1.0j):
        r=newton2(c30,T0,e,a1,K1)
        if r is None: continue
        z,y=r
        if all(abs(z[0]-s[0])>1e-5 or abs(z[1]-s[1])>1e-5 for s in sols):
            sols.append((z[0],z[1],y[4])); print(f"  c3={z[0]:.6f}  T={z[1]:.6f}  I/a={y[4]:.5f}  R(T)={Rf(y[0],y[1],y[2]):.4f}",flush=True)
print("distinct saddles at the double-bubble data:",len(sols))
