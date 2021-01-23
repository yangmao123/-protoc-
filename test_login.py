#! /usr/bin/python

import argis_pb2


address_book = argis_pb2.TT()
with open("data.bin", "rb") as f:
    address_book.ParseFromString(f.read())
    print(len(address_book.ins.dsfsdd.d))
    for i in address_book.ins.dsfsdd.d:
        print(i.r)
        break
