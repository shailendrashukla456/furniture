from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'my_shop/base.html')

def about(request):
    return render(request, 'my_shop/about.html')

def services(request):
    return render(request,'my_shop/services.html')

def products(request):
    return render(request,'my_shop/products.html')

def projects(request):
    return render(request,'my_shop/projects.html')

def clients(request):
    return render(request,'my_shop/clients.html')

def contact(request):
    print("hello")
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # OR contact_success if defined
        else:
            print("❌ Form Errors:", form.errors)
    else:
        form = ContactForm()
    return render(request, 'my_shop/contact.html', {'form': form})
