from django import forms
from .models import StaffInformation, Department, Book, Staff


class StaffInformationForm(forms.ModelForm):

    # Djangoでは、class Meta というものを定義する
    class Meta:
        model = StaffInformation

        # 画面上に表示する入力欄を埋める
        # fields = '__all__ で全て表示できる
        # excludes = ('email', ...) で除くこともできる
        fields = ('staff_name', 'email', 'address', 'birthday', 'hire_date', 'at_desk')


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name',)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'management_code')


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('name', 'information', 'department', 'rented_books')


class StaffInformationUpdateForm(forms.ModelForm):

    # フォームが作る入力欄のHTMLに、一括でclass="input"のように指定したい場合は、次のような _init_メソッドを作成してください。
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-input'

    class Meta:
        model = Staff
        fields = ('name', 'information', 'department', 'rented_books')
        widgets = {
            'address': forms.Textarea
        }