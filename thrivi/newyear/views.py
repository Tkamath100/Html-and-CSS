from django.shortcuts import render
import datetime

# Create your views here.
def newyear(request):
	now=datetime.datetime.now()
	return render(request, "newyear/newyear.html", 
		{"newyear": now.day==1 and now.month==1})
