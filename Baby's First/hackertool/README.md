Baby's First: 1 points  

# hackertool  

## Instructions  

hey, we need to check that your connection works, torrent this file and md5 it   

http://services.2014.shallweplayaga.me/hackertool.torrent_fe3b8b75e9639d35e8ac1d9809726ee2  

## hints  

KINDA A HINT FOR HACKERTOOL: http://imgur.com/XCtMjJ2  

## pwn it!   

-- buddha's notes -----  

ran strings on the .torrent for 'key' found
Using bless, found:
6B 65 79 20 27 B4 04 8B 44 BE 76 05 35 BD B8 E9 3B F7 CC 4B 4E 49 08 78 B3 94 E5 4C EF 0D 84 9F 28 63 04 C7 B7 B2 32 3D 9C 5F 20 B1 2E FA 89 10 9D FC F3 3D 62 24 8E 16 CE C9 6E 01 57 B6 9B 41 C3 BB B7 71 C7 72 66 2F 20 07 DD 23 4F CB 32 9D C0 D8 3F 63 15 FA 1F 7B 53 F2 4E 89 89 8A B5 90 D6 1D DD B1 15 25 BA F4 24 AD 20 07 4B AF D9 C1 EC AE 2D D9 BB F0 8E 99 4D 12 12 2D FB 12 0C 82 60 75 B3 7D 1F BE 2C C3 3F A5 AC 3C 9B 7B 52 DA 10 AE 9B 70 7D FA 09 81 99 68 BC DC F8 C8 AA 21 1B E2 88 50 3C AE 05 2D D5 E4 CC 10 88 EB 5A 84 9E 97 60 57 F7 F6 AD 2D 3C 49 EE A1 48 2A 02 81 1A D5 05 13 EF 9B 1C 71 8E D2 F3 EF A0 A3 87 81 65 99 53 C4 76 F6 41 E9 79 26 C0 54 2C 95 AE B3 D3 6A 4B 5F 7A 35 FD AA 9B 52 7C 73 76 57 AE 19 DD 97 8D 38 49 5A 36 B1 74 C0 7B DC 73 C5 72 B4 D8 B5 1B E8 E0 56 93 3F 40 D5 30 9E DD 30 8A C2 ED 95 15 82 C5 9C 63 9C 5D 3F 3D 9A BC 25 E3 A6 75 AA 3E 8D 00 F3 4F 99 75 19 8E 88 7F 94 7E 15 E3 30 48 BB 8E 8C 03 36 87 3C 04 79 6B 73 F4 D5 D3 18 63 87 33 25 1B 74 B1 F9 74 6A 71 86 F6 3D 3F FF 29 18 53 88 D4 A3 F8 98 FD 58 A8 E7 5E 8F A7 6C EC 31 3B CE 2D E3 A3 D7 46 6F 7D 66 2A 9F 6D 16 53 82 4E BD FD 25 68 13 C1 D3 3C 96 D7 6C 16 38 6E 13 C5 F4 40 DF 5C 27 D4 41 30 AB 61 5C 77 30 BA B0 84 24 A3 9D DE A4 91 89 B0 30 FA F1 D5 55 27
key '\B4\8BD\BEv5\BD\B8\E9;\F7\CCKNIx\B3\94\E5L\EF
\84\9F(cǷ\B22=\9C_ \B1.\FA\89\9D\FC\F3=b$\8E\CE\C9nW\B6\9BAû\B7q\C7rf/ \DD#O\CB2\9D\C0\D8?c\FA{S\F2N\89\89\8A\B5\90\D6ݱ%\BA\F4$\AD K\AF\D9\C1\EC\AE-ٻ\F0\8E\99M-\FB\82`u\B3}\BE,\C3?\A5\AC<\9B{R\DA\AE\9Bp}\FA	\81\99h\BC\DC\F8Ȫ!\E2\88P<\AE-\D5\E4\CC\88\EBZ\84\9E\97`W\F7\F6\AD-<I\EE\A1H*\81\D5\EF\9Bq\8E\D2\F3\87\81e\99S\C4v\F6A\E9y&\C0T,\95\AE\B3\D3jK_z5\FD\AA\9BR|svW\AEݗ\8D8IZ6\B1t\C0{\DCs\C5r\B4ص\E8\E0V\93?@\D50\9E\DD0\8A\C2\ED\95\82Ŝc\9C]?=\9A\BC%\E3\A6u\AA>\8D\00\F3O\99u\8E\88\94~\E30H\BB\8E\8C6\87<yks\F4\D5\D3c\873%t\B1\F9tjq\86\F6=?\FF)S\88ԣ\F8\98\FDX\A8\E7^\8F\A7l\EC1;\CE-\E3\A3\D7Fo}f*\9FmS\82N\BD\FD%h\C1\D3<\96\D7l8n\C5\F4@\DF\'\D4A0\ABa\w0\BA\B0\84$\A3\9Dޤ\91\89\B00\FA\F1\D5U'

The main file hash didn't work, but I'm guessing there is a way to calc the MD5 hash of each file without downloading it. I'll keep working on this tomorrow (sat).

-- mav's notes -----

This is a joke. An old one, but I don't know where I saw it... if you connect to the torrent, it contains only one file: a file called something like every_IP_address_ever.txt

Should you download some of that file, you'll find that it literally is IP addresses, every single one, from 0.0.0.0 to 255.255.255.255.

Running the script generates the same output as the file to stdout. Pipe output into md5sum and wait - a few minutes later (depending on how fast your computer is - it's a lot of data!) out pops the md5sum, which is the key, done.
