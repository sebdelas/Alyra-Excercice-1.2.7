#!/usr/bin/env python3

import hashlib

donnees = [
            ['Amsterdam', '153.8.223.72'],
            ['Chennai', '169.38.84.49'],
            ['Dallas', '169.46.49.112'],
            ['Dallas, TX, USA', '184.173.213.155'],
            ['Frankfurt', '159.122.100.41'],
            ['Hong Kong', '119.81.134.212'],
            ['London', '5.10.5.200'],
            ['London', '158.176.81.249'],
            ['Melbourne', '168.1.168.251'],
            ['Mexico City', '169.57.7.230'],
            ['Milan', '159.122.142.111'],
            ['Paris', '159.8.78.42'],
            ['San Jose', '192.155.217.197'],
            ['São Paulo', '169.57.163.228'],
            ['Toronto', '169.56.184.72'],
            ['Washington DC', '50.87.60.166']
          ]

tablehash = {}

for donnee in donnees:
    hash8 = str(hashlib.md5(donnee[1].encode('utf-8')).hexdigest())[0:8]
    collision = False
    while hash8 in tablehash:
        collision = True
        hash8 = str(hashlib.md5(hash8.encode('utf-8')).hexdigest())[0:8]
    tablehash[hash8] = [donnee[0], donnee[1]]

print (str(tablehash))
