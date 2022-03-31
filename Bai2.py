class SumN:
    def __init__(self,n):
        self.so_N = n
    def Sum(self):
        result = 0
        for i in range(1,self.so_N+1):
            result+=i
        return result
if __name__ == "__main__":
    N = (int)(input("Nhap so tu nhien N:"))
    tong = SumN(N)
    print("Tong N so tu nhien:",tong.Sum())
    