# Tokyo Westerns CTF 3rd 2017 

###Rev Rev Rev 

We have a ELF file, let excute it and see what it does
```
./rev_rev_rev 
Rev! Rev! Rev!
Your input: AAAAA
Invalid!

```
So if we input right string we will have a flag.

```
ltrace ./rev_rev_rev 
__libc_start_main(0x80485ab, 1, 0xbf824de4, 0x80487f0 <unfinished ...>
puts("Rev! Rev! Rev!"Rev! Rev! Rev!
)                           = 15
printf("Your input: ")                           = 12
fgets(Your input: TWCTF{
"TWCTF{\n", 33, 0xb77825a0)                = 0xbf824d0b
strchr("TWCTF{\n", '\n')                         = "\n"
strlen("TWCTF{")                                 = 6
strcmp("!\235\325=\025\325", "A)\331e\241\361\341\311\031\t\223\023\241\t\271I\271\211\335a1i\241\361q!\235\325=\025\325") = -1
puts("Invalid!"Invalid!
)                                 = 9
+++ exited (status 0) +++

```

Great! As we can see, the string we have to input is flag, and the characters have been mapped ( T = \325, W = \025 ...). So we have to do is write a simple script to find mapping of all character.
After find all mapping I have

```
TWCTF{qpzisyDnbmboz76oglxpzYdk}
```

Okay let check it out

```
./rev_rev_rev 
Rev! Rev! Rev!
Your input: TWCTF{qpzisyDnbmboz76oglxpzYdk}
Correct!

```


Great so flag is:
```
TWCTF{qpzisyDnbmboz76oglxpzYdk}
```

