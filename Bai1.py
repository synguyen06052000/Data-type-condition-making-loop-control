class Problem:
    def __init__(self,n):
        self.so_N = n
    def InSoLe(self):
        for i in range(0,self.so_N+1):
            if((i%2)!=0):
                print(i,end=" ")
    def InSoChan(self):
        for i in range(0,self.so_N+1):
            if((i%2)==0):
                print(i,end=" ")    
if __name__ == "__main__":
    print("Nhap so N:",end=" ")
    N = (int)(input())
    problem = Problem(N)
    print("So le nho hon N:")
    problem.InSoLe()
    print("\nSo chan nho hon N:")
    problem.InSoChan()