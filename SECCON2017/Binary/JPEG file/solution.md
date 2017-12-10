# JPEG file

I used jpeginfo for this challenge. When I check the picture with the command: ```jpeginfo -cvi tktk-892009a0993d079214efa167cda2e7afc85e6b9cb38588cba9dab23eb6eb3d46.jpg``` and I got:
```
tktk-892009a0993d079214efa167cda2e7afc85e6b9cb38588cba9dab23eb6eb3d46.jpg  339 x 53   24bit JFIF  Normal Huffman,192dpi   11628  Corrupt JPEG data: premature end of data segment  Unsupported marker type 0xfc  [ERROR]
```
I made a jpeg file same pixel and compare with the picture in HXD. Search ```fc```, clearly at the first result, I can see the wrong byte.
Change ``` FF FC A2 ``` to ``` FD FC A2 ``` and tada:
