// ****************************************************
//
//     Making Prophecies with Decision Predicates
//
//              Byron Cook * Eric Koskinen
//                     July 2010
//
// ****************************************************

// Benchmark: fig8-2007.c
// Property: G(a => F r)

#define STATUS_SUCCESS 1
#define STATUS_OBJECT_NAME_COLLISION 2
#define PC_IO 1
#define PC_NIO 0
int pc;
int i; int Pdolen; int num; int DName;
int lptNamei; //[5];
int dcIdi; // [5];
int Pdoi; //[5];
int PdoType; int status;

void init() { set = unset = 0; }

// The Program
void body() {
  set = 1; set = 0;
  while (i < Pdolen) { 
    DName = NONDET; 
    if (!DName) { break; } 
    status = NONDET; 
    if (1 != status) { 
      if (2 == status) { 
	goto loc_continue; 
      } 
      break; 
    } else { 
      i++; 
    } 
  } 
  unset = 1; unset = 0;
 loc_continue:0;
}

int main() { }
