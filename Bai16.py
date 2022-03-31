class HCN:
    def __init__ (self,n,m):
        self.chieu_dai = n
        self.chieu_rong = m
    def printHCN(self):
        for i in range(0,self.chieu_rong):
            for j in range(0, self.chieu_dai):
                print("*",end=" ")
            print(end="\n")
            
if __name__ == "__main__":
    dai = (int)(input("Nhap chieu dai: "))
    rong = (int)(input("Nhap chieu rong: "))
    hcn = HCN(dai,rong)
    hcn.printHCN()
    