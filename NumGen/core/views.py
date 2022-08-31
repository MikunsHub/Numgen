from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from .utils import rand
import pandas as pd
import os


def index(request):
    
    if request.method == "POST":

        fixedVar1 = int(request.POST["Fixed Var 1"])
        fixedVar2 = int(request.POST["Fixed Var 2"])

        var1 = request.POST["Var 1"]
        temp = var1.split("-")
        print("temp",temp)
        var1 = [item for item in range(int(temp[0]),int(temp[1]))]
        print(var1[0])

        var2 = request.POST["Var 2"]
        temp = var2.split("-")
        var2 = [item for item in range(int(temp[0]),int(temp[1]))]
        print(var2[0])

        var3 = request.POST["Var 3"]
        temp = var3.split("-")
        var3 = [item for item in range(int(temp[0]),int(temp[1]))]
        print(var3[0])

        if var2[0] <= var1[0] or var3[0] <= var2[0]:
            print("worjmde")
            return render(request, 'core/result.html')
        
        df = pd.DataFrame({'combinations': rand(fixedVar1,fixedVar2,var1,var2,var3)})
        df.to_csv(r"C:\Users\HP PC\Documents\PersonalProjects\Numgen\NumGen\core\static\core\combinations.csv")
        return redirect('result')
        
    context = {}
    return render(request, 'core/index.html',context)

def result(request):
    file_location = r"C:\Users\HP PC\Documents\PersonalProjects\Numgen\NumGen\core\static\core\combinations.csv"
    return serve(request, os.path.basename(file_location), os.path.dirname(file_location))


