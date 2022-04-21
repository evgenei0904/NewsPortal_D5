from django.contrib import admin
from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch, NewsCreate, NewsUpdate, NewsDelete, UserUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('search', NewsSearch.as_view()),
    path('add', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('user/', UserUpdateView.as_view(), name='user_update'),


]


