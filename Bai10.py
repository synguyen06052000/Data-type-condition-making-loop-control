import math
class NSoNgTo:
    def __init__(self,n):
        self.so_N = n
    def check_Ngto(self,x):
        if(x < 2):
            return 0
        can_X = (int)(math.sqrt(x))
        for i in range(2,can_X+1):
            if(x % i == 0):
                return 0
        return 1
    def lietKe(self):
        dem = 0
        i = 2
        while (dem < self.so_N):
            if(self.check_Ngto(i)):
                print(i,end=" ")
                dem += 1
            i += 1
        
if __name__=="__main__":
    N = (int)(input("Nhap so nguyen N: "))
    n_SoNguyenTo = NSoNgTo(N)
    print(N, "so nguyen dau tien:",end=" ")
    n_SoNguyenTo.lietKe()
    