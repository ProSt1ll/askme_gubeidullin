from django.contrib import admin
from django.urls import path
from questions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="new"),
    path('sign_in/', views.sign_in, name="sign_in"),
    path('question/<int:qid>', views.question, name="question"),
    path('registration/', views.registration, name="registration"),
    path('ask/', views.ask, name="ask"),
    path('tag/<str:tid>/', views.tag_page, name='tag'),
    path('hot/', views.hot, name='hot'),
]
