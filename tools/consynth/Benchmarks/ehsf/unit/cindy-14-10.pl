/*
Stepmother v Cindrella Game:
 
There are 5 buckets arranged in a circle. 
Each bucket can hold upto b lit of water. 
Initially all buckets are empty. 
Each round of the game: 
stepmother brings 1 lit of additional water 
and splits it into 5 buckets. 
If any of the buckets overflow, stepmother wins. 
If not, cindrella empties two *adjacent* buckets. 
If game goes on forever, cindrella wins. 

Question: Find b* such that if b is below b*, 
stepmother wins, and if b is above b*, Cindrella wins 
(hopefully with an accompanying winning strategy/proof). 

Warmup: If b < 1.5 lit, stepmother wins 
(in first round, split 1 lit into two adjacent buckets, 
no matter what Cindrella does, there will be bucket 
with 0.5 lit, and stepmother can cause a spill 
in second round by adding 1 lit in that bucket). 
If b >= 3 lit, Cindrella wins 
(Cindrella can just go round robin emptying two 
buckets in each round, and this is winning no matter 
what stepmother does). 

Actual value of b* is thus somewhere between 1.5 and 3. 
The answer is known with a formal proof, but I am really 
curious if one of our techniques can find it 
(template-based techniques could work, for instance). 
Note that Cindrella's choice is discrete (she has 5 choices), 
but stepmother's choice is infinite: pick rational/real numbers 
c1, c2, c3, c4, c5 that add up to 1). 

Generalized puzzle: 
Now assume that there are n buckets,  each of which holds 
b lit, and in each round, stepmother uses c lit of additional 
water. 
Find b* as a function of n and c. 
As far as I know, the solution to the general case is not known 
(however, using computer aid, people have computed answers 
for some special cases).
*/
query_naming(init(b, b1, b2, b3, b4, b5)).
query_naming(overflow(b, b1, b2, b3, b4, b5)).
query_naming(inv(b, b1, b2, b3, b4, b5)).
query_naming(stepmother(b, b1, b2, b3, b4, b5, 'b\'', 'b1\'', 'b2\'', 'b3\'', 'b4\'', 'b5\'')).
query_naming(cinderella(b, b1, b2, b3, b4, b5, 'b\'', 'b1\'', 'b2\'', 'b3\'', 'b4\'', 'b5\'')).
query_naming(round(b, b1, b2, b3, b4, b5, 'b\'', 'b1\'', 'b2\'', 'b3\'', 'b4\'', 'b5\'')).
query_naming(round_p(b, b1, b2, b3, b4, b5, 'b\'', 'b1\'', 'b2\'', 'b3\'', 'b4\'', 'b5\'')).
query_naming(s5('_b', '_b1', '_b2', '_b3', '_b4', '_b5',
		b, b1, b2, b3, b4, b5, 'b\'', 'b1\'', 'b2\'', 'b3\'', 'b4\'', 'b5\'')).

init(B, B1, B2, B3, B4, B5) := B>=0, B1=0, B2=0, B3=0, B4=0, B5=0, B=14.
overflow(B, B1, B2, B3, B4, B5) := B1>B; B2>B; B3>B; B4>B; B5>B.
stepmother(B, B1, B2, B3, B4, B5, B, B1p, B2p, B3p, B4p, B5p) := B1p>=B1, B2p>=B2, B3p>=B3, B4p>=B4, B5p>=B5, B1p+B2p+B3p+B4p+B5p-B1-B2-B3-B4-B5=10.
cinderella(B, B1, B2, B3, B4, B5, B, B1p, B2p, B3p, B4p, B5p) :-
        B1p=0, B2p=0, B3p=B3, B4p=B4, B5p=B5;
	B1p=B1, B2p=0, B3p=0, B4p=B4, B5p=B5;
	B1p=B1, B2p=B2, B3p=0, B4p=0, B5p=B5;
	B1p=B1, B2p=B2, B3p=B3, B4p=0, B5p=0;
	B1p=0, B2p=B2, B3p=B3, B4p=B4, B5p=0.

% stepmother wins := EF overflow
inv(B, B1, B2, B3, B4, B5) :- init(B, B1, B2, B3, B4, B5).

exists([Bpp, B1pp, B2pp, B3pp, B4pp, B5pp],
       (
%	 stepmother(Bp, B1p, B2p, B3p, B4p, B5p, Bpp, B1pp, B2pp, B3pp, B4pp, B5pp),
	 inv(Bpp, B1pp, B2pp, B3pp, B4pp, B5pp),
	 round(B, B1, B2, B3, B4, B5, Bpp, B1pp, B2pp, B3pp, B4pp, B5pp)
       )
      ) :-		
	inv(B, B1, B2, B3, B4, B5), \+overflow(B, B1, B2, B3, B4, B5), 
	cinderella(B, B1, B2, B3, B4, B5, Bp, B1p, B2p, B3p, B4p, B5p).

wf(round/12).

skolem_template(s5, [_B, _B1, _B2, _B3, _B4, _B5,
		     B, B1, B2, B3, B4, B5,
		     Bp, B1p, B2p, B3p, B4p, B5p],
 		true,
		true,
 		(
		  B1p=B1+D1, B2p=B2+D2, B3p=B3+D3, B4p=B4+D4, B5p=B5+D5, Bp=B
 		),
		( D1>=0, D2>=0, D3>=0, D4>=0, D5>=0, D1+D2+D3+D4+D5=10 )
 	       ).
