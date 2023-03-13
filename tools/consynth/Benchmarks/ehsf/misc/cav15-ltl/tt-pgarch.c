// Property: G F wakened==1

void init() {
  wakend = 1; got_SIGHUP = NONDET;
}


int time(int a) { return nondet(); }
#define PGARCH_AUTOWAKE_INTERVAL 1000

void body() {
        wakend = true;
        while(1)
        {
                if (got_SIGHUP>0)
                {
                        got_SIGHUP = 0;
			  if (NONDET) break;
                }
                if (wakend>0)
                {
                        wakend = 0;
                        last_copy_time = time(NULL);
                }
                if (wakend<=0)
                {
                        curtime = time(NULL);
                        if ((curtime - last_copy_time) >= PGARCH_AUTOWAKE_INTERVAL) wakend = true;
                }
		if (NONDET) break;
        }

  while(1) { dummy=dummy; } L_return: return 0;
}

int main() {}
