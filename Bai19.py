class TamGiacCan:
    def __init__(self,h):
        self.chieu_cao = h
    def printTGCan(self):
        for i in range(1,self.chieu_cao+1):
            for j in range(1,2*self.chieu_cao):
                if(abs(self.chieu_cao-j) <= (i-1)):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("\n")
if __name__ =="__main__":
    cao = (int)(input("Nhap chieu cao h: "))
    tamgiac = TamGiacCan(cao)
    tamgiac.printTGCan()