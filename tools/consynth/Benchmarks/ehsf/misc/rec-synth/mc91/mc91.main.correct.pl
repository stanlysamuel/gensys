/*
    int mccarthy(int n) {      
      int t, r;
1:    if (n > Unk1) {
2:      r = n-Unk2;
      } else {
3:      t = mccarthy(n+Unk3);
4:      r = mccarthy(t);
      }
5:    return r;	    
    }

    void main(void) {
      int n, r;
11:   r = mc(n);
12:   assert( n=<100 && r==91 || n>=101 && r==n-10);	  
    }
*/
init(N,R,T,PC) :- PC=11.
step(N,R,T,PC,Np,Rp,Tp,PCp) :-
	PC=1, N>100, Np=N, Rp=R, Tp=T, PCp=2;
	PC=2, Np=N, Rp=N-10, Tp=T, PCp=5;
	PC=1, \+(N>100), Np=N, Rp=R, Tp=T, PCp=3.
call(N,R,T,PC,Np,Rp,Tp,PCp) :-
	PC=3, Np=N+11, PCp=1;
	PC=4, Np=T, PCp=1;
	PC=11, Np=N, PCp=1.
ret(N,R,T,PC,Npp,Rpp,Tpp,PCpp,Np,Rp,Tp,PCp) :=
	PC=5, PCpp=3, Np=Npp, Rp=Rpp, Tp=R, PCp=4;
	PC=5, PCpp=4, Np=Npp, Rp=R, Tp=Tpp, PCp=5;
	PC=5, PCpp=11, Np=Npp, Rp=R, Tp=Tpp, PCp=12.
safe(N,R,T,PC,Np,Rp,Tp,PCp) :=
	(PCp=12 -> (N>100 -> Rp=N-10; Rp=91)).

query_naming(summ(n,r,t,pc,'n\'','r\'','t\'','pc\'')).
summ(N,R,T,PC,N,R,T,PC) :- init(N,R,T,PC).
summ(N0,R0,T0,PC0,N2,R2,T2,PC2) :-
	summ(N0,R0,T0,PC0,N1,R1,T1,PC1),
	step(N1,R1,T1,PC1,N2,R2,T2,PC2).
summ(N2,R2,T2,PC2,N2,R2,T2,PC2) :-
	summ(N0,R0,T0,PC0,N1,R1,T1,PC1),
	call(N1,R1,T1,PC1,N2,R2,T2,PC2).
summ(N0,R0,T0,PC0,N4,R4,T4,PC4) :-
	summ(N0,R0,T0,PC0,N1,R1,T1,PC1),
	call(N1,R1,T1,PC1,N2,R2,T2,PC2),
	summ(N2,R2,T2,PC2,N3,R3,T3,PC3),
	ret(N3,R3,T3,PC3,N1,R1,T1,PC1,N4,R4,T4,PC4).
safe(N0,R0,T0,PC0,N1,R1,T1,PC1) :- summ(N0,R0,T0,PC0,N1,R1,T1,PC1).

query_naming(descent(n,r,t,pc,'n\'','r\'','t\'','pc\'')).
query_naming(descent_p(n,r,t,pc,'n\'','r\'','t\'','pc\'')).
descent(N0,R0,T0,PC0,N2,R2,T2,PC2) :-
	PC0=1,
	summ(N0,R0,T0,PC0,N1,R1,T1,PC1),
	call(N1,R1,T1,PC1,N2,R2,T2,PC2).
wf(descent/8).
