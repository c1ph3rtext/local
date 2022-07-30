
#!/bin/python

import datetime
import base64
from string import *
import time
import random
import codecs
import sys
import os
import socket
from itertools import cycle
import pexpect as pex

perm_l = []
fact = lambda x : x and x * fact(x - 1) or 1
ilu = ascii_letters + punctuation

class Basic:
    def bopen_lines(self, file):
       """open files in binary (rb) read mode with function readlines()"""
       with open(file, "rb") as fp:
           con = fp.readlines()
       return con

    def open_lines(self, file):
       """open files in normal (r) read mode with function readlines()"""
       with open(file, "r") as fp:
           con = fp.readlines()
       return con

    def bparse(self, file):
       """open files in binary(rb) read mode with function read()"""
       with open(file, "rb") as fp:
           con = fp.read()
       return con

    def parse(self, file):
       """open files in normal(r) read mode with function read()"""
       with open(file, "r") as fp:
           con = fp.read()
       return con

class Base:
    def is64(self, s):
         try:
             print(base64.b64encode(base64.b64decode(s)))
             if base64.b64encode(base64.b64decode(s)) == s.encode():
                return True
         except Exception as e: pass

    def is32(self, s):
         try:
             if base64.b32encode(base64.b32decode(s)) == s.encode():
                return True
         except Exception as e: print ("Error: ", e)

    def is16(self, s):
         try:
             if base64.b16encode(base64.b16decode(s)) == s.encode():
                return True
         except Exception as e: print ("Error: ", e)

    def is85(self, s):
         try:
             if base64.b85encode(base64.b85decode(s)) == s.encode():
                return True
         except Exception as e: print ("Error: ", e)
    def d64(self, value):
        arg =  value.encode()
        dcoded = base64.b64decode(arg)
        return dcoded.decode()

    def e64(self, value):
        arg = value.encode()
        dcoded = base64.b64encode(arg)
        return dcoded.decode()

    def d32(self, value):
        arg = value.encode()
        dcoded = base64.b32decode(arg)
        return dcoded.decode()

    def e32(self, value):
        arg = value.encode()
        dcoded = base64.b32encode(arg)
        return dcoded.decode()

    def d16(self, value):
        arg = value.encode()
        dcoded = base64.b16decode(arg)
        return dcoded.decode()

    def e16(self, value):
        arg = value.encode()
        dcoded = base64.b16encode(arg)
        return dcoded.decode()

    def d85(self, value):
        arg = value.encode()
        dcoded = base64.b64decode(arg)
        return dcoded.decode()

    def e85(self, value):
        arg = value.encode()
        dcoded = base64.b85encode(arg)
        return dcoded.decode()
class Sock:
    def connect(self, host=None, port=None):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        return s
    def interact(self, soc):
        while 1:
            r = soc.recv(1024).decode()
            if r.isascii():
               print ("recved: ",r)
            snd = input("send: ")
            soc.send(snd.encode() + b"\r\n")
    def recvuntil(self, sock, string):
        buf = b""
        while 1:
            buf += sock.recv(1)
            if buf.endswith(string.encode()):
                  return buf

class CTF(Basic, Base, Sock):
    def crack_bar(self):
        for i in range(50):
            words = "".join(random.choices(ilu, k=16))
            time.sleep(0.10)
            print (f"CRACKING: [ {words} ]\t", flush=True, end="\r")
        print("\n", auto.now())

    def xor(self, c1, c2):
         return "".join([chr(ord(a) ^ ord(b)) for (a,b) in zip(c1,cycle(c2))])

    def perm(self, string, i=0):
         if i == len(string):
            perm_l.append("".join(string))

         for j in range(i, len(string)):
             words = [c for c in string]
             words[i], words[j] = words[j], words[i]
             self.perm(words, i + 1)
         return sorted(list(set(perm_l)))

    def rot13(self, val):
        txt = codecs.encode(val, "rot13")
        return txt
    def now(self):
        start = str(datetime.datetime.now()).split(".")[0]
        return start
    def hex2txt(self, val: str):
        v = val[2:]
        return bytes.fromhex(v).decode()
    def txt2bin(self, val):
        string = ""
        for i in val:
            string += bin(ord(i))[2:] + " "
        return string
    def bin2txt(self, val):
        x = [v for v in val.split(" ") if v != ""]
        for i in x:
            print(i)
#            print(chr(int(i,16)),end="")
        print()
ctf = CTF()
