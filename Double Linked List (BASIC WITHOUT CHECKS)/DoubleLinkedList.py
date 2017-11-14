class LinkedList:
    data = 0

    def __init__(self, data):
        self.next = None
        self.data = data
        self.back = None

class Main:
    def __init__(self):
        self.first = None
        self.cur = None
        self.pre = None
        self.last = None

    # MENU TO HANDLE ALL THE OPTIONS
    def menu(self):
        flag = True
        while (flag):
            choice = int(input(""" ====> MENU <==== 
                   1. ADD NODE
                   2. PRINT DATA FROM NODE (Left -> Right)
                   3. PRINT DATA FROM NODE (Right -> Left)
                   4. MODIFY DATA IN NODE
                   5. DELETE NODE
                   6. Exit
                   Enter Your Choice: """))
            if (choice == 1):
                self.addnode()
            elif (choice == 2):
                self.showdata()
            elif (choice == 3):
                self.showbackward()
            elif (choice == 4):
                self.modifydata()
            elif (choice == 5):
                self.deletenode()
            elif (choice == 6):
                flag = False

                # ADDING DATA TO NODE!

    def addnode(self):
        # Later to be Broken to Top Mid and Last Insertion
        ch = "y"
        while (ch == 'y'):
            data = input("Enter Data for Node: ")
            self.cur = LinkedList(data)

            if (self.first == None):
                self.first = self.pre = self.cur
            else:
                self.pre.next = self.cur
                self.cur.back = self.pre
                self.pre = self.cur
                self.last = self.cur
            ch = input("Do You Want to Add More Nodes? \n y for Yes \n n for No \n Enter Choice: ")

            # TRAVERSE DATA FROM LIST

    def showdata(self):
        self.cur = self.first
        while (self.cur != None):
            print("Data is: " + str(self.cur.data))
            self.cur = self.cur.next

    def showbackward(self):
        self.cur = self.last
        while (self.cur != None):
            print("Data is: " + str(self.cur.data))
            self.cur = self.cur.back
            # MODIFYING DATA OF NODE

    def modifydata(self):
        self.cur = self.first
        data = input("Enter Data of the Node You Wish to Change: ")

        while (self.cur != None and self.cur.data != data):
            self.cur = self.cur.next

        if (self.cur != None):
            print("Current Data of Node: " + str(self.cur.data))
            data = input("Enter Updated Data: ")
            self.cur.data = data
        else:
            print("The Data is not Found in the List!")

            # DELETING DATA FROM NODE!

    def deletenode(self):
        self.cur = self.first
        data = input("Enter the Data of the Node You Want to Delete: ")

        while (self.cur != None and self.cur.data != data):
            self.pre = self.cur
            self.cur = self.cur.next

        if (self.cur != None):
            self.pre.next = self.cur.next
            self.cur = self.cur.next
            self.cur.back = self.pre
        else:
            print("The Data is not Found in the List!")


obj = Main()
obj.menu()