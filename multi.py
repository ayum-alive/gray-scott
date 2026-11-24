import numpy as np
n=200
rng=np.random.default_rng(7)
U=np.ones((n,n));V=np.zeros((n,n))
for _ in range(10):
    x,y=rng.integers(20,n-20,2);U[y-4:y+4,x-4:x+4]=.5;V[y-4:y+4,x-4:x+4]=.25
# F,k vary across the plane: spots left -> labyrinth right
F=np.tile(np.linspace(.022,.04,n),(n,1));K=np.tile(np.linspace(.051,.066,n)[::-1]*0+np.linspace(.051,.066,n),(n,1))
K=np.repeat(np.linspace(.056,.066,n)[:,None],n,1)
L=lambda A:np.roll(A,1,0)+np.roll(A,-1,0)+np.roll(A,1,1)+np.roll(A,-1,1)-4*A
for _ in range(9000):
    r=U*V*V;U+=.16*L(U)-r+F*(1-U);V+=.08*L(V)+r-(F+K)*V
g=np.clip(V/V.max(),0,1)
rgb=np.stack([g*230+20,g*120+15,g*80+40],-1).astype(np.uint8)
open('m.ppm','wb').write(b'P6 %d %d 255\n'%(n,n)+rgb.tobytes())
