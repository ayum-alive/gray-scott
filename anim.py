import numpy as np,subprocess
n=160
rng=np.random.default_rng(3)
U=np.ones((n,n));V=np.zeros((n,n))
U[70:90,70:90]=.5;V[70:90,70:90]=.25
V+=rng.random((n,n))*.02
F,k=.0367,.0649
L=lambda A:np.roll(A,1,0)+np.roll(A,-1,0)+np.roll(A,1,1)+np.roll(A,-1,1)-4*A
p=subprocess.Popen('ffmpeg -y -loglevel error -f rawvideo -pix_fmt rgb24 -s 160x160 -r 24 -i - -vf scale=480:480:flags=neighbor -pix_fmt yuv420p mitosis.mp4'.split(),stdin=subprocess.PIPE)
for f in range(240):
    for _ in range(25):
        r=U*V*V;U+=.16*L(U)-r+F*(1-U);V+=.08*L(V)+r-(F+k)*V
    g=np.clip(V/.4,0,1);img=np.stack([g*255*.9+20,g*200+20,g*120+40],-1).astype(np.uint8)
    p.stdin.write(img.tobytes())
p.stdin.close();p.wait()
