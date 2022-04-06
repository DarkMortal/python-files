import datetime

subjects={
    "Sangeeta Mam":("CS402","DSA"),
    "Sraboni Mam":("CS403","Automata"),
    "Anup Thander Sir":("M(CSE)401","Maths"),
    "Arnab Sir":("MC401","Economics"),
    "Mahmuda Sultana Mam":("CS401","Computer Architecture")
}
practicals={
    "Sangeeta Mam":("CS492","DSA Practical"),
    "Anup Thander Sir":("M(CSE)491","Maths Practical"),
    "Mahmuda Sultana Mam":("CS491","Computer Architecture")
}
routine={
    "Monday":[subjects["Arnab Sir"]],
    "Tuesday":[subjects["Arnab Sir"],subjects["Anup Thander Sir"],subjects["Sangeeta Mam"],practicals["Mahmuda Sultana Mam"]],
    "Wednesday":[subjects["Mahmuda Sultana Mam"],subjects["Sraboni Mam"],subjects["Anup Thander Sir"],subjects["Arnab Sir"]],
    "Thursday":[practicals["Sangeeta Mam"],subjects["Sraboni Mam"],subjects["Arnab Sir"]],
    "Friday":[subjects["Sangeeta Mam"],subjects["Mahmuda Sultana Mam"],practicals["Anup Thander Sir"]]
}

Teachers=list(subjects.keys())
Subjects=list(subjects.values())

P_Teachers=list(practicals.keys())
P=list(practicals.values())

def dates(d1,d2):
    date={}
    x=d1
    y=d2+datetime.timedelta(days=1)
    while x!=y:
        try:
            for i in routine[x.strftime("%A")]:
                try:
                    t=(Teachers[Subjects.index(i)],"Subject")
                except ValueError:
                    t=(P_Teachers[P.index(i)],"Practical")
                try:
                    date[t].append(x.strftime("%d/%m/%Y"))
                except KeyError:
                    date[t]=[x.strftime("%d/%m/%Y")]
        except:
            pass
        x+=datetime.timedelta(days=1)
    return date

if __name__=="__main__":
    start=datetime.datetime(2022,3,14)
    end=datetime.datetime(2022,4,1)
    data=dates(start,end)
    classes=[(teacher[0],data[teacher]) for teacher in data.keys() if teacher[1]=="Subject"]
    practical=[(teacher[0],data[teacher]) for teacher in data.keys() if teacher[1]=="Practical"]
    print("Classes\n")
    for i in classes:
        print(i[0])
        for j in i[1]:
            print(j)
        print("\n")
    print("Practicals\n")
    for i in practical:
        print(i[0])
        for j in i[1]:
            print(j)
        print("\n")