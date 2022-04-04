from cmath import sqrt


import math
class KiemTraSoNguyen:
    def __init__(self,n):
        self.so_N = n
    def check_Ngto(self):
        if(self.so_N < 2):
            return("khong la so nguyen to")
        can_N = (int)(math.sqrt(self.so_N))
        for i in range(2,can_N+1):
            if(self.so_N % i == 0):
                return("khong la so nguyen to")
        return("la so nguyen to")
if __name__=="__main__":
    N = (int)(input("Nhap so nguyen N: "))
    kiemTra = KiemTraSoNguyen(N)
    print("N",kiemTra.check_Ngto())
    
        