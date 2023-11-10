from django.shortcuts import render


def encontrar_jobs(request):
    if request.method == "GET":
        return render(request, 'encontrar_jobs.html')