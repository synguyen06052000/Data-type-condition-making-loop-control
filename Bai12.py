class TongChuSo:
    def __init__(self,st):
        self.s = st
    def tongChuSo(self):
        sum = 0
        for i in range(0,len(self.s)):
            sum += (int(self.s[i]))
        return sum
if __name__ == "__main__":
    N = input("Nhap so N: ")
    tong = TongChuSo(N)
    print("Tong chu so cua so N =",tong.tongChuSo())