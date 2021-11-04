from authapp.models import ShopUser
from authapp.forms import ShopUserEditForm
from mainapp.models import ProductCategory
from django import forms


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = '__all__'


class ProductCategoryEditForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'
