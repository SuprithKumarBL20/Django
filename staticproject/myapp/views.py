from django.shortcuts import render

# Create your views here.
def myview(request):
    name='rama'
    bird='peacock'
    animal='lion'
    dish="biryani"
    ctx={'name':name,'bird':bird,'animal':animal,'dish':dish}
    return render(request,'myapp/fav.html',ctx)