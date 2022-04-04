class UocSo:
    def __init__(self,n):
        self.so_N = n
    def Uoc(self):
        count = 0
        for i in range(1,self.so_N+1):
            if(self.so_N%i==0):
                count+=1
                print(i,end=" ")
        print("\nSo cac uoc cua N",count) 
                
if __name__=="__main__":
    N = (int)(input("Nhap so nguyen N:"))
    uocSo = UocSo(N)
    print("Liet ke cac uoc cua N:")
    uocSo.Uoc()