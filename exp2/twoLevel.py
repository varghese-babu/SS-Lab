dir=["" for x in range(50)]
files=["" for x in range(50)]


def addDir():
	dname=input("enter directory name :\n")
	if dname not in dir:
		dir.append(dname)
		return
	print("already found...\n")

def deleteDir():
	dname=input("enter directory name to delete :\n")
	if dname in dir:
		dir.remove(dname)
		return
	print("not found.....\n")
	
def showDir():
	print("\n....Directories....\n")
	for i in dir:
		if(i==""):
			continue
		print(i)
	print()
	return
	
def addFile():
	fname=input("enter file name :\n")
	if dname not in files:
		files.append(fname)
		return
	print("already found...\n")

def deleteFile():
	fname=input("enter file name to delete :\n")
	if fname in files:
		files.remove(fname)
		return
	print("not found.....\n")
	
def showFile():
	print("\n....Files....\n")
	for i in files:
		if(i==""):
			continue
		print(i)
	print()
	return

dname = input("enter directory name:\n")
while(1):
	print("1. add file\n2. delete file\n3. show files\n4. add directory\n5. delete directory\n6. show directories\n7. exit\nenter your choice:\n")
	ch=int(input())
	if(ch==1):
		addFile()
	elif(ch==2):
		deleteFile()
	elif(ch==3):
		showFile()
	elif(ch==4):
		addDir()
	elif(ch==5):
		deleteDir()
	elif(ch==6):
		showDir()
	elif(ch==7):
		break
	else:
		print("invalid input\n")
