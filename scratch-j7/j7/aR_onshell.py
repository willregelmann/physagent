# On-shell fixed-(a,R) action of the real regular caps at a=2, evaluated at each cap's own R:  I_(a,R) = I_inv - eps*R*v  (a^2=4).
import re
for e,fn in ((1.0,'vfamily.out'),(0.3,'vfamily.out')):
    rows=[]
    for src in ('vfamily.out','vfine.out'):
        block=None
        for line in open(src):
            m=re.match(r"=== eps=([\d.]+)",line)
            if m: block=float(m.group(1)); continue
            if block!=e: continue
            m=re.match(r"c3=([+-][\d.]+) (\w+)\s+tau1=\s*([\d.]+) v=\s*([+-][\d.]+) R=\s*([+-][\d.]+) I_inv=\s*([+-][\d.]+)",line)
            if m:
                c3,side,t1,v,R,Ii=float(m.group(1)),m.group(2),float(m.group(3)),float(m.group(4)),float(m.group(5)),float(m.group(6))
                rows.append((v,c3,side,R,Ii,Ii-e*R*v))
    rows.sort()
    print(f"=== eps={e}: on-shell I_(a,R)(cap)=I_inv-eps*R*v along the real family at a=2 (sorted by v) ===")
    for v,c3,side,R,Ii,IaR in rows: print(f"  v={v:+8.4f} c3={c3:+.5f} {side:11s} R={R:+9.3f} I_inv={Ii:+10.3f}  I_(a,R)={IaR:+10.3f}")
    m=min(rows,key=lambda r:r[5]); print(f"  minimum: I_(a,R)={m[5]:+.4f} at v={m[0]:+.4f}, R={m[3]:+.3f} (c3={m[1]:+.5f}); ends: v={rows[0][0]:+.2f}->{rows[0][5]:+.1f}, v={rows[-1][0]:+.2f}->{rows[-1][5]:+.1f}")
