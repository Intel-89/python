# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------------------------------------

class Warehouse:
    def __init__(self,var_pur: str="default1",var_reg: str="default2"):
        self.mypurpose=var_pur
        self.myregion=var_reg
    def atest(self):
        print(self.mypurpose," ",self.myregion)
    

w1 = Warehouse()
print(w1.mypurpose, w1.myregion)

w2 = Warehouse("test1","test")
#w2.myregion = 'var_change'
print(w2.mypurpose, w2.myregion)
print(w1.mypurpose, w1.myregion)
w1.atest()

#------------------------------------------------------------------------------------------------------------

