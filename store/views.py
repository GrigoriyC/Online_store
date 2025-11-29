 
from django.shortcuts import render

from store.models import Products

# "request" в скобках указывать обязательно, можно поставить другое слово, 
# но лучше "request".
def get_product_list(request): 
  products = Products.objects.all()

  # Здесь уже нужно создать 
  # первый шаблон. Путь 'blog/index.html' здесь не нужно указывать полный. 
  # Джанго шаблоны ищет в папке "templates".
  return render(request, 'store/index.html', context={'products': products})
