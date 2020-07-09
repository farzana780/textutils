from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get("newlineremover", 'off')
    extraspaceremover = request.POST.get("extraspaceremover", 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        a = {'purpose': 'removed punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, "analyze.html", a)
    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        a = {'purpose': 'Capitalized', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, "analyze.html", a)

    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        a = {'purpose': 'new line removed', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, "analyze.html", a)

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
        a = {'purpose': 'extra space removed', 'analyzed_text': analyzed}


    return render(request, "analyze.html", a)

