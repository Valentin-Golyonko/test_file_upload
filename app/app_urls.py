from django.urls import path

from app.views import BookListView, BookView, BookUpdate

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('<int:pk>/', BookView.as_view(), name='book'),
    path('update/<int:pk>/', BookUpdate.as_view(), name='book-update'),
]
