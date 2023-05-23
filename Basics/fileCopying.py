import os

filePath1 = os.path.join(os.getcwd(), "../Files", "File1.xml")
filePath2 = os.path.join(os.getcwd(), "../Files", "File2.xml")

if __name__ == "__main__":
    try:
        with open(filePath1, 'r') as file1:
            with open(filePath2, 'w') as file2:
                for line in file1.readlines():
                    #s=line.rstrip() #removes trailing whitespace at the end of line
                    #rstrip=strip from right
                    #lstrip=strip from left
                    #strip=strip from both sides
                    file2.write(line)
                file2.flush()
                file2.close()
            file1.close()
            print("File saved successfully")
    except FileNotFoundError:
        print("File not found")
    except Exception:
        print(
            "There was some error.\nMake sure you have proper write priviledges to the File"
        )