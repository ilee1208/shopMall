from django.urls import path, include
from django.contrib import admin
from patShop import views

app_name='patShop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('itemList/', views.itemList, name='itemList'),
    path('itemAdd/', views.itemAdd, name='itemAdd'),
    path('itemSearch/', views.itemSearch, name='itemSearch'),
    path('itemDetail/<int:item_id>/', views.itemDetail, name='itemDetail'),
    path('basketInsert/', views.basketInsert, name='basketInsert'),
    path('basketList/', views.basketList, name='basketList'),
    path('basketDelete/<int:basket_id>/', views.basketDelete, name='basketDelete'),
    path('basketAllDelete/', views.basketAllDelete, name='basketAllDelete'),
    path('orderForm/', views.orderForm, name='orderForm'),
    path('orderPro/', views.orderPro, name='orderPro'),
    path('orderList/', views.orderList, name='orderList'),
    path('commentAdd/', views.commentAdd, name='commentAdd'),
    path('commentDelete/<int:comment_id>/', views.commentDelete, name='commentDelete'),
    # path('boardRemove/<int:board_id>/', views.boardRemove, name='boardRemove'),
    # path('boardSearch/', views.boardSearch, name='boardSearch'),

]