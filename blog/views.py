from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post




# Create your views here.
# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request,'blog/home.html',context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'    #to change the default template to look into
    context_object_name = 'posts'       #the name of the context variable should be *posts* rather than default variable name
    ordering = ['-date_posted']         # negative sign indicates that ordering should be from new to old. Remove the negative sign to change the order from old to new
    paginate_by = 7


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'    
    context_object_name = 'posts'        
    paginate_by = 7

    def get_queryset(self):
        user = get_object_or_404(User,username= self.kwargs.get('username'))     #pick up username from url
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request,'blog/about.html',{'title': 'About'})