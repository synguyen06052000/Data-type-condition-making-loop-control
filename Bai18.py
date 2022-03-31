class TGVuongCan:
    def __init__(self,h):
        self.chieu_cao = h
    def printTG(self):
        for i in range(0,self.chieu_cao):
            for j in range(0,self.chieu_cao):
                if(i>=j):
                    print("*",end=" ")
            print(end="\n")
if __name__ == "__main__":
    cao = (int)(input("Nhap chieu cao: "))
    tamgiac = TGVuongCan(cao)
    tamgiac.printTG()
        