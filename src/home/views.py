from django.shortcuts import render
from .models import Product


def indexview(request):
    queryset=Product.objects.all()
    lookBook=Product.objects.get(pk=9)

    context={
        'object_list':queryset,
         'product'   : lookBook
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

def productPageView(request):
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



