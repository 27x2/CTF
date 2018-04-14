# Pyx writeup

In this challenge, we have a png file. Firstly, I put it into pngtweak to check it.

![img](https://github.com/BinhHuynh/CTF/blob/master/2018/Hitb/misc/tpyx/Screenshot1.PNG)

Oh, something error here, let's open it's in 010 Hex Editor. As you can see, the 010 Hex Editor can't identified the last chunk (it's IEND chunk).

By the notification of PNG tweak, we knew the problem is the length of the IDAT chunk change `1162839` to `1164470`

![img](https://github.com/BinhHuynh/CTF/blob/master/2018/Hitb/misc/tpyx/Screenshot2.PNG)

Hm, let's check it again by PNGtweak, oops CRC error, change `BA3DE214h` to `6A0412FFh`. 

Okay now it's correct but nothing here.

This time, I used zsteg and got something

![img](https://github.com/BinhHuynh/CTF/blob/master/2018/Hitb/misc/tpyx/Screenshot3.PNG)

It's a zlib, let uncompress it by zlib-flate
`zlib-flate -uncompress < Untitled1.zlib`


Hm it's look like a hex code, check the header we can easily know it's a 7z file.

Nah, It's request the password, I tried a brucrefore but it's not necessary because the password is the string we can see when open the file in 010 Hex Editor

![img](https://github.com/BinhHuynh/CTF/blob/master/2018/Hitb/misc/tpyx/Screenshot4.PNG)

![img](https://github.com/BinhHuynh/CTF/blob/master/2018/Hitb/misc/tpyx/Screenshot5.PNG)
