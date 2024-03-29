import os
filePath = os.path.join(os.getcwd(), "../Files", "Text.txt")

if __name__ == "__main__":
    try:
        file = open(filePath, 'r')
        #file.seek(n) puts file put pointer at n

        # reading the file line by line
        contents = file.readline()
        while contents:
            print(contents)
            contents = file.readline()
        file.close()

        # reading the file ad once
        print(file.read())

    except FileNotFoundError:
        file = open(filePath, 'w')
        file.write("What's the matter clown?\n" +
                   "Are you angry, humiliated, is that it?\n" +
                   "Fool, you don't know what humiliation is.")
        file.flush()
        file.close()
        print("File was generated")

        with open(filePath, 'r') as fileRead:
            print(fileRead.read())
    
    except Exception:
        print(
            "There was some error.\nMake sure you have proper write priviledges to the File"
        )