#!/usr/bin/env python3

import csv
import json

result = {}
cattorkts = {}

def fillCatalogue(filename, catname):
    global cattorkts
    res = {}
    cattorkts[catname] = res
    with open(filename, newline='') as csvfile:
        r = csv.reader(csvfile)
        for row in r:
            try:
                rktsid = int(row[1])
                catid = int(row[0])
            except ValueError as ex:
                pass
            res[catid] = rktsid

def fillCatalogues(tengyur=False):
    if not tengyur:
        fillCatalogue('D-rKTs.csv', 'D')
        fillCatalogue('H-rKTs.csv', 'H')
        fillCatalogue('N-rKTs.csv', 'N')
        fillCatalogue('S-rKTs.csv', 'S')
        #fillCatalogue('A-rKTs.csv', 'A')
    else:
        fillCatalogue('D-rKTsT.csv', 'D')
        fillCatalogue('G-rKTsT.csv', 'G')
        fillCatalogue('N-rKTsT.csv', 'N')
        fillCatalogue('Q-rKTsT.csv', 'Q')
    

def fillOutline(filename, workname, catname):
    global cattorkts, result
    catcorr = cattorkts[catname]
    with open(filename, newline='') as csvfile:
        r = csv.reader(csvfile)
        for row in r:
            nodeid = row[0]
            catid = 0
            try:
                catid = int(row[1])
            except ValueError as ex:
                continue
            if catid not in catcorr:
                continue
            rktsid = catcorr[catid]
            if rktsid not in result:
                result[rktsid] = {}
            idcorrsgen = result[rktsid]
            if workname not in idcorrsgen:
                idcorrsgen[workname] = []
            idcorrsgen[workname].append(nodeid)


def fillOutlines(tengyur=False):
    if not tengyur:
        fillOutline('W1PD96682-D.csv', 'W1PD96682', 'D')
        fillOutline('W1PD96685-N.csv', 'W1PD96685', 'N')
        fillOutline('W4CZ7445-D.csv', 'W4CZ7445', 'D')
        fillOutline('W22084-D.csv', 'W22084', 'D')
        fillOutline('W22703-N.csv', 'W22703', 'N')
        fillOutline('W26071-H.csv', 'W26071', 'H')
        fillOutline('W29468-N.csv', 'W29468', 'N')
        fillOutline('W22083-S.csv', 'W22083', 'S')
        fillOutline('W4CZ5369-D.csv', 'W4CZ5369', 'D')
    else:
        fillOutline('W1GS66030-D.csv', 'W1GS66030', 'D')
        fillOutline('W23703-D.csv', 'W23703', 'D')
        fillOutline('W22704-Q.csv', 'W22704', 'Q')
        fillOutline('W1KG13126-Q.csv', 'W1KG13126', 'Q')
        fillOutline('W1PD95844-D.csv', 'W1PD95844', 'D')
        fillOutline('W23702-Q.csv', 'W23702', 'Q')

fillCatalogues()
fillOutlines()
with open('rkts-bdrc.json', 'w') as fp:
    json.dump(result, fp, indent=4, sort_keys=True)

result = {}
cattorkts = {}
fillCatalogues(True)
fillOutlines(True)
with open('rktst-bdrc.json', 'w') as fp:
    json.dump(result, fp, indent=4, sort_keys=True)
