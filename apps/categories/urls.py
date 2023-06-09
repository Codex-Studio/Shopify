from django.urls import path

from apps.categories.views import category_detail


urlpatterns = [
    path('<str:slug>/', category_detail, name="category_detail")
]