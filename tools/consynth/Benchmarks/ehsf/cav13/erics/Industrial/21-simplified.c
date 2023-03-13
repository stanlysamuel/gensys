// pgarch-succeed/original.c in the benchmarks

unsigned int _NONDET;
int wakend, last_copy_time = 0, curtime, got_SIGHUP;
int __rho_1_;
void init() { wakend = 1; got_SIGHUP = _NONDET; }
int __phi() { return CAG(CAF(CAP(wakend == 1))); }

void body() {
  wakend = 1;
  while(1) {
    if (got_SIGHUP>0) {
      got_SIGHUP = 0;
      __rho_1_ = _NONDET;
      if (__rho_1_ <= 0) break; 
    }
    if (wakend>0) { 
l1:   wakend = 0; 
      last_copy_time = _NONDET;
    }
    if (wakend<=0) {
      curtime = _NONDET;
      if ((curtime-last_copy_time)>=1000) wakend = 1;
    }
    if (_NONDET<=0) { break; }
  }
l2:  while(1) { wakend = 1; } 
  return 0;
}

