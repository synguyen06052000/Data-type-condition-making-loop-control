class Pi:
    def __init__(self,c):
        self.m_c = c
    def tong (self):
        i = 0 
        s = 0
        g = 1.00000
        while(g >= self.m_c):
            g = round((1.0 / (2*i+1)),4)
            s = round((s + pow(-1,i)*g),4)
            i += 1
        return float(4*s)
if __name__ == "__main__":
    x = (float)(input("Nhap so c: "))
    pi = Pi(x)
    print("So pi tinh toan duoc la:",pi.tong())
    