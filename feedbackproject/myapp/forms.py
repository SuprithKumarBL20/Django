from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    feedback = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        n=self.cleaned_data['name']
        if len(n)<=3:
            raise forms.ValidationError("minimum no of characte is 3 ")
        return n
