from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Thermal
from .form import ThermalPost


def home(request):
    return render(request, 'home.html')


def create(request):
    blog = Thermal()
    blog.title = request.GET['title']
    blog.student_name = request.GET['student_name']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/get_temp/'+str(blog.id))


def detail(request, thermal_id):
    thermal_detail = get_object_or_404(Thermal, pk=thermal_id)
    return render(request, 'detail.html', {'thermal': thermal_detail})


def blogpost(request):
    if request.method == "POST":
        form = ThermalPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            print('time: ',timezone.now())
            post.save()
            return redirect('new')
    else:
        form = ThermalPost()
        return render(request, 'new.html', {'form': form})


def new(request):
    return render(request, 'new.html')