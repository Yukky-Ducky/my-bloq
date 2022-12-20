# bloq/urls.py

from django.urls import path

from . import views


urlpatterns = [
    path('', views.BloqListView.as_view(), name='home'),
    path('post/<int:pk>/', views.BloqDetailView.as_view(), name='post_detail'),
]