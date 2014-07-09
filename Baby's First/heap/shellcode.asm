  sub    $0x30,%rsp
  mov    $0x400664,%esi
  mov    $0x400666,%edi
  callq  0x400490
  mov    %rax,-0x8(%rbp)
  jmp    4005be <main+0x28>
  movsbl -0x9(%rbp),%eax
  mov    %eax,%edi
  callq  400450 <putchar@plt>
  mov    -0x8(%rbp),%rax
  mov    %rax,%rdi
  callq  400460 <fgetc@plt>
  mov    %al,-0x9(%rbp)
  cmpb   $0xff,-0x9(%rbp)
  jne    4005b3 <main+0x1d>
  mov    $0x0,%eax
  leaveq 
  retq   
  nopw   0x0(%rax,%rax,1)
