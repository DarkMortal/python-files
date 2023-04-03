class Warrior:

    def __init__(self, power):
        try:
            self.powerLevel = int(power)
        except:
            raise TypeError("Expected Integer got String")

    def disp(self):
        if self.powerLevel <= 9000:
            return "Pathetically Weak"
        else:
            return "It's over 9000!!!"


class Saiyan(Warrior):

    def __init__(self, power, age, name, gender):
        try:
            super().__init__(power)  #Initialsing super(parent) class
            self.name = name
            self.age = int(age)
            self.gender = gender
        except TypeError as t:
            raise Exception(t)


if __name__ == "__main__":
    try:
        goku = Saiyan("10000", "40", "Kakarot", "male")
        value = goku.disp() if goku.disp() == Warrior.disp(
            goku) else "No value Found"
        print(value)
        goku = Saiyan("100+00", "40", "Kakarot",
                      "male")  # will print 'Expected Integer got String'
        #goku=Saiyan("10000","4+0","Kakarot","male") will print 'invalid literal for int() with base 10: '4+0''
    except Exception as e:
        print(e)

'''Output
It's over 9000!!!
Expected Integer got String'''