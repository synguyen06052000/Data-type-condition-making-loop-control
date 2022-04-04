import string
class KiemTraThuanNghich:
    def __init__(self,st):
        self.m_s = st
    def check(self):
        S = self.m_s
        for i in range(0,int(len(S)/2)):
            if(S[i]!=S[len(S)-i-1]):
                return("Khong la so thuan nghich")
        return("La so thuan nghich")
if __name__ == "__main__":
    mS = (input("Nhap so nguyen N: "))
    kiemTra = KiemTraThuanNghich(mS)
    print(mS,kiemTra.check())