from django.shortcuts import render,get_list_or_404,redirect
from .models import Product,ProductCategory,ProductSubCategory
from django.http import Http404, request
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def indexview(request):
    queryset=Product.objects.all()
    # Products = Product.objects.filter()
    # images = Products[0].image.first()
    # print(images.image)
    context={
        'object_list':queryset,
        #  'product'   : lookBook
    }
    return render(request,"index.html",context)
    

def checkOutView(request):
    return render(request,"check-out.html")

def contactView(request):
    return render(request,"contact.html")

def categoriesNavView(request):
     queryset=ProductCategory.objects.all()
     context={
        'object_list':queryset,
    }
     return render(request,"categoriesnav.html",context)

def categoriesView(request,category_id):
    
    if request.method=="POST":
        productsfilter=request.POST['productFilter']
        if productsfilter=='price':
            queryset=Product.objects.filter().order_by('price').all()
            
        elif productsfilter=='featured':
            queryset=Product.objects.filter().order_by('id').all()

        elif productsfilter=='order':
            queryset=Product.objects.filter(Q(title='shoes')).order_by('name').all()
    else:    
        queryset=Product.objects.filter(categoryId_id=category_id)

    page = request.GET.get('page')

    paginator = Paginator(queryset, 8)
    try:
        queryset_number = paginator.page(page)
    except PageNotAnInteger:
        queryset_number = paginator.page(1)
    except EmptyPage:
        queryset_number = paginator.page(paginator.num_pages)
    context={
        'product_list':queryset_number,
        
    }
    return render(request,"categories.html",context)

def subcategoriesView(request,subcategory_id):
    
    if request.method=="POST":
        productsfilter=request.POST['productFilter']
        if productsfilter=='price':
            queryset=Product.objects.filter(subCategoryId_id=subcategory_id).order_by('price').all()
            
        elif productsfilter=='featured':
            queryset=Product.objects.filter(subCategoryId_id=subcategory_id).order_by('id').all()

        elif productsfilter=='order':
            queryset=Product.objects.filter(subCategoryId_id=subcategory_id).order_by('name').all()
    else:    
        queryset=Product.objects.filter(subCategoryId_id=subcategory_id)

    page = request.GET.get('page')

    paginator = Paginator(queryset, 8)
    try:
        queryset_number = paginator.page(page)
    except PageNotAnInteger:
        queryset_number = paginator.page(1)
    except EmptyPage:
        queryset_number = paginator.page(paginator.num_pages)
    context={
        'product_list':queryset_number,
        
    }

    return render(request,"categories.html",context)

def shoppingCartView(request):
    return render(request,"shopping-cart.html")

def productPageView(request,product_id):
    # obj= Product.objects.get(id=my_id)
    # obj=get_list_or_404(Product,id=my_id)
    try:
         productsobject= Product.objects.get(id=product_id)
         imageobject=productsobject.image.all()
         queryset=Product.objects.filter(Q(featured=True) | Q(name=productsobject.name) )
         next_product=Product.objects.filter(name=productsobject.name,id=productsobject.id+1).order_by('id').first()
         previous_product=Product.objects.filter(name=productsobject.name,id=productsobject.id-1).order_by('id').first()
         print(next_product,previous_product)
        #  for i in imageobject:
        #      print(i.image)
    except Product.DoesNotExist:
        raise Http404
    productContext={
        'object':productsobject,
        'images':imageobject,
         'items':queryset,
         'next_product':next_product,
         'previous_product':previous_product
    }
    return render(request,"product-page.html",productContext)

def productsPageView(request):
    return render(request,"product-page.html")

# def register(request):
#     if request.method=="POST":
#         # form=UserCreationForm(request.POST)
#         form=UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data.get('username')
#             messages.success(request,f'Your account has been created! You are now able to log in ')
#             return redirect('')
#     else:
#         # form=UserCreationForm()
#          form=UserRegistrationForm()
#     return render(request,'register.html',{'form':form})



