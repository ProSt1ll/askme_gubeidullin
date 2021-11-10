from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *


global_info = {
    'best_users': Profile.objects.all()[:10],
    'hot_tags': Tag.objects.all()[:10],
}
# Create your views here.

def paginate(objects_list, request, per_page=5):
    cl = list(objects_list)
    paginator = Paginator(cl, per_page)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    print("hello drujok-pirojok")
    return page_obj




def index(request):
    latest_question_list = Question.objects.get_new()
    page_obj = paginate(latest_question_list, request)
    return render(request, 'index.html', {'questions': page_obj, 'global_info': global_info})

def hot_questions(request):
    tag_list = Tag.objects.all()[:10]
    hot_question_list = Question.objects.hot()
    page_obj = paginate(hot_question_list, request)
    return render(request, 'hot_questions.html', {'questions': page_obj, 'global_info': global_info})

def sign_in(request):
    return render(request, "sign_in.html", {'global_info' : global_info})


def question(request, qid):
    tag_list_all = Tag.objects.all()[:10]
    question= Question.objects.get(pk=qid)
    comments_list = list(question.comment_set.all())
    page_obj = paginate(comments_list, request, 5)
    tag_list = question.tags.all()[:5]

    return render(request, 'question.html',{'question': question, 'comments': page_obj, 'global_info': global_info, 'question_tags': tag_list})


def registration(request):
    return render(request, "registration.html", {'global_info' : global_info})

def ask(request):
    return render(request, "ask.html", {'global_info' : global_info})

def tag_page(request, tid):
    tag_list = Tag.objects.all()[:10]
    tag = Tag.objects.get(tag_title=tid)
    latest_question_list = tag.question_set.all()
    page_obj = paginate(latest_question_list, request)
    return render(request, 'tag_page.html', {'tag': tid, 'questions': page_obj, 'global_info': global_info})



def hot(request):
    tag_list = Tag.objects.all()[:10]
    hot_question_list = Question.objects.hot()
    page_obj = paginate(hot_question_list, request)
    return render(request, 'hot.html', {'questions': page_obj, 'global_info': global_info})