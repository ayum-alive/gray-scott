import numpy as np
from midiutil import MIDIFile
n=120;rng=np.random.default_rng(5)
U=np.ones((n,n));V=np.zeros((n,n));U[50:70,50:70]=.5;V[50:70,50:70]=.25;V+=rng.random((n,n))*.02
F,k=.0367,.0649
L=lambda A:np.roll(A,1,0)+np.roll(A,-1,0)+np.roll(A,1,1)+np.roll(A,-1,1)-4*A
m=MIDIFile(1);m.addTempo(0,0,120);m.addProgramChange(0,0,0,11)
sc=[0,2,4,7,9]
for s in range(64):
    for _ in range(40):
        r=U*V*V;U+=.16*L(U)-r+F*(1-U);V+=.08*L(V)+r-(F+k)*V
    cols=V[n//2,::24][:5]
    for i,c in enumerate(cols):
        if c>.03: m.addNote(0,0,60+sc[i]+12*(i%2),s*.5,1.5,int(50+c*150))
m.writeFile(open('gs.mid','wb'))
