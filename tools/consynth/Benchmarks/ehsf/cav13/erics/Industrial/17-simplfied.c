
int WItemsNum;
int __rho_1_;
int __rho_2_;
int __phi() { return CAG(CAF(CAP(WItemsNum>=1))); }

void init() { WItemsNum = nondet(); }


void body() {
  __rho_1_ = nondet();
    WItemsNum = __rho_1_;
    while(1) {
      while(1) { 
	__rho_2_ = nondet();
	if (WItemsNum<=5) { if (__rho_2_>0) break; }
	       WItemsNum++;
        }
    
      while(1) { 
	if (!(WItemsNum>2)) break;
             WItemsNum--;
        }
      WItemsNum = 1;
    }
  while(1) { dummy=dummy; } L_return: return 0;
}
    
int main () {}