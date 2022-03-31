import math
from tabnanny import check
class NSoNgTo:
    def __init__(self,n):
        self.so_N = n
    def check(self,a):
        if (a<2):
            return 0
        count = 0
        for i in range (1,a+1):
            if(a%i==0):
                count += 1
        if count == 2:
            return 1
        else:
            return 0
    def lietKe(self):
        dem = 0
        i = 2
        while (dem < self.so_N):
            if(self.check(i)):
                print(i,end=" ")
                dem += 1
            i += 1
        
if __name__=="__main__":
    N = (int)(input("Nhap so nguyen N: "))
    n_SoNguyenTo = NSoNgTo(N)
    print("N so nguyen dau tien:",end=" ")
    n_SoNguyenTo.lietKe()
    