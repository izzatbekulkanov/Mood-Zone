from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'blog/blog-dashboard.html')
def blogCategory(request):
    return render(request, 'blog/blog-category.html')
def blogComments(request):
    return render(request, 'blog/blog-comments.html')
def blogDetail(request):
    return render(request, 'blog/blog-detail.html')
def blogGrid(request):
    return render(request, 'blog/blog-grid.html')
def blogList(request):
    return render(request, 'blog/blog-list.html')
def blogMain(request):
    return render(request, 'blog/blog-main.html')
def blogTrending(request):
    return render(request, 'blog/blog-trending.html')
