if __name__=="__main__":
    try:
        file1=open("./Files/File1.xml",'r')
        file2=open("./Files/File2.xml",'w')
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