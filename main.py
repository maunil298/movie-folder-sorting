
import requests
import os
import re

clear = lambda: os.system('cls')
#get all folder names in a list
folderlist = os.listdir()

#function for removing brackets or any other symbol specified
def mname(name,symb):
	x = name.rfind(symb)
	newname = name[0:x]
	return newname

#this function searches for title and gets json from omdb api, and returns string as imdbrating-title-year from json
def searchomdb(title):
	try:
		pass
		#search for title
		params_dict = {'apikey':omdbkey,'t':title}
		req = requests.get("http://www.omdbapi.com", params = params_dict)
		
		# store requested json to dictionary
		req_dictionary = (req.json())
		
		name_with_rating = (req_dictionary['imdbRating'] + " - " + title + " " + "(" +req_dictionary['Year'] + ")")
		return name_with_rating
	except:
		return False

def rename(old_foldername,new_foldername):
	old_path = os.path.join(os.getcwd(), old_foldername)
	new_path = os.path.join(os.getcwd(), new_foldername)
	try:
		os.rename(old_path, new_path)
		return True
	except:
		return False


omdbkey = input ("Enter omdb api key : ")
verifykey = searchomdb("troy")

while verifykey != "7.2 - troy (2004)":
	pass
	omdbkey = input("Enter correct omdb api key..!!  : ")
	verifykey = searchomdb("troy")

clear()
print("\n\n" + "OLD FOLDER NAME".ljust(25,' ') + "STATUS".ljust(25,' ') + "RENAMED TO\n\n")

for folder in folderlist:
	oldname = folder
	symbol_one = folder.count('[')
	symbol_two = folder.count('(')
	a = 0
	while a<symbol_one:
		pass
		folder = mname(folder,"[")
		a = a+1
	a = 0
	while a<symbol_two:
		pass
		folder = mname(folder,"(")
		a = a+1

	new_foldertitle = searchomdb(folder)
	
	if new_foldertitle == False:
		print (oldname.ljust(25,' ') + "Not Found ")
	else:
		print (oldname.ljust(25,' ') + "Renamed  ".ljust(25,' ') + new_foldertitle)
		rename(oldname,new_foldertitle)

print(' ')
os.system('pause')

