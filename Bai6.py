class UocSo:
    def __init__(self,n):
        self.so_N = n
    def dem_So_Uoc(self):
        count = 0
        for i in range(1,self.so_N+1):
            if(self.so_N%i==0):
                count+=1
        return count
    def liet_Ke_Uoc(self):
        for i in range(1,self.so_N+1):
            if(self.so_N%i==0):
                print(i,end=" ")
if __name__=="__main__":
    N = (int)(input("Nhap so nguyen N:"))
    uocSo = UocSo(N)
    print("Tong so uoc cua N:",uocSo.dem_So_Uoc())
    print("Liet ke cac uoc cua N:",end=" ")
    uocSo.liet_Ke_Uoc()