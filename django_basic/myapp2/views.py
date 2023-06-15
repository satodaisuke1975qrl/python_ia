from django.views import generic
from django.views.generic import CreateView, DetailView, UpdateView, FormView
from django.urls import reverse_lazy
from .models import StaffInformation, Department, Book, Staff
from .forms import StaffInformationForm, DepartmentForm, BookForm, StaffForm

# from django.shortcuts import render, redirect


class StaffListView(generic.ListView):
    model = Staff
    template_name = 'myapp2/staff_list.html'


class StaffDetailView(generic.DetailView):
    model = Staff
    template_name = 'myapp2/staff_detail.html'

    def get_object(self, queryset=None):

        # self.kwargsには、URL内のint:pkといった部分が含まれている
        staff = Staff.objects.get(pk=self.kwargs['pk'])
        # →Staff.objects.get(pk=1)  # 今回、URLは/staff_detail/1/
        # →Staff.objects.get(id=1)  # 今回のpkはidフィールドのこと

        # ターミナルのログに表示される
        print(staff)

        return staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        staff = self.get_object()
        context['books'] = staff.rented_books.all()
        return context


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