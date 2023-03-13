//version 1: 9
int keA; keR;
unsigned int pc;
int __phi() { return CAG(CIMP(CAP(keA==1),CAF(CAP(keR==1)))); }

void init() { keA = 0; keR = 0;}

int body() {
   keA = 1; keA = 0; keA = 1; keA = 0;
   __rho_2_ = nondet();
   k1 = __rho_2_;
   while (1) { 
     if (!(k1>0)) break;
       k1--;
   }
   keR = 1; keR = 0; keR = 1; keR = 0;
   keA = 1; keA = 0; keA = 1; keA = 0;
   __rho_6_ = nondet();
   k2 = __rho_6_;
   while (1) {
     if (!(k2>0)) break;
       k2--;
   }
   keR = 1; keR = 0; keR = 1; keR = 0;
   while (1) {
       keA = 1; keA = 0; keA = 1; keA = 0;
       __rho_10_ = nondet();
       k3 = __rho_10_;
       if (k3>0) {
           k3--;
           keR = 1; keR = 0; keR = 1; keR = 0;
       }
       else {
           keR = 1; keR = 0; keR = 1; keR = 0;
           break;
       }
   }
   __rho_11_ = nondet();
   k4 = __rho_11_;
   while (1) {
       keA = 1; keA = 0; keA = 1; keA = 0;
       if (k4>0) {
           k4--;
           keR = 1; keR = 0; keR = 1; keR = 0;
       }
       else {
           keR = 1; keR = 0; keR = 1; keR = 0;
           break;
       }
   }
   keA = 1; keA = 0; keA = 1; keA = 0;
   __rho_13_ = nondet();
   k5 = __rho_13_;
   while (1) {
     if (!(k5>0)) break;
       k5--;
   }
   keR = 1; keR = 0; keR = 1; keR = 0;

   while(1) { dummy=dummy; } L_return: return 0;
}


//version 2: 10, 11
int keA; keR;
unsigned int pc;
int __phi() { return CAG(CIMP(CAP(keA==1),CAF(CAP(keR==1)))); }

void init() { keA = 0; keR = 0;}

int body() {
   keA = 1; keA = 0; keA = 1; keA = 0;
   __rho_2_ = nondet();
   k1 = __rho_2_;
   while (1) { 
     if (!(k1>0)) break;
       k1--;
   }
   keR = 1; keR = 0; keR = 1; keR = 0;
   keA = 1; keA = 0; keA = 1; keA = 0;
   __rho_6_ = nondet();
   k2 = __rho_6_;
   while (1) {
     if (!(k2>0)) break;
       k2--;
   }
   keR = 1; keR = 0; keR = 1; keR = 0;
   while (1) {
       keA = 1; keA = 0; keA = 1; keA = 0;
       __rho_10_ = nondet();
       k3 = __rho_10_;
       if (k3>0) {
           k3--;
           keR = 1; keR = 0; keR = 1; keR = 0;
       }
       else {
           keR = 1; keR = 0; keR = 1; keR = 0;
           break;
       }
   }
   __rho_11_ = nondet();
   k4 = __rho_11_;
   while (1) {
       keA = 1; keA = 0; keA = 1; keA = 0;
       if (k4>0) {
           k4--;
           keR = 1; keR = 0; keR = 1; keR = 0;
       }
       else {
           keR = 1; keR = 0; keR = 1; keR = 0;
           break;
       }
   }
   keA = 1; keA = 0; keA = 1; keA = 0;
   __rho_13_ = nondet();
   k5 = __rho_13_;
   while (1) {
     if (!(k5>0)) break;
     __rho_56_ = nondet(); //The difference with version 1
       if(__rho_56_>0)
	 k5--;
   }
   keR = 1; keR = 0; keR = 1; keR = 0;

   while(1) { dummy=dummy; } L_return: return 0;
}


//version 3: 12
int keA; keR;
unsigned int pc;
int __phi() { return CAG(CIMP(CAP(keA==1),CAF(CAP(keR==1)))); }

void init() { keA = 0; keR = 0;}

int body() {
   keA = 1; keA = 0; keA = 1; keA = 0;
   __rho_2_ = nondet();
   k1 = __rho_2_;
   while (1) { 
     if (!(k1>0)) break;
       k1--;
   }
   keR = 1; keR = 0; keR = 1; keR = 0;
   keA = 1; keA = 0; keA = 1; keA = 0;
   __rho_6_ = nondet();
   k2 = __rho_6_;
   while (1) {
     if (!(k2>0)) break;
       k2--;
   }
   keR = 1; keR = 0; keR = 1; keR = 0;
   while (1) {
       keA = 1; keA = 0; keA = 1; keA = 0;
       __rho_10_ = nondet();
       k3 = __rho_10_;
       if (k3>0) {
           k3--;
           keR = 1; keR = 0; keR = 1; keR = 0;
       }
       else {
           keR = 1; keR = 0; keR = 1; keR = 0;
           break;
       }
   }
   __rho_11_ = nondet();
   k4 = __rho_11_;
   while (1) {
       keA = 1; keA = 0; keA = 1; keA = 0;
       if (k4>0) {
           k4--;
           keR = 1; keR = 0; keR = 1; keR = 0;
       }
       else {
           keR = 1; keR = 0; keR = 1; keR = 0;
           break;
       }
   }
   keA = 1; keA = 0; keA = 1; keA = 0;
   __rho_13_ = nondet();
   k5 = __rho_13_;
   while (1) {
     if (!(k5>0)) break;
       __rho_56_ = nondet();//The difference with version 1 & 2.... nested condition over _rho56
       if(__rho_56_>0) {
	 if(__rho_56_>0) {
	   k5--;
	 }
       }

   }
   keR = 1; keR = 0; keR = 1; keR = 0;

   while(1) { dummy=dummy; } L_return: return 0;
}
