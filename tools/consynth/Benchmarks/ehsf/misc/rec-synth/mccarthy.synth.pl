h1(A,B,C,A,B,C) :- true. % s_main
h2(A,B,C,D,A,B,C,D) :- A=E, h1(F,G,H,E,I,J). % main_23
h4(A,B,C,D,E,F) :- F=G, H=D, h1(A,B,C,D,E,I), h3(H,J,K,L,M,N,O,G). % extra(main_23)
h6(A,B,C,D,E,F) :- E=F, h4(A,B,C,D,G,F). % extra(main_24)
h7(A,B,C,D,E,F) :- h6(A,B,C,D,E,F). % extra(main_25)
h8(A,B,C,D,E,F) :- D=<101, h7(A,B,C,D,E,F). % extra(main_30)
h9(A,B,C,D,E,F) :- h8(A,B,C,D,E,F). % extra(main_26)
h10(A,B,C,D,E,F) :- D>=102, h7(A,B,C,D,E,F). % extra(main_31)
h11(A,B,C,D,E,F) :- h10(A,B,C,D,E,F). % extra(main_28)
h12(A,B,C,D,E,F) :- E=92+G, G=\=0, h9(A,B,C,D,E,F). % extra(main_32)
false :- h12(A,B,C,D,E,F). % main_27
h13(A,B,C,D,E,F) :- E=92, h9(A,B,C,D,E,F). % extra(main_33)
h11(A,B,C,D,E,F) :- h13(A,B,C,D,E,F). % extra(main_28)
h14(A,B,C,D,E,F) :- h11(A,B,C,D,E,F). % extra(e_main)
h15(A,B,C,D,E,F,G,H) :- h2(A,B,C,D,E,F,G,H). % extra(mccarthy_29)
h16(A,B,C,D,E,F,G,H) :- /*E>=101*/E>=Const+1, sgrd(_,_,_,_,E,_,_,_,Const), h15(A,B,C,D,E,F,G,H). % extra(mccarthy_38)
h17(A,B,C,D,E,F,G,H) :- /*H= -10+E*/ sret(_,_,_,_,E,_,_,_,H), h16(A,B,C,D,E,F,G,I). % extra(mccarthy_30)
h18(A,B,C,D,E,F,G,H) :- /*E=<100*/E=<Const, sgrd(_,_,_,_,E,_,_,_,Const), h15(A,B,C,D,E,F,G,H). % extra(mccarthy_39)
h2(A,B,C,D,A,B,C,D) :- /*A=E+11*/scall(_,_,_,_,E,_,_,_,A), h18(F,G,H,I,E,J,K,L). % mccarthy_32
h19(A,B,C,D,E,F,G,H) :- F=I, /*J=11+E*/scall(_,_,_,_,E,_,_,_,J), h18(A,B,C,D,E,K,G,H), h3(J,L,M,N,O,P,Q,I). % extra(mccarthy_32)
h20(A,B,C,D,E,F,G,H) :- h17(A,B,C,D,E,F,G,H). % extra(mccarthy_31)
h21(A,B,C,D,E,F,G,H) :- h20(A,B,C,D,E,F,G,H). % extra(mccarthy_36)
h2(A,B,C,D,A,B,C,D) :- A=E, h19(F,G,H,I,J,E,K,L). % mccarthy_33
h23(A,B,C,D,E,F,G,H) :- G=I, J=F, h19(A,B,C,D,E,F,K,H), h3(J,L,M,N,O,P,Q,I). % extra(mccarthy_33)
h25(A,B,C,D,E,F,G,H) :- H=G, h23(A,B,C,D,E,F,G,I). % extra(mccarthy_34)
h26(A,B,C,D,E,F,G,H) :- h25(A,B,C,D,E,F,G,H). % extra(mccarthy_35)
h21(A,B,C,D,E,F,G,H) :- h26(A,B,C,D,E,F,G,H). % extra(mccarthy_36)
h3(A,B,C,D,E,F,G,H) :- h21(A,B,C,D,E,F,G,H). % extra(e_mccarthy)

exists([Exp], qgrd(E, Exp)) :- id(grd), h15(_,_,_,_,E,_,_,_).
skolem_template(sgrd, [_,_,_,_,E,_,_,_, Exp], true, true, Exp=Delta, (100=<Delta, Delta=< 101)).

exists([Exp], qret(E, Exp)) :- id(ret), h16(_,_,_,_,E,_,_,_).
skolem_template(sret, [_,_,_,_,E,_,_,_, Exp], true, true, Exp=E+Delta, (-11=<Delta, Delta=< -11)).

exists([Exp], qcall(E, Exp)) :- id(call), h18(_,_,_,_,E,_,_,_).
skolem_template(scall, [_,_,_,_,E,_,_,_, Exp], true, true, Exp=E+Delta, Delta= 11). % (10=<Delta, Delta=< 15)).


descent(F,A) :-
	/*A=E+11*/ scall(_,_,_,_,E,_,_,_,A), h18(F,G,H,I,E,J,K,L);
	A=E, h19(F,G,H,I,J,E,K,L).
wf(descent/2).