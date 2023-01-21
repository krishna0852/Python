class UserAccount:
    dic={111:"admin"}
    li=[10,20,30]
    def users(self):
        self.inputs()
        if self.Userid==111 and self.passwd=='admin':
            print("Admin has access to see all the users")
            print(self.dic)
            
        else:
            print("the admin account details are incorrect ")
    def inputs(self):
         Userid=int(input("Enter the userid"))
         passwd=input("Enter the password")
         self.Userid=Userid
         self.passwd=passwd
    def login(self):
        self.inputs()
        for key in (self.dic.keys()):
            if key==self.Userid:
                if self.passwd==self.dic[key]:
                    print("you have access to view the data ")
                    self.operations()
                else:
                    print("your password is incorrect, please try again")
                    
            else:
                if self.Userid not in self.dic.keys():
                    print("not found")
                    break
                else:
                    continue
                
        #need to cross check the credentials 
    def createUser(self):
        self.inputs()
        self.dic.update({self.Userid:self.passwd})
        print("userid is created with ",self.Userid,"you can login now")
        print(self.dic)

        pass

    '''li=[10,20,30]  initially when i have declare list in operations method all the elements are added but when i try to reterive from 
       list it's not inserted because it will get destroyed after the method execution to overcome 
        that i have declare this in class level(it will store until the program execution 
        it will destroy once the program execution is completed) ..'''
    def operations(self):
        #li=[10,20,30]
        print("you have access here to insert and reterive the data to insert press 1 and to reterive press 4")
        inp=int(input("Enter your choice to insert or reterive"))
        if inp==1:
            len=int(input("how elemnts you need to enter"))
            print("please enter the items")
            for i in range(len):
                item=input()
                self.li.append(item)
            print("elements are inserted")
                
        else:
            print(self.li)

obj=UserAccount()
while(True):
    print("===========User-Accounts=============")
    print("need an user account to write the element in the list")
    print("Enter 1 to login with your credentials")
    print("Enter 2 to create user account ")
    print("if you want to see all the users enter 9  ONLY ADMIN CAN SEE THIS INFORMATION")
    inp=int(input("Enter your choice"))
    if inp==1:
        obj.login()
        continue
    elif inp==2:
        obj.createUser()
        continue
    elif inp==9:
        obj.users()
        continue
    else:
        print("you gave the wrong input please choose the correct one")
        continue
    break

