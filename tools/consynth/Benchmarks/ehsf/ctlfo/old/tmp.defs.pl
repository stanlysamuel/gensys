init([A,R,N,PC]):-A=0,R=0,PC=1.
next([A,R,N,PC],[Ap,Rp,Np,PCp]):-
    PC=1,Ap=A,Rp=R,Np=N,PCp=5;
    PC=1,Ap=1,Rp=R,Np=N,PCp=2;
    PC=2,Ap=0,Rp=R,Np=N,PCp=3;
    PC=3,N>0,Ap=A,Rp=R,Np=N-1,PCp=3;
    PC=3,N=<0,Ap=A,Rp=1,Np=N,PCp=4;
    PC=4,Ap=A,Rp=0,Np=N,PCp=1.
p1([A,R,N,PC]):-A=1.
p2([A,R,N,PC]):-R=1.