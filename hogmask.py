import numpy as np
n=240
yy,xx=np.mgrid[0:n,0:n]
body=((xx-110)/90.)**2+((yy-140)/55.)**2<1
head=((xx-205)/32.)**2+((yy-150)/22.)**2<1
mask=(body|head)
rng=np.random.default_rng(2)
U=np.ones((n,n));V=np.zeros((n,n))
for _ in range(25):
    x,y=rng.integers(30,210,2);U[y-3:y+3,x-3:x+3]=.5;V[y-3:y+3,x-3:x+3]=.25
F,k=.029,.057
L=lambda A:np.roll(A,1,0)+np.roll(A,-1,0)+np.roll(A,1,1)+np.roll(A,-1,1)-4*A
for _ in range(7000):
    r=U*V*V;U+=.16*L(U)-r+F*(1-U);V+=.08*L(V)+r-(F+k)*V
    V[~mask]=0;U[~mask]=1
g=np.clip(V/V.max(),0,1)
img=np.where(mask[...,None],np.stack([g*200+50,g*150+35,g*90+20],-1),[20,20,42]).astype(np.uint8)
open('h.ppm','wb').write(b'P6 %d %d 255\n'%(n,n)+img.tobytes())
