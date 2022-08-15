from django.urls import path

from ads.views import CategoryView, root, AdsView, CategoryDetailView, AdDetailView

urlpatterns = [
    path('', root),
    path('cat/', CategoryView.as_view()),
    path('ad/', AdsView.as_view()),
    path('cat/<int:pk>', CategoryDetailView.as_view()),
    path('ad/<int:pk>', AdDetailView.as_view())

]