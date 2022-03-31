class HCN_Rong:
    def __init__(self,n,m):
        self.chieu_dai = n
        self.chieu_rong = m
    def printHCNRong(self):
        for i in range(0,self.chieu_rong):
            for j in range(0,self.chieu_dai):
                if ((i==0) or (j==0) or (i==self.chieu_rong-1) or (j==self.chieu_dai-1)):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print(end="\n")
if __name__=="__main__":
    dai = (int)(input("Nhap chieu dai: "))
    rong = (int)(input("Nhap chieu rong: "))
    hcn = HCN_Rong(dai,rong)
    hcn.printHCNRong()