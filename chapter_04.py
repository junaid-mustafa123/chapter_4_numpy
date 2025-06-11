import numpy as np
class Practice:  
    def __init__(self):
        self.mynp=None

    def welcome(self):
        print("_______________________________________________________")  
        print("            WELCOME TO NUMPY LIBRARY")
        print("_______________________________________________________")   

    def op(self):
        print("""
_______________________________________________________________________
              OPERATION PANEL
_______________________________________________________________________
              1️⃣ . RESHAPE 
              2️⃣ . INSERT
              3️⃣ . APPEND
              4️⃣ . CONCATENATE
              5️⃣ . DELETE
              6️⃣ . STACKING
              7️⃣ . SPLITTING  
_______________________________________________________________________
""")   
    def  fun1(self,arr,r,c):
        self.mynp=np.array(arr)
        new = self.mynp.reshape(r,c)
        print("____________________________________")
        print("AFTER RESHAPE : ",new)
        print("_____________________________________")

    def fun2(self,a1,a2):
        self.mynp=np.array([a1,a2])
        print("____________________________________")
        print("RAVEL : ",self.mynp.ravel())
        print("-----------------------------------")
        print("FLATTEN : ",self.mynp.flatten())
        print("____________________________________")
        
    def fun3(self,arr,ind,value):
        self.mynp=np.array(arr)
        print("______________________________________")
        print("BEFORE",self.mynp)
        print("______________________________________")
        new=np.insert(arr,ind,value)
        print("AFTER : ",new)
        print("________________________________________")
    def fun4(self,a1,a2,ind,value):
        self.mynp=np.array([a1,a2])
        print("_______________________________________")
        print(self.mynp)
        print("_______________________________________")
        new = np.insert(self.mynp,ind,value,axis=0)
        print(new)
        print("_______________________________________")
        
    def fun5(self,a1,v):
        self.mynp=np.array(a1)
        print("____________________________")
        print(self.mynp)
        print("_____________________________")
        new = np.append(a1,v)
        print(new)
        print("_____________________________")

    def fun6(self,a1,a2):
        print(a1)
        print(a2)
        self.mynp=np.concatenate((a1,a2),axis=0)
        print("________________________________________")
        print(self.mynp)
        print("________________________________________")
    def fun7(self,arr,ind):
        self.mynp=np.array(arr)
        print(self.mynp)
        print("____________________________________________")
        new = np.delete(arr,ind,axis=None)
        print(new)
        print("_________________________________________")

    def fun8(self,a1,a2,ind):
        self.mynp=np.array((a1,a2)) 
        print("______________________________________")
        print(self.mynp)
        new=np.delete(self.mynp,ind,axis=0)
        print("_______________________________________")
        print(new)
        print("_________________________________________")   

    def fun9(self,a1,a2):
        self.mynp=np.array((a1,a2))
        print(self.mynp)
        print("_______________________________") 
        new = np.hstack((a1,a2))
        print(new)
        print("___________________________________")  

    def fun10(self,a1,a2):
        print("_______________________________") 
        new = np.vstack((a1,a2))
        print(new)
        print("___________________________________")  

    def fun11(self, arr, parts):
        print("_________________________________")
        self.mynp=np.array(arr)
        print(self.mynp)
        new = np.split(self.mynp,parts)
        print(new)
f1=Practice()
while True:
    f1.welcome()
    f1.op()
    choice = int(input("SELECT OPTION (1 to 7) : "))
    if choice == 1:
        print("""
    _____________________________________________________________
            RESHAPE : MEANS BREAKING INTO ROWS AND COLUMNS (1d into 2d)  # [SPELLING FIX] 'COLUMS' to 'COLUMNS'
            1.1D ARRAY (into 2d)
            2.2D ARRAY (into 1d)
    _____________________________________________________________          
    """)
        s = int(input("SELECT OPTION (1 TO 2) : "))
        if s ==1:
            arr = [1,2,3,4,5,6]
            r = int(input("ENTER ROWS : "))
            c = int(input("ENTER COLUMNS : "))
            f1.fun1(arr,r,c)
        elif s==2:
            print("""
    ______________________________________________________________________
                1.RAVEL() RETURN VIEW AND DISTURB ORIGINAL   # [SPELLING FIX] 'DISTRUB' to 'DISTURB', 'ORIGIBNAL' to 'ORIGINAL'
                2.FLATTEN() RETURN VIEW AND DON'T DISTURB 
    ______________________________________________________________________
    """)
            a1=[1,2,3]
            a2=[4,5,6]
            f1.fun2(a1,a2)
        else:
            print("❌SELECT VALID CHOICE")  
    elif choice == 2:
        print("_____________________________________________________")
        print("""INSERT : ADDING ELEMENT TO A SPECIFIC INDEX  # [SPELLING FIX] 'ADDIND' to 'ADDING', 'SPECFIC' to 'SPECIFIC'
            1.1D ARRAY 
            2.2D ARRAY""")
        print("_____________________________________________________")
        s = int(input("SELECT OPTION (1 TO 2) : "))
        if s==1:
            ar = [1,2,3,4,5,6]
            ind = int(input("ENTER THE INDEX : "))  
            value = int(input("ENTER THE VALUE : "))  
            f1.fun3(ar,ind,value)
        elif s==2:
            a1=[1,2]
            a2=[3,4]
            ind = int(input("ENTER THE INDEX : ")) 
            value = [5,6]
            f1.fun4(a1,a2,ind,value)
        else:    
            print("❌SELECT VALID CHOICE") 
        
    elif choice == 3:
        print("_____________________________________________________")
        print("APPEND : MEANS ADDING ELEMENT AT THE END") 
        print("_____________________________________________________")
        arr=[1,2,3,4,5]
        value = int(input("ENTER THE VALUE WHICH YOU WANT TO APPEND : "))
        f1.fun5(arr,value)
        
    elif choice == 4:
        print("_____________________________________________________")
        print("CONCATENATE : MEANS ADDING TWO ARRAYS")
        print("_____________________________________________________")
        a1=[1,2,3]
        a2=[4,5,6]
        f1.fun6(a1,a2)

    elif choice == 5:
        print("_____________________________________________________")
        print("""DELETE(): REMOVING ELEMENT OF AN ARRAY  # [SPELLING FIX] 'ELEMET' to 'ELEMENT', 'ARRARY' to 'ARRAY'
            1.1D ARRAY 
            2.2D ARRAY """)
        print("_____________________________________________________")
        s = int(input("SELECT OPTION (1 TO 2) : "))
        if s==1:
            arr=[1,2,3,4,5,6,7,8,9,10]
            print(arr)
            ind = int(input("ENTER THE INDEX WHICH YOU WANT TO DELETE : "))
            f1.fun7(arr,ind)
        elif s==2:
            a1=[1,2]
            a2=[3,4]
            print(a1)
            print(a2)
            ind = int(input("ENTER THE INDEX WHICH YOU WANT TO DELETE : "))
            f1.fun8(a1,a2,ind)
        else:
            print("❌SELECT VALID CHOICE")     
    elif choice == 6:
        print("""STACKING : MEANS ADDING ARRAY ROW-WISE AND COLUMN-WISE  # [SPELLING FIX] 'ADDIND' to 'ADDING'
            1.hstack() HORIZONTAL  # [SPELLING FIX] 'HORIZANTAL' to 'HORIZONTAL'
            2.vstack () VERTICAL""")
        s = int(input("SELECT OPTION (1 TO 2) : "))
        if s==1:
            a1=[1,2,3]
            a2=[3,4,5]
            f1.fun9(a1,a2)
        elif s==2:
            a1=[1,2,3]
            a2=[3,4,5]
            print(a1)
            print(a2)
            f1.fun10(a1,a2)
        else:
            print("❌SELECT VALID CHOICE")
        pass
    elif choice ==7:
        print("___________________________________")
        print("SPLITTING : MEANS DIVIDING INTO PARTS")  
        print("___________________________________")
        arr = [1,2,3,4,5,6,7,8,9,10]
        print(arr)
        p = int(input("ENTER THE NUMBER OF PARTS TO SPLIT INTO: "))
        f1.fun11(arr,p)
    else:
        print("❌SELECT VALID CHOICE") 

    try:
        again = input("DO YOU WANT TO CONTINUE (YES/NO) : ").lower()
        if again=="yes":
            continue
        elif again=="no":
            break
        else:
            print("❌SELECT VALID CHOICE")
    except ValueError as e:
        print("ERROR :",e)
