from django.shortcuts import render, redirect, reverse
from apps.forms import BlogForm
from apps.models import BlogC, Blog, BlogComment, ProductC, Product, ProductComment


def blogs(request):
    category_id = request.GET.get('category', 0)
    if category_id:
        blogss = Blog.objects.filter(category_id=category_id)
    else:
        blogss = Blog.objects.all()
    context = {
        'blogs': blogss,
        'categories': BlogC.objects.all()
    }
    return render(request, 'apps/blog_list.html', context)


def add_blog(request):
    context = {
        'categories': BlogC.objects.all()
    }
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs')
    return render(request, 'apps/add_blog.html', context)


def one_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    comments = BlogComment.objects.filter(blog=blog)
    context = {
        'blog': blog,
        'comments': comments
    }
    return render(request, 'apps/blog_detail.html', context)


def add_comment_blog(request, pk):
    if request.method == 'POST':
        blog = Blog.objects.get(pk=pk)
        BlogComment.objects.create(body=request.POST['body'], blog=blog)
    return redirect(reverse('one_blog', kwargs={'pk': pk}))


def products_page(request):
    category_id = request.GET.get('category', 0)
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    context = {
        'products': products,
        'categories': ProductC.objects.all()
    }
    return render(request, 'apps/products.html', context)


def one_product(request, pk):
    product = Product.objects.get(id=pk)
    comments = ProductComment.objects.filter(product=product)
    context = {
        'product': product,
        'comments': comments
    }
    return render(request, 'apps/product_detail.html', context)


def add_comment_product(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        ProductComment.objects.create(body=request.POST['body'], product=product)
    return redirect(reverse('one_product', kwargs={'pk': pk}))
