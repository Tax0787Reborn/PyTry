from shutil import move as m
from os import mkdir
from os import rmdir
from os import chdir as cd
from sys import argv as a
def UnArc():
    m('a/a1','PyTry/ChatUI_HouseOfPytry.ent')
    cd('PyTry')
    mkdir('HexTest')
    cd('..')
    m('a/a2','PyTry/HexTest/bmp_24.bmp')
    m('a/a3','PyTry/HexTest/230329.ent')
    rmdir('a')
def Arced():
    mkdir('a')
    m('PyTry/ChatUI_HouseOfPytry.ent','a/a1')
    m('PyTry/HexTest/bmp_24.bmp','a/a2')
    m('PyTry/HexTest/230329.ent','a/a3')
    cd('PyTry')
    rmdir('HexTest')
    cd('..')
if a[1]=='build':
    UnArc()
else:
    Arced()