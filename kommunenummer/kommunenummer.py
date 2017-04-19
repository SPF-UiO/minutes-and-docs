# -*- coding: utf-8 -*-
import numpy as np
import re
import codecs

class kommuneFind:
    kommuner = {}

    def __init__(self, filename):
        self.filename = filename
        infile = open(filename, 'r')
        kommuner = self.kommuner

        for line in infile:
            sample = line.split('\t')
            Postnummer, Kommunenummer, Kommune \
                 = sample[0], sample[2], sample[3]
            
            if Kommune in kommuner:
                kommuner[str(Kommune)][1].append(Postnummer) 
            else:
                kommuner[str(Kommune)] = [Kommunenummer,[Postnummer]]
        

        

        infile.close()
        
    def findKommune(self, Postnummer):
        kommuner = self.kommuner
        self.Postnummer = Postnummer
        for key in kommuner:
            if self.Postnummer in kommuner[key][1]:
                print key, kommuner[key][0]

          
    def returnKommuner(self):
        return self.kommuner

k = kommuneFind(filename = 'Postnummerregister.txt')
k.findKommune('1783')
K = k.returnKommuner()
print len(K)

outfile = open('Postnummeroppdatert.txt','w')


for key in K:
    nr = K[key][0]
    for postnummer in K[key][1]:
        outfile.write(key+'\t' + str(nr) + '\t' + str(postnummer) + '\n')

outfile.close()
