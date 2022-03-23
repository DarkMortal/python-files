dictionary={
    "Naruto Uzumaki":("6290436310","Genin","Konoha"),
    "Sasuke Uchiha":("9836099827","Genin","Konoha"),
    "Sakura Haruno":("9051634859","Jonin","Konoha"),
    "Kakashi Hatake":("7439302254","Jonin","Konoha")
}

def firstName(name):
    return name[:name.index(' ')]

if __name__=="__main__":
    name=str(input("Enter the name of the person whose details ypu want to know : \n"))
    while name != "":
        if name in dictionary.keys() or name in list(map(firstName,dictionary.keys())):
            try:
                print(f"\nPhone number : {dictionary[name][0]}\nVillage : {dictionary[name][2]}\nRank : {dictionary[name][1]}")
            except KeyError:
                print("Please Enter Full Name")
        else:
            opt=str(input("\nMember not Found\nWould you like to add it? (Y/N) : "))[0]
            if opt =='Y' or opt=='y':
                phone=str(input("Enter the Phone Number : "))
                rank=str(input("Enter Rank : "))
                village=str(input("Enter Village : "))
                dictionary[name]=(phone,rank,village)
        name=str(input())