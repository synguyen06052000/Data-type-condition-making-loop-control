from re import A


class NgToCungNhau:
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b
    def UCLN(self,x,y):
        while(x!=y):
            if(x>y):
                x -= y
            else:
                y -= x
        return x
    def check(self):
        if(self.UCLN(self.num1,self.num2)==1):
            return("la hai so nguyen to cung nhau")
        else:
            return("khong la nguyen to cung nhau")
if __name__=="__main__":
    number1 = (int)(input("Nhap so thu nhat: "))
    number2 = (int)(input("Nhap so thu hai: "))
    ngto = NgToCungNhau(number1,number2)
    print("Hai so vua nhap:",ngto.check())
        