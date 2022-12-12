from .models import Category

def categories(request):
    category = Category.objects.filter(parent_category=None)

    context ={
        'category':category
    }
    return context