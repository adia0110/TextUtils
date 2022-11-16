# i have created this file-aditya
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1>hello</h1>''')

# def about(request):
#     return HttpResponse('''about hello<a href="https://www.youtube.com/watch?v=2tWRmToaesk&list=RD2tWRmToaesk&start_radio=1">Dino</a>''')



def index(request):
    params={'name':'harry','place':'mars'}
    return render(request,'index.html',params)
   # return HttpResponse("Home")

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newline = request.GET.get('newline','off')
    extraspacereover = request.GET.get('extraspacereover','off')
    # print(removepunc)
    # print(djtext)
    # # analyzed=djtext
    punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    analyzed=""
    if removepunc=="on":
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params={'purpose':'remove punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif fullcaps=="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params={'purpose':'remove punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    elif newline=="on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed+char
        params={'purpose':'removed newline','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif extraspacereover=="on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed+char
        params={'purpose':'extraspace','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")
# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remove first")

# def spaceremover(request):
#     return HttpResponse("space remover <a href='/'>back</a>")

# def charcount(request):
#     return HttpResponse("charcoun")


