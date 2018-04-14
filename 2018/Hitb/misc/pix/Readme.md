# Pix Writeup

Again we have a PNG file, and one more time I used zsteg, and we got a keepass file.

![img](https://github.com/BinhHuynh/CTF/blob/master/2018/Hitb/misc/pix/screenshot1.png)

Follow the hint, I created a password dictionary by this python code
now, let's find out the password by john:

![img](https://github.com/BinhHuynh/CTF/blob/master/2018/Hitb/misc/pix/screenshot2.png)

So the password is: `hitb180408`

Now what is being hidden in the keepass?

Boom:

![img](https://github.com/BinhHuynh/CTF/blob/master/2018/Hitb/misc/pix/screenshot3.png)
