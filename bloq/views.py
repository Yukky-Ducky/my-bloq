# bloq/views.py


from django.views.generic import ListView, DetailView

from .models import Post



class BloqListView(ListView):
    model = Post
    template_name = 'home.html'


class BloqDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'