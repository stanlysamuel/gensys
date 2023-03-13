exists([C],aux0(A,B,C)):-init(A,B).
inv0(A,B,C):-aux0(A,B,C).
aux1(A,B,C),exists([A,B,C],(next(A,B,A,B),C=C,inv0(A,B,C),rank0(A,B,C,A,B,C))):-inv0(A,B,C),\+aux2(A,B,C).
dwf(rank0).
p1(A,B,C):-aux1(A,B,C).
p2(A,B,C):-aux2(A,B,C).
