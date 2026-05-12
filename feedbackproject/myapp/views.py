from django.shortcuts import render
from myapp.forms import FeedbackForm
# Create your views here.

def formview(request):
    f=FeedbackForm()
    if request.method=="POST":
        f=FeedbackForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data['name']
            rollno = f.cleaned_data['rollno']
            feedback = f.cleaned_data['feedback']

            d = {
                'name': name,
                'feedback': feedback,
                'rollnumber': rollno
            }

            return render(request, 'output.html', d)

    d={'form':f}
    return render(request,'form.html',d)