# Self Made file

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    gettext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == 'on':
        analyzed = removePunc(gettext)
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        gettext = analyzed

    if uppercase == 'on':
        analyzed = upperCase(gettext)
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        gettext = analyzed

    if newlineremove == 'on':
        analyzed = newLineremove(gettext)
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        gettext = analyzed

    if spaceremove == 'on':
        analyzed = spaceRemove(gettext)
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        gettext = analyzed

    if charcount == 'on':
        analyzed = charCount(gettext)
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}

    if removepunc != 'on' and uppercase != 'on' and newlineremove != 'on' and spaceremove != 'on' and charcount != 'on':
        return HttpResponse("Please Tick the check box and try again")

    return render(request, 'analyze.html', params)


def removePunc(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ''
    for char in text:
        if char not in punctuations:
            analyzed = analyzed + char
    return analyzed


def upperCase(text):
    analyzed = ''
    for char in text:
        analyzed = analyzed + char.upper()
    return analyzed


def newLineremove(text):
    analyzed = ''
    for char in text:
        if char != '\n' and char != '\r':
            analyzed = analyzed + char
    return analyzed


def spaceRemove(text):
    analyzed = ''
    for char in text:
        if ' ' == char:
            pass
        else:
            analyzed = analyzed + char
    return analyzed


def charCount(text):
    return len(text)
