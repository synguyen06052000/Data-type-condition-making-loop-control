class Sum:
    def __init__(self,n):
        self.so_N = n
    def sum_N(self):
        result = 0
        for i in range(1,self.so_N):
            if((i%7)==0):
                result+=i
        return result
if __name__ == "__main__":
    N = (int)(input("Nhap so N="))
    sumN = Sum(N)
    print("Tong so tu nhien khong qua N va chia het cho 7=",sumN.sum_N())
    