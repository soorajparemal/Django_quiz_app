from django.shortcuts import render
from .models import main
# Create your views here

def main_page(request):
    quiz=main.objects.all()
    context={'quiz':quiz}
    return render(request ,'master/mainpage.html',context)

def result_page(request):
    quiz=main.objects.all()
    score=0

    for quizes in quiz:
        right=quizes.answer
        entered=request.POST.get(str(quizes.id))
        if(right==entered):
            score += 1
    context={'score':score}
    return render(request,'master/result.html',context)

