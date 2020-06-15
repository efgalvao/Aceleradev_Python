from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the 'Solfi APi'  index.")

def solfi(request):
    return HttpResponse("Olá Mundo. Assim se cria uma página?")

def _ordenar(numbers):
    out = []
    nums = list(set([(a, numbers.count(a)) for a in numbers]))
    nums.sort(key=itemgetter(0), reverse=True)
    nums.sort(key=itemgetter(1))
    nums.reverse()
    print(nums)
    for n in nums:
        counter = n[1]
        while counter > 0:
            out.append(n[0])
            counter -= 1
    return out


def lambda_function(request):

    pass
