from django import forms
from django.urls import reverse

# from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget  # image 처리가능

from .models import Item, Basket, Order, Comment

# option1 ModelForm 처리 : model+field로만 정리하면 됨

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'

class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        # fields = '__all__'
        fields = ('item', 'item_name', 'basket_count', 'member_id',)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # fields = '__all__'
        fields = ("item_id", "order_count", "member_id", "item_name", "delivery_name", "delivery_phone", "delivery_zipcode", "delivery_addr1", "delivery_addr2", "delivery_request", "pay_type", "pay_account", "total_price",)

class CommentForm(forms.ModelForm):

    # content = forms.CharField(widget=CKEditorWidget())
    # content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Comment
        fields = ('item_id', 'review_content', 'username',)
        # fields = '__all__'





# option 2 : Form class 로 처리 : 각자의 field 정리
# class BoardForm(forms.Form):
#     subject = forms.CharField()
#     bpassword = forms.CharField()
#     category = forms.IntegerField()
#     writer = forms.CharField()
#     content = forms.CharField(widget=forms.Textarea)

#     def save(self, commit=True):
#         board=Board(**self.cleaned_data)
#         if commit:
#             board.save()
#
#         return board

# class PostSearchForm(forms.Form):
# #     searchNum = forms.CharField(label='Search Num')
# #     searchWord = forms.CharField(label='Search Word')