from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import RegistrationForm,AccountAuthenticationForm
from .models import Company
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required


def renderhome(request):
    return render(request,'companies/home.html')

def register_view(request):
    context={}
    if request.POST:
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            print(request.FILES)
            # uploaded_file=request.FILES['company-logo']
            # fs=FileSystemStorage()
            # fs.save(uploaded_file.name,uploaded_file)
            
            return redirect('companylist')
        else:
            context['form'] = form
            return render(request,'companies/register.html',context)
    else:
        form = RegistrationForm()
        context['form'] = form
        return render(request, 'companies/register.html', context)
    

        



    
@login_required
def list_companies_view(request):
    context={}
    companies=Company.objects.all()
    context['companies']=companies
    
    return render(request,'companies/companylist.html',context)
    