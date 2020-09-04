import os, sys

def convertText(line) :

	newLine = convertCurrency(line)

	return newLine	

def main():
	try :
		para = open(sys.argv[1], 'r') 
	except :
		print("Error opening file")
		return 
	lines = para.readlines() 
	initialize()

	filename, file_extension = os.path.splitext(sys.argv[1])
	outfile = filename + '-converted' + file_extension

	out = open(outfile, 'w')
	for line in lines :
		line = convertText(line)
		out.write(line)


	para.close()
	out.close()


if __name__=="__main__":
    main()
