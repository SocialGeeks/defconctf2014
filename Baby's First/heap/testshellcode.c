#define SYSCALL_READ 3
#define FD_STDIN 0
#define MAX_LEN 4096

char shellcode[MAX_LEN];


int __readShell() {
  int ret;
  asm volatile("int $0x80"
	       : "=a"(ret)
	       : "a"(SYSCALL_READ), "b"(FD_STDIN), "c"(shellcode), "d"(MAX_LEN));
  return ret;
}

int main()
{
  void (*shell)();

  __readShell();

  shell = (void (*)()) shellcode;
  shell();
  return 0;
}
