from django.shortcuts import render

def pythonide(request):
	return render(request, 'pythonide.html', {})