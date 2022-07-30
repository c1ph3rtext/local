#!/bin/python

import datetime
import base64
from string import *
import time
import random
import codecs
import itertools
import sys
import os
import socket
from itertools import *


perm_l = []
fact = lambda x : x and x * fact(x - 1) or 1
ilu = ascii_letters + punctuation

def bopen_lines(file):
   """open files in binary (rb) read mode with function readlines()"""
   with open(file, "rb") as fp:
       con = fp.readlines()
   return con

def open_lines(file):
   """open files in normal (r) read mode with function readlines()"""
   with open(file, "r") as fp:
       con = fp.readlines()
   return con

def bparse(file):
   """open files in binary(rb) read mode with function read()"""
   with open(file, "rb") as fp:
       con = fp.read()
   return con

def parse(file):
   """open files in normal(r) read mode with function read()"""
   with open(file, "r") as fp:
       con = fp.read()
   return con

def connect(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s
def recvuntil(sock, string):
    buf = b""
    while 1:
        buf += sock.recv(1)
        if buf.endswith(string.encode()):
              return buf
def crack_bar():
    for i in range(50):
        words = "".join(random.choices(ilu, k=16))
        time.sleep(0.10)
        print (f"CRACKING: [ {words} ]\t", flush=True, end="\r")
    print("\n", auto.now())

def is64(s: bytes):
     try:
         if base64.b64encode(base64.b64decode(s)) == s.encode():
            return True
     except Exception as e: print ("hi", e)

def is32(s):
     try:
         if base64.b32encode(base64.b32decode(s)) == s.encode():
            return True
     except Exception as e: print ("hi", e)

def is16(s):
     try:
         if base64.b16encode(base64.b16decode(s)) == s.encode():
            return True
     except Exception as e: print ("hi", e)

def is85(s):
     try:
         if base64.b85encode(base64.b85decode(s)) == s.encode():
            return True
     except Exception as e: print ("hi", e)

def xor(c1, c2):
     return "".join([chr(ord(a) ^ ord(b)) for (a,b) in zip(c1,cycle(c2))])

def perm(string, i=0):
     if i == len(string):
        perm_l.append("".join(string))

     for j in range(i, len(string)):
         words = [c for c in string]
         words[i], words[j] = words[j], words[i]
         perm(words, i + 1)
     return perm_l, i

def rot13(val):
    txt = codecs.encode(val, "rot13")
    return txt
def now():
    start = str(datetime.datetime.now()).split(".")[0]
    return start
def d64(value):
    arg = value.encode()
    dcoded = base64.b64decode(arg)
    return dcoded.decode()
def e64(value):
    arg = value.encode()
    dcoded = base64.b64encode(arg)
    return dcoded.decode()
def d32(value):
    arg = value.encode()
    dcoded = base64.b32decode(arg)
    return dcoded.decode()
def e32(value):
    arg = value.encode()
    dcoded = base64.b32encode(arg)
    return dcoded.decode()
def d16(value):
    arg = value.encode()
    dcoded = base64.b16decode(arg)
    return dcoded.decode()
def e16(value):
    arg = value.encode()
    dcoded = base64.b16encode(arg)
    return dcoded.decode()
def d85(value):
    arg = value.encode()
    dcoded = base64.b64decode(arg)
    return dcoded.decode()
def e85(value):
    arg = value.encode()
    dcoded = base64.b85encode(arg)
    return dcoded.decode()


