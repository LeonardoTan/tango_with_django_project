from django import forms
from rango.models import Category, Page, UserProfile
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    """Category表单数据类型"""
    name = forms.CharField(
        max_length=128, help_text='Please enter the category name.')
    # views = forms.IntegerField(widget=forms.HiddenInput(), initial='0')
    # likes = forms.IntegerField(widget=forms.HiddenInput(), initial='0')
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # 用内联类型提供表单的额外信息
    class Meta:
        model = Category
        # 包含的字段
        fields = ['name']


class PageForm(forms.ModelForm):
    """Page表单数据类型"""
    title = forms.CharField(
        max_length=128, help_text='Please enter the title of the Page.')
    url = forms.URLField(
        max_length=200, help_text='Please enter the URL of the page.')
    # views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        # 排除的字段
        exclude = ['category', 'views']

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        # If url is not empty and doesn't start with 'http://', prepend
        # 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
        return cleaned_data


# class UserForm(forms.ModelForm):
#     """docstring for UserForm"""
#     password = forms.CharField(widget=forms.PasswordInput())

#     class Meta:
#         """docstring for Meta"""
#         model = User
#         fields = ['username', 'email', 'password']


class UserProfileForm(forms.ModelForm):
    """docstring for Userp"""
    class Meta:
        model = UserProfile
        fields = ['website', 'picture']