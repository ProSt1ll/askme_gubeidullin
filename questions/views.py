from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "index.html", {'questions':content})
questions = [{
    "title": f"Title {i+1}",
    "text": f"This is text for {i+1} question",
    "number": i,
} for i in range(100)
]
def sign_in(request):
    return render(request, "sign_in.html", {})

def question(request,number):
    return render(request, "question.html", {question(number)})

def registration(request):
    return render(request, "registration.html", {})
