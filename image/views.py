from django.core.mail import mail_admins
from django.shortcuts import render

# Create your views here.
def index(request):
	mail_admins('our subject', 'content')
	return render(request, 'base.html', context={})

def thing_detail(request, slug):
	thing = Thing.objects.get(slug=slug)

	social_accounts = thing.social_accounts.all()

	return render(request, 'things/thing_detail.html', {
			'thing' : thing,
			'social_accounts': social_accounts
		})