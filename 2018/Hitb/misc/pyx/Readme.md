# Pyx writeup

In this challenge, we have a png file. Firstly, I put it into pngtweak to check it.

Oh, something error here, let's open it's in 010 Hex Editor. As you can see, the 010 Hex Editor can't identified the last chunk (it's IEND chunk).
By the notification of PNG tweak, we knew the problem is the length of the IDAT chunk, you can fix it by do the math:

Hm, let's check it again by PNGtweak, oops we need to fix the CRC. 

Okay now it's correct but nothing here.

This time, I used zsteg and got something

It's a zlib, let uncompress it by zlib-flate

Hm it's look like a hex code, check the header we can easily know it's a 7z file.

Nah, It's request the password, I tried a brucrefore but it's not necessary because the password is the string we can see when open the file in 010 Hex Editor

Tada the flag is:
