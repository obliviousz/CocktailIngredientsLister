from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
import requests

def byname(request):
	if request.method == "POST":
		name = request.POST.get('name')
		name.lower()
		s = 'http://www.thecocktaildb.com/api/json/v1/1/search.php?s='
		s += name
		response = requests.get(s).json()
		if len(response)==0:
			return HttpResponse(render(request,"base.html",{"present":False,"searched":True}))

		return HttpResponse(render(request,"base.html",{"present": True, "response":response['drinks'],"searched":True}))
	return HttpResponse(render(request,"base.html",{"present": False, "searched":False}))