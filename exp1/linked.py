list=[0]*100
flag=1
success=0
abort=0
st = int(input("enter starting index:"))
if(list[st]==0):
	list[st]=1
	flag=int(input("do you want to continue..1 to continue..0 to abort.."))
	while(flag==1):
		val = int(input("enter next index :"))
		if(list[val]==0):
			list[val]=1
			flag=int(input("do you want to continue..1 to continue..0 to abort.."))
			if(flag==1):
				continue
			else:
				success =1
				break
		else:
			print("already allocated....aborting....")
			flag=0
			break
	if(success==1):
		print("successfully allocated")
