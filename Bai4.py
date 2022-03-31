class SumN:
    def __init__(self,n):
        self.so_N = n
    def sum_N(self):
        s = 0
        for i in range(1,self.so_N):
            s+=i
        return s
    def sum_le_N(self):
        s1 = 0
        for i in range(1,self.so_N):
            if((i%2)!=0):
                s1+=i
        return s1
    def sum_chan_N(self):
        s2 = 0
        for i in range(1,self.so_N):
            if((i%2)==0):
                s2+=i
        return s2
if __name__=="__main__":
    N = (int)(input("Nhap so N:"))
    sumN = SumN(N)
    print("Tong so tu nhien khong qua N la S=",sumN.sum_N())
    
    print("Tong so tu nhien le khong qua N la S1=",sumN.sum_le_N())
 
    print("Tong so tu nhien chan khong qua N la S2=",sumN.sum_chan_N())
    