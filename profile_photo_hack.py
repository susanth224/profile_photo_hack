import os,commands
def username(id):
	if len(id)==1:r="000"+id
	elif len(id)==2:r="00"+id
	elif len(id)==3:r="0"+id
	else:r=id
	return r


batch = raw_input("Enter Batch ID: ").upper()
ImageFormatList=[".jpg",".JPG",".jpeg",".JPEG",".png",".PNG"]
bound=input("range: ")
os.system("mkdir "+batch)
for i in range(0,bound+1):
	ID=batch+username(str(i))
	for j in ImageFormatList:
                idF=ID+j
		os.system("wget -c http://10.11.4.35/SMS/usrphotos/user/"+idF+" -P "+batch)
		break

