list=[0]*100
flag=1
success=1
abort=0
while(flag==1):
	st = int(input("enter index block no:"))
	if(list[st]==0):
		list[st]=1
		n= int(input("enter no.of blocks..."))
		for i in range(0,n):
			j=int(input("enter the index number:"))
			if(list[j]==0):
				list[j]=1
			else:
				print("ithu locka monuse..sthalam vitto..")
				success=0
				flag=0
				break
		if(success==1):
			lag=int(input("do you want to continue..yes=>1 and no=>0"))
