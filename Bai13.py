import math


class ChinhPhuong:
    def __init__(self,m,n):
        self.so_M = m
        self.so_N = n
    def CheckChinhPhuong(self,a):
        if (a==0):
            return 0
        else:
            can_A = (int)(math.sqrt(a))
            if (can_A*can_A == a):
                return 1
            else:
                return 0
    def LietKeChinhPhuong(self):
        for i in range(self.so_M,self.so_N+1):
            if(self.CheckChinhPhuong(i)):
                print(i,end=" ")
if __name__ == "__main__":
    M = (int)(input("Nhap so M = "))
    N = (int)(input("Nhap so N = "))
    so = ChinhPhuong(M,N)
    print("So chinh phuong trong doan [m,n]:",end=" ")
    so.LietKeChinhPhuong()
    
        