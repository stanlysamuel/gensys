# Rules for a translator :Gensys-LTL to Raboniel

# (pc1 == 1) to (eq pc1 i1())
# (pc1 == 2) to (eq pc1 i2())
# (pc2 == 3) to (eq pc2 i3())
# And(pc1 == 4, pc2 == 4) to (eq pc1 i4() && eq pc2 i4())
# Or(pc1 == 4, pc2 == 4) to (eq pc1 i4() || eq pc2 i4())
# Not(And(pc1 == 4, pc2 == 4)) to ! (eq pc1 i4() && eq pc2 i4())
# pc2_ == 4 to [pc2 <- i4()]
# pc2_ == 10 to [pc2 <- i10()]
# pc2_ == pc2 to [pc2 <- pc2]
# And(pc1 == 4, pc2_ == 4) to (eq pc1 i4() -> [pc2 <- i4()])

# And(pc1==1, f1a_==1,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==2,pc2_==pc2) TO
# eq pc i1() -> ([f1a <- i2()] && [f1b <- f1b] && [t1b <- t1b] && [f2a <- f2a] && [f2b <- f2b] && [t2b <- t2b] && [pc1 <- i2()] && [pc2 <- pc2]);
                
# And(pc1 == 2, f1a_==f1a,f1b_==f1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==3,pc2_==pc2) TO
# eq pc1 i2() -> ([f1a <- f1a] && [f1b <- f1b] && [f2a <- f2a] && [f2b <- f2b] && [t2b <- t2b] && [pc1 <- i3()] && [pc2 <- pc2]);
                

# And(pc1 == 3, f1b==1,t1b==1,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==3,pc2_==pc2), TO
# (eq pc1 i3() && eq f1b i1() && eq t1b i1()) -> ([f1a <- f1a] && [f1b <- f1b] && [t1b <- t1b] && [f2a <- f2a] && [f2b <- f2b] && [t2b <- t2b] && [pc1 <- i3()] && [pc2 <- pc2]);
                
# And(pc1 == 3, Or(f1b==0, t1b==0),f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==4,pc2_==pc2), TO
# (eq pc1 i3() && (eq f1b i0() || eq t1b i0())) -> ([f1a <- f1a] && [f1b <- f1b] && [t1b <- t1b] && [f2a <- f2a] && [f2b <- f2b] && [t2b <- t2b] && [pc1 <- i4()] && [pc2 <- pc2]);
                
# And(pc1 == 4, f1a_==0,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==5,pc2_==pc2), TO
# eq pc1 i4() -> ([f1a <- i0()] && [f1b <- f1b] && [t1b <- t1b] && [f2a <- f2a] && [f2b <- f2b] && [t2b <- t2b] && [pc1 <- i5()] && [pc2 <- pc2]);
                
# And(pc1 == 5, t1b==1,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==1,  f2b_==f2b,t2b_==t2b,pc1_==6,pc2_==pc2), TO
# (eq pc1 i5() && eq t1b i1()) -> ([f1a <- f1a] && [f1b <- f1b] && [t1b <- t1b] && [f2a <- i1()] && [f2b <- f2b] && [t2b <- t2b] && [pc1 <- i6()] && [pc2 <- pc2]);
                
# And(pc1 == 5, t1b==1,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==9,pc2_==pc2), TO
# (eq pc1 i5() && eq t1b i1()) -> ([f1a <- f1a] && [f1b <- f1b] && [t1b <- t1b] && [f2a <- f2a] && [f2b <- f2b] && [t2b <- t2b] && [pc1 <- i9()] && [pc2 <- pc2]);
                
# And(pc1 == 6, t1b==1,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,  f2b_==f2b,t2b_==1,  pc1_==7,pc2_==pc2), TO
# (eq pc1 i6() && eq t1b i1()) -> ([f1a <- f1a] && [f1b <- f1b] && [t1b <- t1b] && [f2a <- f2a] && [f2b <- f2b] && [t2b <- i1()] && [pc1 <- i7()] && [pc2 <- pc2]);

# And(pc1 == 7, f2b==1,t2b==1,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==8,pc2_==pc2), TO
# (eq pc1 i7() && eq f2b i1() && eq t2b i1()) -> ([f1a <- f1a] && [f1b <- f1b] && [t1b <- t1b] && [f2a <- f2a] && [f2b <- f2b] && [t2b <- t2b] && [pc1 <- i8()] && [pc2 <- pc2]);

# And(pc1 == 8, f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==0,  f2b_==f2b,t2b_==t2b,pc1_==9,pc2_==pc2), TO
# eq pc1 i8() -> ([f1a <- f1a] && [f1b <- f1b] && [t1b <- t1b] && [f2a <- i0()] && [f2b <- f2b] && [t2b <- t2b] && [pc1 <- i9()] && [pc2 <- pc2]);
                
# And(pc1 == 9, f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==1,pc2_==pc2), TO
# eq pc1 i9() -> ([f1a <- f1a] && [f1b <- f1b] && [t1b <- t1b] && [f2a <- f2a] && [f2b <- f2b] && [t2b <- t2b] && [pc1 <- i1()] && [pc2 <- pc2]);
                
# And(f1a == 1, f1a_ == 0, f1b_ == f1b, t1b == t1b_, f2a == f2a_, f2b == f2b_, t2b == t2b_, pc1 == pc1_, pc2 == pc2_), TO
# eq f1a i1() -> ([f1a <- i0()] && [f1b <- f1b] && [t1b <- t1b] && [f2a <- f2a] && [f2b <- f2b] && [t2b <- t2b] && [pc1 <- pc1] && [pc2 <- pc2]);

# And(pc2==1,f1a_==f1a,f1b_==1,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==2), TO
# eq pc2 i1() -> ([f1a <- f1a] && [f1b <- i1()] && [t1b <- t1b] && [f2a <- f2a] && [f2b <- f2b] && [t2b <- t2b] && [pc1 <- pc1] && [pc2 <- i2()]);
                
# And(pc2==2,f1a_==f1a,f1b_==f1b,t1b_==0,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==3), TO
# eq pc2 i2() -> ([f1a <- f1a] && [f1b <- f1b] && [t1b <- i0()] && [f2a <- f2a] && [f2b <- f2b] && [t2b <- t2b] && [pc1 <- pc1] && [pc2 <- i3()]);
                
# And(pc2==3,f1a==1,t1b==0,  f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==3), TO
# (eq pc2 i3() && eq f1a i1() && eq t1b i0()) -> ([f1a <- f1a] && [f1b <- f1b] && [t1b <- t1b] && [f2a <- f2a] && [f2b <- f2b] && [t2b <- t2b] && [pc1 <- pc1] && [pc2 <- i3()]);
                
# And(pc2==3,Or(f1a==0,t1b==1),f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==4), TO
# (eq pc2 i3() && (eq f1a i0() || eq t1b i1())) -> ([f1a <- f1a] && [f1b <- f1b] && [t1b <- t1b] && [f2a <- f2a] && [f2b <- f2b] && [t2b <- t2b] && [pc1 <- pc1] && [pc2 <- i4()]);
                
# And(pc2==4,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==1,t2b_==t2b,pc1_==pc1,pc2_==5), TO
# eq pc2 i4() -> ([f1a <- f1a] && [f1b <- f1b] && [t1b <- t1b] && [f2a <- f2a] && [f2b <- i1()] && [t2b <- t2b] && [pc1 <- pc1] && [pc2 <- i5()]);
                
# And(pc2==5,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==0,pc1_==pc1,pc2_==6), TO
# eq pc2 i5() -> ([f1a <- f1a] && [f1b <- f1b] && [t1b <- t1b] && [f2a <- f2a] && [f2b <- f2b] && [t2b <- i0()] && [pc1 <- pc1] && [pc2 <- i6()]);

# And(pc2==6,f2a==1,t2b==0,  f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==6), TO
# (eq pc2 i6() && eq f2a i1() && eq t2b i0()) -> ([f1a <- f1a] && [f1b <- f1b] && [t1b <- t1b] && [f2a <- f2a] && [f2b <- f2b] && [t2b <- t2b] && [pc1 <- pc1] && [pc2 <- i6()]);
                
# And(pc2==6,Or(f2a==0,t2b==1),f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==7), TO
# (eq pc2 i6() && (eq f2a i0() || eq t2b i1())) -> ([f1a <- f1a] && [f1b <- f1b] && [t1b <- t1b] && [f2a <- f2a] && [f2b <- f2b] && [t2b <- t2b] && [pc1 <- pc1] && [pc2 <- i7()]);
                
# And(pc2==7,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==0,t2b_==t2b,pc1_==pc1,pc2_==8), TO
# eq pc2 i7() -> ([f1a <- f1a] && [f1b <- f1b] && [t1b <- t1b] && [f2a <- f2a] && [f2b <- i0()] && [t2b <- t2b] && [pc1 <- pc1] && [pc2 <- i8()]);
                
# And(pc2==8,f1a_==f1a,f1b_==0,t1b_==t1b,f2a_==f2a,f2b_==f1b,t2b_==t2b,pc1_==pc1,pc2_==9), TO
# eq pc2 i8() -> ([f1a <- f1a] && [f1b <- i0()] && [t1b <- t1b] && [f2a <- f2a] && [f2b <- f1b] && [t2b <- t2b] && [pc1 <- pc1] && [pc2 <- i9()]);

# And(pc2==9,f1a_==f1a,f1b_==f1b,t1b_==t1b,f2a_==f2a,f2b_==f2b,t2b_==t2b,pc1_==pc1,pc2_==1), TO
# eq pc2 i9() -> ([f1a <- f1a] && [f1b <- f1b] && [t1b <- t1b] && [f2a <- f2a] && [f2b <- f2b] && [t2b <- t2b] && [pc1 <- pc1] && [pc2 <- i1()]);
                
# And(f1a == f1a_, f1b_ == f1b, t1b == t1b_, f2a == f2a_, f2b == f2b_, t2b == t2b_, pc1 == pc1_, pc2 == pc2_), TO
# ([f1a <- f1a] && [f1b <- f1b] && [t1b <- t1b] && [f2a <- f2a] && [f2b <- f2b] && [t2b <- t2b] && [pc1 <- pc1] && [pc2 <- pc2]);

# And(pc1 == 1, pc1_ == 2, x_ == x + z, y1_ == y1, y2_ == y2, z_ == z, pc2_ == pc2, pc3_ == pc3), TO
# eq pc1 i1() -> ([x <- x + z] && [y1 <- y1] && [y2 <- y2] && [z <- z] && [pc1 <- i2()] && [pc2 <- pc2] && [pc3 <- pc3]);
                
# And(pc1 == 2, pc1_ == 3, x_ == x + z, y1_ == y1, y2_ == y2, z_ == z, pc2_ == pc2, pc3_ == pc3),
# eq pc1 i2() -> ([x <- x + z] && [y1 <- y1] && [y2 <- y2] && [z <- z] && [pc1 <- i3()] && [pc2 <- pc2] && [pc3 <- pc3]);
                
# And(Or(pc1<=0, pc1>=3), pc1_ == pc1, x_ == x, y1_ == y1, y2_ == y2, z_ == z, pc2_ == pc2, pc3_ == pc3), TO
# (leq pc1 i0() || geq pc1 i3()) -> ([x <- x] && [y1 <- y1] && [y2 <- y2] && [z <- z] && [pc1 <- pc1] && [pc2 <- pc2] && [pc3 <- pc3]);
                
# And(pc2 == 1, pc2_ == 2, z_ == z + 1, y1_ == y1, y2_ == y2, x_ == x, pc1_ == pc1, pc3_ == pc3), TO
# eq pc2 i1() -> ([z <- z + i1()] && [y1 <- y1] && [y2 <- y2] && [x <- x] && [pc1 <- pc1] && [pc2 <- i2()] && [pc3 <- pc3]);

# And(pc2 == 2, pc2_ == 3, z_ == z + 1, y1_ == y1, y2_ == y2, x_ == x, pc1_ == pc1, pc3_ == pc3), TO
# eq pc2 i2() -> ([z <- z + i1()] && [y1 <- y1] && [y2 <- y2] && [x <- x] && [pc1 <- pc1] && [pc2 <- i3()] && [pc3 <- pc3]);
                
# And(Or(pc2<=0, pc2>=3), pc2_ == pc2, x_ == x, y1_ == y1, y2_ == y2, z_ == z, pc1_ == pc1, pc3_ == pc3), TO
# (leq pc2 i0() || geq pc2 i3()) -> ([x <- x] && [y1 <- y1] && [y2 <- y2] && [z <- z] && [pc1 <- pc1] && [pc2 <- pc2] && [pc3 <- pc3]);
                
# And(pc3 == 1, pc3_ == 2, x == 1, y1_ == 3, y2_ == y2, x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1), TO
# (eq pc3 i1() && eq x i1()) -> ([y1 <- i3()] && [y2 <- y2] && [z <- z] && [pc2 <- pc2] && [pc1 <- pc1] && [pc3 <- i2()]);
                
# And(pc3 == 1, pc3_ == 2, x == 2, y1_ == 6, y2_ == y2, x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1), TO
# (eq pc3 i1() && eq x i2()) -> ([y1 <- i6()] && [y2 <- y2] && [x <- x] && [z <- z] && [pc2 <- pc2] && [pc1 <- pc1] && [pc3 <- i2()]);
                
# And(pc3 == 1, pc3_ == 2, Or(x<=0, x>=3), y1_ == 5, y2_ == y2, x_ == x, z_ == z, pc2_ == pc2, pc1_ == pc1), TO
# (eq pc3 i1() && (leq x i0() || geq x i3())) -> ([y1 <- i5()] && [y2 <- y2] && [x <- x] && [z <- z] && [pc2 <- pc2] && [pc1 <- pc1] && [pc3 <- i2()]);
                
# And(pc3 == 2, pc3_ == 3, y2_ == x, x_ == x, y1_ == y1, z_ == z, pc2_ == pc2, pc1_ == pc1), TO
# eq pc3 i2() -> ([y2 <- x] && [x <- x] && [y1 <- y1] && [z <- z] && [pc2 <- pc2] && [pc1 <- pc1] && [pc3 <- i3()]);
                
# And(pc3 == 3, pc3_ == 4, y1 != y2, x_ == x, y1_ == y1, y2_ == y2, z_ == z, pc2_ == pc2, pc1_ == pc1), TO
# (eq pc3 i3() && ! (eq y1 y2)) -> ([x <- x] && [y1 <- y1] && [y2 <- y2] && [z <- z] && [pc2 <- pc2] && [pc1 <- pc1] && [pc3 <- i4()]);
                
# And(Or(pc3<=0, pc3>=4), pc3_ == pc3, x_ == x, y1_ == y1, y2_ == y2, z_ == z, pc2_ == pc2, pc1_ == pc1), TO
# (leq pc3 i0() || geq pc3 i4()) -> ([x <- x] && [y1 <- y1] && [y2 <- y2] && [z <- z] && [pc2 <- pc2] && [pc1 <- pc1] && [pc3 <- pc3]);