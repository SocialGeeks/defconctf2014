Lightning: 4 points

# dosfun4u  

## Instructions  

Welcome to DOS, this is going to suck   
http://services.2014.shallweplayaga.me/dosfun4u_5d712652e1d06a362f7fc6d12d66755b   
dosfun4u_5d712652e1d06a362f7fc6d12d66755b.2014.shallweplayaga.me:8888  

## pwn it!  
~~The file is a gzip file?~~

It's an image that appears to be for use with bochs since there's a bochsrc.

The associated port to connect to reports that it needs data before continuing:

> Due to CPU reqs, you must provide data starting with GKJHMBCHEMMNEIDB of length 22 where the sha1 hash starts with 3 null bytes before continuing

The string changes each connection.

I was able to get this working under the current version of bochs in the ubuntu repos. When you start it, it will fail to autodetect HD geometry but you can CONT and it will boot. You need to connect to it on serial com1, which is emulated to localhost:8888. Once you've connected to it, it will show a map of the Rio on the emulation screen and display no data...

I booted it to a DOS floppy image that is still included in the config file, and there are two text files in the root dir. Whatever this thing is, there are TWO keys, one that gives you extra points or something... presumably, doing *something* to the program will cause it to spit out a key in one of these files. Not sure what the thing you need to do is.
