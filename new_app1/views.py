from django.shortcuts import render

def test2(request):
    return render(request,"index.html")
def test1(request):
    return render(request,"template1.html")
