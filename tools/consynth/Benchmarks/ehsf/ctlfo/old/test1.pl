inv(X):=X=0.
exists([Y],q1(Y)):-id(1),inv(X).
aux(Y):-s1(X,Y),inv(X).
skolem_template(s1, [X,Y],
    		true,
		(B=<0;B>=1),
		(
  		 B=<0,Y=0;
  		 B>=1,Y=1
  		),
    		(B=0;B=1)
    	       ).
Y=1:-aux(Y).
