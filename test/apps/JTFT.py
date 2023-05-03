from json import load as l
from json import dump as d
from os.path import isdir
from os.path import isfile
from os import listdir as dir
from os import getcwd as pwd
from os import chdir as cd
from os import mkdir
from os import rename
from sys import argv as a

o = open
g = lambda f: l(o(f))
s = lambda f, x: d(x,o(f, 'w'))
child = lambda x, y: type(x, (y,), {})
E = child('E', Exception)
error = lambda x: child(x, E)
NotFileOrDirectory = error('NotFileOrDirectory')
ThisIsNotFTF = error('ThisIsNotFTF')
NotError=error('NotError')

def tfting(root: str, OneDir=True, Error=False, Warning=True):
	now, jtft = pwd(), {}
	cd(root)
	for x in dir():
		if isfile(x):
			with o(x) as f:
				jtft[x] = f.read()
		elif isdir(x):
			jtft[x] = tfting(x, OneDir=False)
		else:
			jtft[x] = None
			if Error:
				raise NotFileOrDirectory(
				 f'{x} is either file nor directory, not Support yet')
			elif Warning:
				print(
				 f'Warning : Error during execution, so that root of error sourse as null value\nroot of error : {x}\nError title : NotFileOrDirectory\nError massage : {x} is either file nor directory, not Support yet'
				)
			else:
				pass
	cd(now)
	if OneDir:
		return {root: jtft}
	else:
		return jtft


def untfting(jtft:dict,
             root='.',
             Error=False,
             Warning=True,
             NotTftError=True,
             NotTftWarning=True):
	now = pwd()
	cd(root)
	for i, j in jtft.items():
		if isinstance(j, str):
			with o(i, 'w') as f:
				f.write(j)
		elif isinstance(j, dict):
			mkdir(i)
			untfting(j, root=i)
		elif j == None:
			if Error:
				raise NotFileOrDirectory(
				 f"NotFileOrDirectory, It's Null value, It's means When Arcaiveing It's was raseid Error\n\nArcaiveingErrorMassage was like this : {i} is either file nor directory, not Support yet"
				)
			elif Warning:
				print(
				 f'\n\nArcaiveingErrorMassage was like this : Warning : Error during execution, so that root of error sourse as null value\nroot of error : {i}\nError title : NotFileOrDirectory\nError massage : {i} is either file nor directory, not Support yet'
				)
			else:
				pass
		else:
			if NotTftError:
				raise ThisIsNotFTF(f'I see... {i}:{j}, {jtft}')
			elif NotTftWarning:
				print(f"Warning : It's not TFT, but we Tring to UnTFTing, It can make you'r PC broken, stop doing to ^C : Ctrl • C\n I See It's not TFT when {i}:{j}, {jtft}")
			else:
				pass
	cd(now)

def jtfting(file:str,root:str,OneDir=True,Error=False, Warning=True):
    IfError=False
    errors=NotError("Haha.... sory bruh...\nhmm...... I'll developing hard")
    try:
        x=tfting(root,OneDir=OneDir,Error=Error, Warning=Warning)
        s(file+'.json',x)
    except Exception as error2:
        IfError=True
        errors=error2
    finally:
        try:rename(file+'.json',file)
        except:pass
    if IfError:
        raise errors
def unjtfting(file:str,
             root='.',
             Error=False,
             Warning=True,
             NotTftError=True,
             NotTftWarning=True):
    IfError=False
    errors=NotError("Haha.... sory bruh...\nhmm...... I'll developing hard")
    try:
             rename(file,file+'.json')
             f=g(file+'.json')
             untfting(f,root=root,Error=Error,Warning=Warning,NotTftError=NotTftError,NotTftWarning=NotTftWarning)
    except Exception as error2:
        IfError=True
        errors=error2
    finally:
        try:rename(file+'.json',file)
        except:pass
    if IfError:
        raise errors
def options(x):
    pass
def main():
    if a[1]=='jtft':
        if len(a)>4:
            b=a[4:]
            print('option not support',b)
        jtfting(a[2],a[3])
    elif a[1]=='unjtft':
        if len(a)>3:
            b=a[3:]
            print('option not support',b)
        unjtfting(a[2])
    else:
        print('jtft or unjtft please')
if __name__=="__main__":main()