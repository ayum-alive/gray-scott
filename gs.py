import numpy as np
n=200
def run(F,k,steps=6000,seed=1):
    rng=np.random.default_rng(seed)
    U=np.ones((n,n));V=np.zeros((n,n))
    for _ in range(12):
        x,y=rng.integers(20,n-20,2);U[y-4:y+4,x-4:x+4]=.5;V[y-4:y+4,x-4:x+4]=.25
    L=lambda A:np.roll(A,1,0)+np.roll(A,-1,0)+np.roll(A,1,1)+np.roll(A,-1,1)-4*A
    for _ in range(steps):
        r=U*V*V
        U+=.16*L(U)-r+F*(1-U);V+=.08*L(V)+r-(F+k)*V
    return V
ps=[(.037,.060),(.029,.057),(.022,.051),(.055,.062)]
tiles=[run(*p) for p in ps]
img=np.hstack(tiles);img=(255*np.clip(img/max(img.max(),1e-6),0,1)).astype(np.uint8)
rgb=np.stack([img*0+20,img//2+30,img],-1).astype(np.uint8)
open('gs.ppm','wb').write(b'P6 %d %d 255\n'%(rgb.shape[1],rgb.shape[0])+rgb.tobytes())
