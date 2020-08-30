list=[0]*100
flag=1
success=1
while(flag==1):
	st = int(input("enter starting index:"))
	len = int(input("enter length:"))
	for i in range(st,(st+len)):
		if(list[i]==0):
			list[i]=1
		else:
			print("already allocated...cannot continue..aborting...")
			success=0
			break
	if(success==1):
		print("allocated successfully:")
		n =  int(input("continue -1 , else -0:"))
		if(n==1):
			continue
		else:
			flag=0
			break
	else:
		break
