from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView

from app.models import Book


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'app/book_list.html'


class BookView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'app/book_detail.html'


class BookUpdate(UpdateView):
    model = Book
    fields = ('title', 'file', 'custom_dir_name')
    template_name = 'app/book_form.html'

    def get_success_url(self):
        return reverse_lazy('book', kwargs={'pk': self.kwargs.get('pk')})
