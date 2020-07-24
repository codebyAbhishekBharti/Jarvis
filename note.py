import datetime

try:
	obj = open("note.txt")
except :
	obj= open("note.txt","w+")
obj =open("note.txt",)
for line in obj:
	print(line,end='')
	
with open("note.txt",'a')as obj:
	time=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
	note =[format(time),":- \n ",input("\n\n\t\t note here what do you want to save in notes \n\n"),". \n "]
	obj.writelines(note)
print("\n\nFile is successfully saved")