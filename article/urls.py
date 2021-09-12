from django.urls import path
from .views import ArticleView

# for reverse lookup
appName = "articles"

urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', ArticleView.as_view()),
]