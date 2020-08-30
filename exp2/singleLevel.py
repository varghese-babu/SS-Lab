list=["" for x in range(50)]
k=0

def add():
	fname=input("enter your file name :\n")
	if fname not in list:
		list.append(fname)
		return
	print("already found...\n")

def delete():
	fname=input("enter the file name to delete :\n")
	if fname in list:
		list.remove(fname)
		return
	print("not found.....\n")
	
def show():
	print("....files.....\n")
	for i in list:
		if(i==""):
			continue
		print(i)
	print()
	return

dname = input("enter directory name:\n")
while(1):
	print("1. add file\n2. delete file\n3. show files\n4. exit\nenter your choice:\n")
	ch=int(input())
	if(ch==1):
		add()
	elif(ch==2):
		delete()
	elif(ch==3):
		print("directory => ",dname)
		show()
	elif(ch==4):
		break
	else:
		print("invalid input\n")
