#include "../ctl.h"

/* prove that either IoCompleteRequest is called, 
   or a value other than STATUS_SUCCESS is returned. */
int __phi() { return COR(CAF(CAP(phi_io_compl == 1)),
			 CAF(CAP(phi_nSUC_ret  == 1))); }

void init() {
  keA = keR = ioA = ioR = 0; phi_nSUC_ret = 0; phi_io_compl = 0; __rho_666_ = nondet();
}

void KeAcquireSpinLock(int * lp, int * ip) { keA = 1; keA = 0; }
void KeReleaseSpinLock(int * lp, int i) { keR = 1; keR = 0; }

int body() {
  KeAcquireSpinLock(lock3, Irql);
  __rho_5_ = nondet(); k1 = __rho_5_;
  while (1) {
    if (!(k1>0)) break;
    k1--;
  }
  KeReleaseSpinLock(lock3, Irql);
  KeAcquireSpinLock(lock1, Irql);
  __rho_4_ = nondet(); k2 = __rho_4_;
  while (1) {
    if (!(k2>0)) break;
    k2--;
  }
  KeReleaseSpinLock(lock1, Irql);
  __rho_10_ = nondet(); k3 = __rho_10_;
  while (1) {
    KeAcquireSpinLock(lock4, Irql);
    if (k3>0) {
      k3--;
      KeReleaseSpinLock(lock4, Irql);
    }
    else {
      KeReleaseSpinLock(lock4, Irql);
      break;
    }
  }
  __rho_11_ = nondet(); k4 = __rho_11_;
  while (1) {
    KeAcquireSpinLock(lock5, Irql);
    if (k4>0) {
      k4--;
      KeReleaseSpinLock(lock5, Irql);
    }
    else {
      KeReleaseSpinLock(lock5, Irql);
      break;
    }
  }
  KeAcquireSpinLock(lock6, Irql);
  __rho_12_ = nondet(); k5 = __rho_12_;
  //if(__rho_666_>0) { assume(k5 > 0);} 
  while (1) {
    if (!(k5>0)) break;
    k5--;
    phi_io_compl = 1;
  }
  KeReleaseSpinLock(lock6, Irql);
  //if(__rho_666_<=0) { assume(ntStatus != STATUS_SUCCESS); }
  if(ntStatus != STATUS_SUCCESS) { phi_nSUC_ret = 1; }
}
