import string
class KiemTraThuanNghich:
    def __init__(self,st):
        self.s = st
    def check(self):
        String = self.s
        for i in range(0,len(String)):
            if(String[i]!=String[len(String)-i-1]):
                return("Khong la so thuan nghich")
            if i >= (len(String)/2):
                return("La so thuan nghich")
if __name__ == "__main__":
    N = (input("Nhap so nguyen N: "))
    kiemTra = KiemTraThuanNghich(N)
    print(N,kiemTra.check())