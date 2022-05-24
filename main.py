from zodiac import *


class Zodiac:

    def __init__(self, y, m, d):
        if y < 1583:
            print('EXCESS MINIMUM!!!')
        elif y > 3999:
            print('EXCESS MAXIMUM!!!')
        else:
            if m == 1:
                y = y-1
                m = 13
            elif m == 2:
                y = y-1
                m = 14
            self.y, self.m, self.d = y, m, d

    def i10w(self, i):
        wk = TEN_K[i-1]
        w = TEN[i-1]
        return [wk, w]
    
    def i12w(self, i):
        wk = TWV_K[i-1]
        w = TWV[i-1]
        return [wk, w]
        
    def zdc_y(self,):
        y10 = (self.y+7)%10
        y12 = (self.y+9)%12
        return list(zip(self.i10w(y10), self.i12w(y12)))
    
    def zdc_m(self,):
        m10 = (2*self.y+self.m+3)%10
        m12 = (self.m+1)%12 
        return list(zip(self.i10w(m10), self.i12w(m12)))
    
    def zdc_d(self,):
        c, n = int(str(self.y)[0:2]), int(str(self.y)[2:])
        d10 = (4*c+floor(c/4)+5*n+floor(n/4)+floor((3*self.m+3)/5)+self.d+7)%10
        d12 = (8*c+floor(c/4)+5*n+floor(n/4)+6*self.m+floor((3*self.m+3)/5)+self.d+1)%12
        return list(zip(self.i10w(d10), self.i12w(d12)))
    
    def display(self):
        return self.zdc_y(), self.zdc_m(), self.zdc_d()
    
    def display_k(self):
        return ''.join(self.zdc_y()[0])+'('+''.join(self.zdc_y()[1])+')'+'년, '+''.join(self.zdc_m()[0])+'('+''.join(self.zdc_m()[1])+')'+'월, '+''.join(self.zdc_d()[0])+'('+''.join(self.zdc_d()[1])+')'+'일'





if __name__ == '__main__':
    tm = localtime(time())
    print(tm.tm_year, tm.tm_mon, tm.tm_mday)
    test = Zodiac(tm.tm_year, tm.tm_mon, tm.tm_mday)
    print(test.display_k())