# SharifCTF 2018 - client - 75p
## Description
```
  Attached file is the homepage of the client01. He knows the flag.
```
Đề bài là một file zip trông như một ổ đĩa vậy, ta để ý thấy có folder .thunderbird. Hmmm theo tiêu đề có thể là flag dấu trong mail của chủ ổ đĩa này vào check folder thì ta sẽ thấy file INBOX, vào kiểm tra ta sẽ thấy một email với tiêu đề là flag kèm với đó là link: 

![img](https://imgur.com/a/7cve0)


```http://www.filehosting.org/file/details/720884/file```, thử tải về xem sao.
Mở file vừa tải bằng `HXD`, ta thấy đó là một file ảnh nhưng bị thiếu mất 1 byte ở phần header.

![img](https://imgur.com/a/EqG3x)

Nếu thiếu thì mình chèn vào thôi, ```89 4E 47``` thành ```89 4E 47```

Và thế là ta có flag:

![img](https://github.com/BinhHuynh/CTF/blob/master/2018/sharif/forensics/client%2001/flag.png)
