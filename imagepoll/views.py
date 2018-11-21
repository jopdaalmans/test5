from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views import generic

from .forms import UserForm

from .models import Item,Category

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'imagepoll/index.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()

class itemdetail(generic.DetailView):
    model = Category
    template_name = 'imagepoll/itemdetail.html'

    def get_queryset(self):
        return Item.objects.all()

class UserFormView(View):
    form_class = UserForm
    template_name = 'imagepoll/registration_form.html'

    # display blank form for a new user signup
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name, {'form': form})

    # process form data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit = False)
            # cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user.username = username
            user.set_password(password)
            user.email = email
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username = username,password = password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('imagepoll:index')

        return render(request, self.template_name, {'form': form})
