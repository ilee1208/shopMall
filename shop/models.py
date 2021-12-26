from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse

# from ckeditor_uploader.fields import RichTextUploadingField  # ckeditor(image 처리가능)

# def min_length_validator(value):
#     if len(value)<3:
#         raise forms.ValidationError('3글짜 이상 입력해주세요.')

# category
MainFood = 'Main shop'
SideMenu = 'Side Menu'
Cleaner  = 'Others'

TYPE_CHOICES = (
    (MainFood, '메인Food'),
    (SideMenu, 'Side Menu'),
    (Cleaner, 'Cleaner'),
)

class Item(models.Model):

    item_name=models.CharField(max_length=100, verbose_name='품명')
    item_type = models.CharField(max_length=10, verbose_name='타입', choices=TYPE_CHOICES)
    item_mainimg=models.FileField(upload_to='uploaded/', verbose_name='매인IMG' )
    item_detailimg = models.FileField(upload_to='uploaded/', verbose_name='세부IMG')
    item_basketimg = models.FileField(upload_to='uploaded/', verbose_name='장바구니IMG')
    item_price=models.IntegerField(default=0, verbose_name='가격')
    item_dcprice=models.IntegerField(default=0, blank="True", verbose_name='DC가격')
    item_totalcount=models.IntegerField(default=0, verbose_name='총량')
    item_salecount=models.IntegerField(default=0, verbose_name='판매수량')
    item_remaincount=models.IntegerField(default=100, verbose_name='잔여량')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']   # - : reverse

    # def __str__(self):                      # Shop() 호출시 subject 리턴
    #     return self.subject
    # def get_absolute_url(self):            # Shop.get_absolute_url()호출시 url 리턴
    #     return reverse('board/boardlist', args=self.id)

class Basket(models.Model):

    item_name=models.CharField(max_length=100, verbose_name='품명')
    basket_count=models.IntegerField(verbose_name='판매수량')
    member_id=models.IntegerField(verbose_name='멤버ID')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='상품ID')


    class Meta:
        ordering = ['-id']   # - : reverse

class Order(models.Model):

    delivery_name=models.CharField(max_length=100, verbose_name='접수자명')
    delivery_phone = models.CharField(max_length=100, verbose_name='전화')
    delivery_zipcode = models.CharField(max_length=100, verbose_name='우편번호')
    delivery_addr1 = models.CharField(max_length=100, verbose_name='주소1')
    delivery_addr2 = models.CharField(max_length=100, blank="True", verbose_name='주소2')
    delivery_request = models.CharField(max_length=100, blank="True", verbose_name='요구사항')
    pay_type=models.CharField(max_length=100, verbose_name='지불방법')
    pay_account=models.CharField(max_length=100, blank="True", verbose_name='계좌번호')
    member_id = models.IntegerField(verbose_name='멤버ID')
    item_name = models.CharField(max_length=100, verbose_name='상품명')
    order_count = models.IntegerField(verbose_name='품목갯수')
    item_id = models.IntegerField(verbose_name='멤버ID')
    total_price = models.IntegerField(verbose_name='가격')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']   # - : reverse


class Comment(models.Model):
    item_id = models.IntegerField(verbose_name='품목ID')
    review_content = models.TextField(verbose_name='내용')
    username = models.CharField(max_length=100, verbose_name='성명')
    review_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']  # - : reverse

