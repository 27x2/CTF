# SharifCTF 2018 - hidden - 100p
## Description
  ``` Find the hidden process.```
  ```The flag is SharifCTF{MD5(Process id)}.```

File đề cho là một file dump, như thường lệ ta kiểm tra file bằng volatility với lệnh imageinfo để xem những thông tin cơ bản của file.
```$volatility -f dump imageinfo```

```INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : WinXPSP2x86, WinXPSP3x86 (Instantiated with WinXPSP2x86)
                     AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                     AS Layer2 : FileAddressSpace (/root/Desktop/chall/sharif/for/hidden/dump)
                      PAE type : PAE
                           DTB : 0x359000L
                          KDBG : 0x80545c60L
          Number of Processors : 1
     Image Type (Service Pack) : 3
                KPCR for CPU 0 : 0xffdff000L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2018-01-28 17:35:20 UTC+0000
     Image local date and time : 2018-01-28 21:05:20 +0330.
  ```
     
Ok đây vậy là profile của file dump là WinXPSP2x86, đề bài yêu cầu ta phải tìm hidden process, có một plugin rất hay của volatility hỗ trợ là ta xem các tiến trình là ```psxview```:
```$volatility -f dump --profile=WinXPSP2x86 psxview```

```Offset(P)  Name                    PID pslist psscan thrdproc pspcid csrss session deskthrd ExitTime
---------- -------------------- ------ ------ ------ -------- ------ ----- ------- -------- --------
0x010eb4c0 rundll32.exe            396 True   True   False    True   True  True    True     
0x01c279c0 svchost.exe             900 True   True   False    True   True  True    True     
0x01e64350 vmtoolsd.exe            404 False  True   False    True   True  True    True     
0x025b7020 explorer.exe           1576 True   True   False    True   True  True    True     
0x01e6d608 winlogon.exe            644 True   True   False    True   True  True    True     
0x01ecd378 svchost.exe             988 True   True   False    True   True  True    True     
0x031b1cf0 spoolsv.exe            1508 True   True   False    True   True  True    True     
0x01fbe410 lsass.exe               700 True   True   False    True   True  True    True     
0x0096c0e8 wscntfy.exe             920 True   True   False    True   True  True    True     
0x039347a8 svchost.exe            1188 True   True   False    True   True  True    True     
0x0308d9f0 svchost.exe            1604 True   True   False    True   True  True    True     
0x01c58798 vmacthlp.exe            856 True   True   False    True   True  True    True     
0x01de4878 svchost.exe            1236 True   True   False    True   True  True    True     
0x01bbd488 services.exe            688 True   True   False    True   True  True    True     
0x01fbd6e0 svchost.exe            1024 True   True   False    True   True  True    True     
0x02e7eb20 svchost.exe            1692 True   True   False    True   True  True    True     
0x01209a00 System                    4 True   True   False    True   False False   False    
0x01bbd900 smss.exe                548 True   True   False    True   False False   False    
0x021a7da0 csrss.exe               620 True   True   False    True   False True    True     
0x02dbb448 wmiprvse.exe            908 False  True   False    False  False False   False    2018-01-28 17:34:22 UTC+0000
0x01ebe168 cmd.exe                1704 False  True   False    False  False False   False    2018-01-28 17:34:00 UTC+0000
```
  
  Trong volatility thì lệnh ```pslist``` là in ra các tiến trình đang hoạt động rõ (tức là tường minh, đoạn này không biết dùng từ gì miêu tả cho đúng xD) còn `psscan` là hiện tất cả các tiến trình bao gồm cả tiến trình ẩn. Như vậy ta thấy tiến trình `vmtoolsd.exe` với ```PID: 404``` chính là tiến trình ta cần tìm
