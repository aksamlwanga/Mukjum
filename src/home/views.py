from django.shortcuts import render,get_list_or_404,redirect
from .models import Product
from django.http import Http404, request
from django.db.models import Q

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

def categoriesView(request):
    return render(request,"categories.html")

def shoppingCartView(request):
    return render(request,"shopping-cart.html")

def productPageView(request,product_id):
    # obj= Product.objects.get(id=my_id)
    # obj=get_list_or_404(Product,id=my_id)
    try:
         productsobject= Product.objects.get(id=product_id)
         imageobject=productsobject.image.all()
         queryset=Product.objects.filter(Q(featured=True) | Q(catergory=productsobject.catergory) )
         next_product=Product.objects.filter(catergory=productsobject.catergory,id=productsobject.id+1).order_by('id').first()
         previous_product=Product.objects.filter(catergory=productsobject.catergory,id=productsobject.id-1).order_by('id').first()
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



