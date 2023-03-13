int main(void){
  int x = 0;
  int y = 1;
  int* p1 = &x;
  int* p2 = &y;

  if (*p1 == *p2)
    {
      goto ERROR;
      return(0);
    }
  return(0);
 ERROR: 
  return(0);
}
