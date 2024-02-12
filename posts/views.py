from django.http import HTTP_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins

from .models import Post
from .serializer import PostSerializer

class PostListView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIViews):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, ** kwargs):
        return self.create(request, *args, **kwargs)                

class PostDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
# class PostListView(APIView):

#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = PostSerializer(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
# class PostDetailView(APIView):
#     def get_objects(self, pk):
#         try:
#             post = Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise HTTP_404
#         return post
    
#     def get(self, request, pk):
#         post = self.get_objects(pk)

#         serializer = PostSerializer(post)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         post = self.get_objects(pk)
        
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         post = self.get_objects(pk)
#         post.delete()
#         return Response(status=status.HTTP_404_NO_CONTENT)
    
# from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
# from .models import Post, Comment
# from django.shortcuts import render, get_object_or_404
# from .forms import PostForm
# from django.views import generic
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .serializer import PostSerializer

# @api_view(['GET'])
# def index(request):
#     # pk = request.query_params.get('pk')
#     pk = request.data.get('pk')
#     try:
#         p = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         return Response({ 'detail': 'Post not exist'}, status=status.Http_404_Not_FOUND)
#     serializer = PostSerializer(p)
#     return Response(serializer.data)

# class PostList(generic.ListView):
#     queryset = Post.objects.all()
#     template_name = 'posts/post_list.html'

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'posts/post_detail.html'

#     def get_context_data(self, **kwargs):
#         context = super(PostDetail, self).get_context_data()
#         context['comments'] = Comment.objects.filter(post=kwargs['objects'].pk)
#         return context
    
#     # context_object_name = 'posts'

#     # def get_queryset(self):
#     #     return get_object_or_404(Post, pk=self.request.POST['post_id'])



# def home(request):
#     return HttpResponse("home")

# def post_list(request):
#     posts = Post.objects.all()
#     context = { "posts": posts }
#     return render(request, "posts/posts.html", context=context)

# def post_detail(request, post_id):
    
#     post = get_object_or_404(Post, post_id)
#     comments = Comment.objects.filter(post=post)
#     context = { "post": post, "comments": comments }
#     return render(request, "posts/post_detail.html", context=context)

# def post_create(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             Post.objects.create(**form.cleaned_data)
#             return HttpResponseRedirect('/posts/')
#     else:
#         form = PostForm()

#     return render(request, 'post/post_create.hml', { 'form': form })  

# class PostList(generic.ListView):
#     queryset = Post.objects.all()
#     template_name = 'posts/post_list.html'

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'posts/post_detail.html'

#     def get_context_data(self, **kwargs):
#         context = super(PostDetail, self).get_context_data()
#         context['comments'] = Comment.objects.filter(post=kwargs['objects'].pk)
#         return context
    
#     # context_object_name = 'posts'

#     # def get_queryset(self):
#     #     return get_object_or_404(Post, pk=self.request.POST['post_id'])

# def index(request):
#     return HttpResponse("index")

# def home(request):
#     return HttpResponse("home")

# def post_list(request):
#     posts = Post.objects.all()
#     context = { "posts": posts }
#     return render(request, "posts/posts.html", context=context)

# def post_detail(request, post_id):
#     # try:
#     #     post = Post.objects.get(pk=post_id)
#     # except Post.DoesNotExist:
#     #     return HttpResponseNotFound('Post is not exist!')
    
#     post = get_object_or_404(Post, post_id)
#     comments = Comment.objects.filter(post=post)
#     context = { "post": post, "comments": comments }
#     return render(request, "posts/post_detail.html", context=context)

# def post_create(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             Post.objects.create(**form.cleaned_data)
#             return HttpResponseRedirect('/posts/')
#     else:
#         form = PostForm()

#     return render(request, 'post/post_create.hml', { 'form': form })    