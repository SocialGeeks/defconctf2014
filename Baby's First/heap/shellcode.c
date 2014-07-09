#include <stdlib.h>
#include <stdio.h>
 
int main() {
   char ch, file_name[25];
   FILE *fp;
 
   fp = fopen("flag", "r");
 
   while( ( ch = fgetc(fp) ) != EOF )
      printf("%c",ch);
 
   return 0;
}

