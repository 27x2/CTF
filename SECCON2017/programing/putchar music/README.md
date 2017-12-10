# Solution

Compile the find then use mplayer to listen the music we'll get the flag

```
./putchar_music | mplayer -demuxer rawaudio -rawaudio rate=8000:channels=1:samplesize=1 -
```

The flag is: SECCON{STAR_WARS}
