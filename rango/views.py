from django.shortcuts import render
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]

    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {'category': category_list, 'page': page_list}

    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html', {})


def category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages

        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context_dict)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category1 = form.save(commit=True)
            print(category1, category1.slug)
            return index(request)
        else:
            print(form.errors)
    else:
        form = CategoryForm()

    context_dict = {'form': form}
    return render(request, 'rango/add_category.html', context_dict)


def add_page(request, category_name_slug):
    try:
        category1 = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category1 = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category1:
                page = form.save(commit=False)
                page.category = category1
                page.views = 0
                page.save()
                # probably better to use a redirect here.
            return category(request, category_name_slug)
        else:
            print(form.errors)
    else:
        form = PageForm()

    context_dict = {'form': form, 'category': category}

    return render(request, 'rango/add_page.html', context_dict)
