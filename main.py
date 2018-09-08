
import requests
import os
import re
# from pprint import pprint
# clear = lambda: os.system('cls')
folderlist = os.listdir()
def mname(name,symb):
	x = name.rfind(symb)
	newname = name[0:x]
	return newname
def searchomdb(title):
	req = requests.get("http://www.omdbapi.com/?apikey=" + omdbkey +"&t=" + title)
	maunil = (req.json())
	try:
		pass
		imrating = (maunil['imdbRating'] + " - " + title + " " + "(" +maunil['Year'] + ")")
		return imrating
	except:
		return oldname

def rename(path_from,path_to):
	absolute_from = os.path.join(os.getcwd(), path_from)
	absolute_to = os.path.join(os.getcwd(), path_to)
	try:
		os.rename(absolute_from, absolute_to)
		return True
	except:
		return False
omdbkey = input ("Enter omdb api key : ")
	
for i in folderlist:
	oldname = i
	c = i.count('[')
	d = i.count('(')
	a = 0
	while a<c:
		pass
		i = mname(i,"[")
		a = a+1
	a = 0
	while a<d:
		pass
		i = mname(i,"(")
		a = a+1

	aaa = searchomdb(i)
	print (aaa)
	rename(oldname,aaa)

print(' ')
os.system('pause')