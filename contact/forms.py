from django import forms

class ContactForm(forms.Form):
	name    = forms.CharField(required=False, max_length=100, help_text='Please enter your name.')
	email   = forms.EmailField(required = True)
	comment = forms.CharField(required = True, widget=forms.Textarea)


	def send_email(self):
		pass