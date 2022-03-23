if __name__=="__main__":
    try:
        file=open("./Files/Text.txt",'r')
        #file.seek(n) puts file put pointer at n
        contents=file.readline()
        while contents:
            print(contents)
            contents=file.readline()
        file.close()
    except FileNotFoundError:
        file=open("./Files/Text.txt",'w')
        file.write("What's the matter clown?\n"+
        "Are you angry, humiliated, is that it?\n"+
        "Fool, you don't know what humiliation is.")
        file.flush()
        file.close()
        print("File was generated")
    except:
        print("There was some error.\nMake sure you have proper write priviledges to the File")