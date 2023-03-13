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
exists([Unk1], unk1(Unk1)) :- id(unk1).
query_naming(sunk1(unk1)).
skolem_template(sunk1, [Unk1], true, true, Unk1=_100, true).

exists([Unk2], unk2(Unk2)) :- id(unk2).
query_naming(sunk2(unk2)).
skolem_template(sunk2, [Unk2], true, true, Unk2=_10, true).
/*
exists([Unk3], unk3(Unk3)) :- id(unk3).
query_naming(sunk3(unk3)).
skolem_template(sunk3, [Unk3], true, true, Unk3=_11, true).
*/

init_1(N,R,T) := true.
step_12(N,R,T,Np,Rp,Tp) :-
	unk1(Unk1),
	N>=Unk1+1, Np=N, Rp=R, Tp=T.
step_25(N,R,T,Np,Rp,Tp) :-
	unk2(Unk2),
	Np=N, Rp=N-Unk2, Tp=T.
step_13(N,R,T,Np,Rp,Tp) :-
	unk1(Unk1),
	N=<Unk1, Np=N, Rp=R, Tp=T.
call_31(N,R,T,Np,Rp,Tp) :=
	Np=N+11.
call_41(N,R,T,Np,Rp,Tp) :=
	Np=T.
ret_534(N,R,T,Npp,Rpp,Tpp,Np,Rp,Tp) :=
	Np=Npp, Rp=Rpp, Tp=R.
ret_545(N,R,T,Npp,Rpp,Tpp,Np,Rp,Tp) :-
	Np=Npp, Rp=R, Tp=Tpp.
safe_5(N,R,T,Np,Rp,Tp) :=
	(N>100 -> Rp=N-10; Rp=91).

query_naming(summ_11(n,r,t,'n\'','r\'','t\'')).
query_naming(summ_12(n,r,t,'n\'','r\'','t\'')).
query_naming(summ_13(n,r,t,'n\'','r\'','t\'')).
query_naming(summ_14(n,r,t,'n\'','r\'','t\'')).
query_naming(summ_15(n,r,t,'n\'','r\'','t\'')).
summ_11(N,R,T,N,R,T) :- init_1(N,R,T).
summ_12(N0,R0,T0,N2,R2,T2) :-
	summ_11(N0,R0,T0,N1,R1,T1),
	step_12(N1,R1,T1,N2,R2,T2).
summ_15(N0,R0,T0,N2,R2,T2) :-
	summ_12(N0,R0,T0,N1,R1,T1),
	step_25(N1,R1,T1,N2,R2,T2).
summ_13(N0,R0,T0,N2,R2,T2) :-
	summ_11(N0,R0,T0,N1,R1,T1),
	step_13(N1,R1,T1,N2,R2,T2).
summ_11(N2,R2,T2,N2,R2,T2) :-
	summ_13(N0,R0,T0,N1,R1,T1),
	call_31(N1,R1,T1,N2,R2,T2).
summ_11(N2,R2,T2,N2,R2,T2) :-
	summ_14(N0,R0,T0,N1,R1,T1),
	call_41(N1,R1,T1,N2,R2,T2).
summ_14(N0,R0,T0,N4,R4,T4) :-
	summ_13(N0,R0,T0,N1,R1,T1),
	call_31(N1,R1,T1,N2,R2,T2),
	summ_15(N2,R2,T2,N3,R3,T3),
	ret_534(N3,R3,T3,N1,R1,T1,N4,R4,T4).
summ_15(N0,R0,T0,N4,R4,T4) :-
	summ_14(N0,R0,T0,N1,R1,T1),
	call_41(N1,R1,T1,N2,R2,T2),
	summ_15(N2,R2,T2,N3,R3,T3),
	ret_545(N3,R3,T3,N1,R1,T1,N4,R4,T4).
safe_5(N0,R0,T0,N1,R1,T1) :- summ_15(N0,R0,T0,N1,R1,T1).

query_naming(descent(n,r,t,'n\'','r\'','t\'')).
query_naming(descent_p(n,r,t,'n\'','r\'','t\'')).
descent(N0,R0,T0,N2,R2,T2) :-
	summ_13(N0,R0,T0,N1,R1,T1),
	call_31(N1,R1,T1,N2,R2,T2).
descent(N0,R0,T0,N2,R2,T2) :-
	summ_14(N0,R0,T0,N1,R1,T1),
	call_41(N1,R1,T1,N2,R2,T2).
wf(descent/6).

