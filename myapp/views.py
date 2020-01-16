from django.shortcuts import render
from myapp.models import *
from django.forms import inlineformset_factory
from myapp.forms import *
# Create your views here.
def index(request,top_name):
    topic=Topic.objects.get(top_name=top_name)
    webpage_form=inlineformset_factory(Topic,Webpage,fields=("name","url")\
        ,extra=1,can_delete=False)
    if request.method=="POST":
        form=webpage_form(request.POST,instance=topic)
        if form.is_valid():
            form.save()
            
    form=webpage_form(instance=topic)
    return render(request,"index.html",context={"form":form})


def form_demo(request):
    form=AddressForm()
    return render(request,"index.html",context={'form':form})

def image_upload(request):
    if request.method=='POST':
        print(request.FILES)
        
    form=Upload_FORM()
    return render(request,"sample.html",{"form":form})