# TUCTF 2017 Reverse Writeup

### funmail

Open file in IDA, we will get:

```
User name: john galt
Password: this-password-is-a-secret-to-everyone!
```
Boom, read the mail and capture the flag

### funmail 2.0

Open file in IDA again, at this challenge we can see in the soure code that user name and password do not need for this challenge. Take a look for PrintFlag function, it will be xor the cipher with 7 than encrypt it in ROT 13. Write a small script we will get the flag or you can solve it by hand xD
