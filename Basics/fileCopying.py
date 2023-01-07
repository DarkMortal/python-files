import os

filePath1 = os.path.join(os.getcwd(), "../Files", "File1.xml")
filePath2 = os.path.join(os.getcwd(), "../Files", "File2.xml")

if __name__=="__main__":
    try:
        file1=open(filePath1,'r')
        file2=open(filePath2,'w')
        for line in file1.readlines():
            #s=line.rstrip() #removes trailing whitespace at the end of line
            #rstrip=strip from right 
            #lstrip=strip from left
            #strip=strip from both sides
            file2.write(line)
        file1.close()
        file2.flush()
        file2.close()
        print("File saved successfully")
    except FileNotFoundError:
        print("File not Found")