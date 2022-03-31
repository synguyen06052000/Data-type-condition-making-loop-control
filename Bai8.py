from cmath import sqrt


import math
class KiemTraSoNguyen:
    def __init__(self,n):
        self.so_N = n
    def check_Ngto(self):
        if(self.so_N < 2):
            return("khong la so nguyen to")
        count = 0 
        for i in range(1,self.so_N+1):
            if(self.so_N%i==0):
                count += 1
        if count == 2:
            return("la so nguyen to")
        else:
            return("khong la so nguyen to")
if __name__=="__main__":
    N = (int)(input("Nhap so nguyen N: "))
    kiemTra = KiemTraSoNguyen(N)
    print("N",kiemTra.check_Ngto())
    
        