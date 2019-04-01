#!/usr/bin/env python3

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

tablehash = [None]*8

for donnee in donnees:
    hash8 = hash(donnee[1])%8
    if (tablehash[hash8] is None):
        tablehash[hash8] = {}        
    tablehash[hash8][len(tablehash[hash8])] = [donnee[0], donnee[1]] 

for entree in tablehash:
    print (str(entree))
