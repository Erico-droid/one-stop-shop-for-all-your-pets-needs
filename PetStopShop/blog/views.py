from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from accounts.form import *
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, View
from django.views.generic import FormView
# from django.urls import reverse_lazy
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#from django.http import HttpResponse



def home(request):
    return render(request, 'blog/index.html')

def blog(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Home',
        }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

def contact_us(request):
    return render(request, 'blog/contact.html')


class BlogPostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-created_on']

class BlogPostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(post = self.get_object()).order_by('-created_on')
        data['comments'] = comments
        if self.request.user.is_authenticated:
            data['form'] = CommentForm(instance=self.request.user)

        return data

    def post(self, request, *args, **kwargs):
        comment = Comment(body=request.POST.get('body'), user=self.request.user, post=self.get_object())
        comment.save()
        return self.get(self, request, *args, **kwargs)


class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # form_class = AddNewPost

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    # form_class = AddNewPost

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class BlogPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostComment(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = 'post_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(PostComment, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse('post_detail', kwargs={'pk': post.pk}) + '#comments'

class PostDetailView(View):

    def get(self, request, *args, **kwargs):
        view = BlogPostDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostComment.as_view()
        return view(request, *args, **kwargs)
