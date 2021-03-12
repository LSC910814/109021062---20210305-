class Hero:
    def __init__(self, name, tacticalskill, passiveskill, trick, age): 
        self.heroName= name
        self.heroTacticalSkill= tacticalskill
        self.heroPassiveSkill= passiveskill
        self.heroTrick= trick
        self.heroAge= age
    def showinfo(self):
        print(self.heroName)
        print(self.heroTacticalSkill)
        print(self.heroPassiveSkill)
        print(self.heroTrick)
        print(self.heroAge)
x1=Hero("尋血犬","上帝之眼","追蹤器","狩獵野獸","未知")
x2=Hero("直布羅陀","保護圓頂","槍盾","防禦性轟炸","30")
x3=Hero("生命線","D.O.C.治療機器人","戰鬥醫療兵","照護艙","24")

x1.showinfo()
x2.showinfo()
x3.showinfo()
