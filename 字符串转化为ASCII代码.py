# -*- coding: utf-8 -*-
import binascii
#16进制整数转ASCii编码字符串
a = 0x18181818
b = hex(a) #转换成相同的字符串即'0x18181818'
b = b[2:]  #截取掉'0x'
c = binascii.a2b_hex(b) #转换成ASCii编码的字符串
print("c:%s" %(c))