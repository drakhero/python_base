class Person:
    def __init__(self,name,age,):
        self.name = name
        self.age = age
        self.money = 0
        self.skill = []

    def teach(self,sb,skill):
        sb.skill.append(skill)
        print(self.name,'教',sb.name,'学',skill)

    def work(self,money):
        self.money += money
        print(self.name,'上班赚了',money,'元')

    def borrow(self,sb,money):
        if self.money > money:
            self.money -= money
            sb.money += money
            print(sb.name,'向',self.name,'借了',money,'元')
        else:
            print(self.name,'没有借钱给',sb.name)

    def show_info(self):
        print(self.age, '岁的', self.name, '有钱', self.money, '元',
              '它学会的技能：', ','.join(self.skill))


zs = Person('张三',35)
ls = Person('李四',8)
zs.teach(ls,'python')
zs.teach(ls,'java')
ls.teach(zs,'王者荣耀')
zs.work(1000)
zs.borrow(ls,999)
zs.show_info()
ls.show_info()
