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
*/
init(N,R,T,PC) := PC=1.
step(N,R,T,PC,Np,Rp,Tp,PCp) :=
	PC=1, N>100, Np=N, Rp=R, Tp=T, PCp=2;
	PC=2, Np=N, Rp=N-10, Tp=T, PCp=5;
	PC=1, \+(N>100), Np=N, Rp=R, Tp=T, PCp=3.
call(N,R,T,PC,Np,Rp,Tp,PCp) :=
        (   PC=3, Np=N+11
	;   PC=4, Np=T
	), PCp=1.
ret(N,R,T,PC,Npp,Rpp,Tpp,PCpp,Np,Rp,Tp,PCp) :=
	PC=5,
	(   PCpp=3, Np=Npp, Rp=Rpp, Tp=R, PCp=4
	;   PCpp=4, Np=Npp, Rp=R, Tp=Tpp, PCp=5
	).
safe(N,R,T,PC,Np,Rp,Tp,PCp) :=
	(PCp=5 -> (N>100 -> Rp=N-10; Rp=91)).

safe91(N,R,T,PC,Np,Rp,Tp,PCp) :=
	(PCp=5, N=<100 -> Rp=91).

query_naming(summ(n,r,t,pc,'n\'','r\'','t\'','pc\'')).
summ(N,R,T,PC,N,R,T,PC) :- init(N,R,T,PC).
% summ(N0,R0,T0,PC0,N2,R2,T2,PC2) :-
% 	summ(N0,R0,T0,PC0,N1,R1,T1,PC1),
%  	step(N1,R1,T1,PC1,N2,R2,T2,PC2).
exists([PC2], summ(N0,R0,T0,PC0,N2,R2,T2,PC2)) :-
	id(step1),
	summ(N0,R0,T0,PC0,N1,R1,T1,PC1),
	PC1=1, N2=N1, R2=R1, T2=T1.
% s3(B,C,D,E,F,G,H,I,J,K,L,A) for (exists [A]: summ(B,C,D,E,F,G,H,A)) :- summ(B,C,D,E,I,J,K,L),L=1,F=I,G=J,H=K.
query_naming(sstep1(_,_,_,_,_,_,_,n,r,t,pc,'pc\'')).
skolem_template(sstep1, [_,_,_,_,_,_,_,N1,R1,T1,PC1,PC2], true,	true, 
    		(   N1>=Unk1+1, PC2=2
		;   N1=<Unk1, PC2=3
		), true).
% summ(N0,R0,T0,PC0,N2,R2,T2,PC2) :-
% 	summ(N0,R0,T0,PC0,N1,R1,T1,PC1),
% 	PC1=2, N2=N1, R2=N1-10, T2=T1, PC2=5.
exists([R2], summ(N0,R0,T0,PC0,N2,R2,T2,PC2)) :-
	id(step2),
	summ(N0,R0,T0,PC0,N1,R1,T1,PC1),
	PC1=2, N2=N1, T2=T1, PC2=5.
% sstep2(B,C,D,E,F,G,H,I,J,K,L,A) for (exists [A]: summ(B,C,D,E,F,A,G,H)) :- summ(B,C,D,E,I,J,K,L),L=2,F=I,G=K,H=5.
query_naming(sstep2(_,_,_,_,_,_,_,n,r,t,pc,'r\'')).
skolem_template(sstep2, [_,_,_,_,_,_,_,N1,R1,T1,PC1,R2], true,	true,
		R2=N1-Unk2, true).

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
	summ(N0,R0,T0,PC0,N1,R1,T1,PC1),
	call(N1,R1,T1,PC1,N2,R2,T2,PC2).
wf(descent/8).

