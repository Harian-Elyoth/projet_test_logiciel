import os

def parcoursRecursif():
	dirList = os.listdir("./")
	for dir in dirList:
		if(dir.startswith("dependenci")):
			command = "./" + dir
			os.system(command)
		if (dir.endswith(".py") & dir.startswith("test")):
			command = "python3 -m unittest " + dir
			os.system("echo")
			os.system("echo /////////////////////////////////////////////")
			os.system("echo " + dir)
			os.system("echo /////////////////////////////////////////////")
			os.system(command)
		if os.path.isdir(dir) == True:
			os.chdir(dir)
			parcoursRecursif()
			os.chdir("..")
			
if __name__ == "__main__":
	parcoursRecursif()
