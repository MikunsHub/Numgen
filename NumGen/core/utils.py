import pandas as pd

def rand(fixedvar1,fixedvar2,var1,var2,var3):
    res=[]
    for i in var1:
        for j in var2:
            for k in var3:
                if i < j and j < k:
                    res.append(fixedvar1*100000000 + fixedvar2*1000000 + i*10000 + j*100 + k)
    return res