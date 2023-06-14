from django.views import generic
from django.views.generic import CreateView, DetailView, UpdateView, FormView
from django.urls import reverse_lazy
from .models import StaffInformation, Department, Book, Staff
from .forms import StaffInformationForm, DepartmentForm, BookForm, StaffForm

# from django.shortcuts import render, redirect


class StaffListView(generic.ListView):
    model = Staff
    template_name = 'myapp2/staff_list.html'


class StaffInformationCreateView(CreateView):
    model = StaffInformation
    form_class = StaffInformationForm
    template_name = 'myapp2/staff_information_create.html'

    # URLの逆引きを実施　app_name関数のname
    success_url = reverse_lazy('myapp:home')
    # success_url = '/home/' と同じ


class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'myapp2/department_create.html'
    success_url = reverse_lazy('myapp:home')


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'myapp2/book_create.html'
    success_url = reverse_lazy('myapp:home')


class StaffCreateView(CreateView):
    model = Staff
    form_class = StaffForm
    template_name = 'myapp2/staff_create.html'
    success_url = reverse_lazy('myapp:home')


# 関数で書く場合
"""
def staff_information(request):
    if request.method == 'POST':
        form = StaffInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:home')
        else:
            context = {
                'form': form,
            }
            return render(request, 'myapp/staff_information_create.html', context)
    else:
        form = StaffInformationForm()
        context = {
            'form': form,
        }
        return render(request, 'myapp/staff_information_create.html', context)
"""