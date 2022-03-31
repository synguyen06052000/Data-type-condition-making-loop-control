class PhanTichNgTo:
    def __init__(self,n):
        self.so_N = n
    def phanTich(self):
        result = self.so_N
        for i in range (2,self.so_N+1):
            while(result % i ==0):
                print(i,end=" ")
                result = result/i
if __name__=="__main__":
    N = (int)(input("Nhap so nguyen N: "))
    problem = PhanTichNgTo(N)
    print("So N phan tich ra thua so nguyen to:",end=" ")
    problem.phanTich()
