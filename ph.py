

class Hesabla:
    def method1(self):
        return [2, 7, 9, 10, 6]
    
    def method2(self):
        hedef_reqem = 3
        mylist = self.method1() 
        for i in range(len(mylist)):
            for j in range(i + 1, len(mylist)):
                if mylist[i] + mylist[j] == hedef_reqem:
                    print("Hedef reqeme beraber olan ededlerin indexi:", (i, j))
                    return
        else:
            
            print(-1)
            return 

netice = Hesabla()
netice.method2()
          