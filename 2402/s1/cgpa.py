import pprint,re
fname = input("Enter the name of the file:")
failed = 0
studdic={}
cgpa= {}

def cgpacal(grades):
	point=0
	for i in grades:
		if("(O)" in i):
			point+=10
		elif("(A+)" in i):
			point+=9
		elif("(A)" in i):
                        point+=8.5
		elif("(B+)" in i):
                        point+=8
		elif("(B)" in i):
                        point+=7
		elif("(C)" in i):
                        point+=6
		elif("(P)" in i):
                        point+=5

	return("{:.2f}".format(point/float(len(grades))))


with open(fname,"r+") as f:
	for i in f:
		if(re.search("(F)", i)):
			studdic[i.split()[0]] =-len(re.findall("(F)",i))
		else:
			studdic[i.split()[0]]=cgpacal(i.split()[1:]) 

rfname =  fname.split('.')[0]+"-cgpa.txt"

with open(rfname,'w+') as rf:
	for student in sorted(studdic.keys()):
		rf.write("{0}\t{1}\n".format(student,studdic[student]))

choice = input("Do you want to calculate the sgpa[Y/N]:")

if(choice.upper()=='Y'):
	fname2 = input("Filename of old sgpa calculated file:\n")
	with open(fname2,'r') as f:
		for i in f:
			slis = i.split()
			omark = float(studdic[slis[0]])
			nmark = float(slis[1])

			if(omark > 0 and nmark>0):
				cgpa[slis[0]] = float("{:.2f}".format((omark+nmark)/2))

			elif(omark > 0 and nmark>0):
				cgpa[slis[0]] = int(nmark)

			elif(omark < 0 and nmark>0):
                                cgpa[slis[0]] =int(omark)

			elif(omark < 0 and nmark < 0):
                                cgpa[slis[0]] =int(nmark + omark)

with open('studname.txt','r') as name:
	with open('cgpa.txt','w+') as cgpa:
		for i in name:
			rollno = i.split()[0]
			name = i.split()[1]
cgpa.write("{}\t{}\t{}".format(rollno,name,cgpa[rollno]))

