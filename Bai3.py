class Sum:
    def __init__(self,n):
        self.n = n
    def tong(self):
        result = 0
        for i in range(1,self.n+1):
            result += (1/i)
        return round(result,4)
if __name__ == "__main__":
    N = (int)(input("Nhap so N: "))
    sum = Sum(N)
    print("Tong tinh toan duoc la: ",sum.tong())
    