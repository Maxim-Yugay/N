from django.views.generic import ListView, DetailView
from .models import *


class AuthorList(ListView):
    model = Author
    context_object_name = 'Author'

class PostList(ListView):
    model = Post
    context_object_name = 'post'

class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'

