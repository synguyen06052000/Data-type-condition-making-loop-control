class HaiSoNguyen:
    def __init__(self,a,b):
        self.number1 = a
        self.number2 = b
    def UCLN(self):
        num1 = self.number1
        num2 = self.number2
        while(num1 != num2):
            if(num1 > num2):
                num1 -= num2
            else:
                num2 -= num1
        return num1
    def BCNN(self):
        return (self.number1*self.number2)/(self.UCLN())
if __name__ == "__main__":
    a = (int)(input("Nhap so nguyen thu nhat:"))
    b = (int)(input("Nhap so nguyen thu hai:"))
    haiSo = HaiSoNguyen(a,b)
    print("UCLN:",haiSo.UCLN())
    print("BCNN:",int(haiSo.BCNN()))
    