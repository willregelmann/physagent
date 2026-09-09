# complex pair at (4,12): eps continuation 0.355 -> 1.00 in steps of 0.02 from lapse_path.py's eps=0.355 seed, path [1.185, tau1]
import numpy as np, sys
exec(open('stm_pair.py').read().split('print("=== (i)')[0])
x=np.array((-0.348717-0.807122j,2.52608+0.95325j),dtype=complex)
prev=None
for e in np.arange(0.355,1.0001,0.02):
    e=round(float(e),4)
    x,y,it=newton(x,4.0,12.0,e)
    if it<0: print(f"eps={e}: lost"); break
    Iinv,B,A,v,R,th=IaR(x[0],e,pathof(x[1]))
    print(f"eps={e:.3f}: c3={x[0]:.6f} tau1={x[1]:.5f} v={v:.4f} I_inv={Iinv:.4f} Re I_aR={Iinv.real+B.real:+.4f} sphere={-(1+2*e):+.4f} gap={Iinv.real+B.real+1+2*e:+.4f}",flush=True)
print("   reference eps=1 pair (invariant.out): c3=-0.885788-0.478724i tau1=2.73251+1.13928i, I_inv=-4.6439-10.9117i, Re I_aR=-4.394, gap=-1.394")
