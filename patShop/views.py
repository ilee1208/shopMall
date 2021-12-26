from django.shortcuts import render, redirect, get_object_or_404

#http 출력위함
from django.http import HttpResponse, HttpResponseRedirect

# django app(auth) Model-authenticate, login 활용
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

#model불러올때
from .models import Item, Basket, Order, Comment

#form 불러올때
from .forms import ItemForm,  BasketForm, OrderForm, CommentForm    #PostSearchForm

#Paginator 불러올때
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# decorator 불러들일때
from django.contrib.auth.decorators import login_required
#from patShop.decorators import user_is_patShop_author

# message불러올때
from django.contrib import messages

#search 기능 수행
from django.views.generic.edit import FormView
from django.db.models import Q

# reverse 함수 사용할때
from django.urls import reverse
#=========================================

def itemList(request):

    best_list = Item.objects.filter(item_salecount__gte=0 )
    item_list = Item.objects.all()

    # Pagination Block : page에 값이 없으면 1, 값이 있으면 그 값을 가져온디
    page = request.GET.get('page', 1)

    # 한페이지에 5개씩 담는다
    paginator = Paginator(item_list, 5)

    try:
        Shops = paginator.page(page)

    except PageNotAnInteger:
        Shops = paginator.page(1)
    except EmptyPage:
        Shops = paginator.page(paginator.num_pages)

    data ={
        'bestList':best_list,
        'itemList':item_list
    }
    return render(request, 'patShop/itemList.html', data)

@login_required
def itemAdd(request):

    if request.method == 'POST':

        form = ItemForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'patShop was successfully added!')
            return redirect('patShop:itemList')

    else:

        data = {
            'form': ItemForm(),
            'patShop_id': 0,
        }
    return render(request, 'patShop/itemForm.html', data)

def itemDetail(request, item_id):

    item = get_object_or_404(Item, pk=item_id)
    comment_list = Comment.objects.filter(item_id=item_id)

    data ={
        'item' : item,
        'item_id' : item_id,
        'commentList': comment_list,
    }
    return render(request, 'patShop/itemDetail.html', data)

@login_required
#@user_is_patShop_author
def itemRemove(request, item_id):
    patShop = get_object_or_404(Item, pk=item_id)
    patShop.delete()
    messages.success(request, 'patShop-item was successfully removed!')
    return redirect('patShop:itemList')

# @login_required
# @user_is_board_author
# def transferBoard(request, board_id):
#     board = get_object_or_404(Board, pk=board_id)
#
#     transfer_to = request.POST.get('transfer_to')
#     new_owner = User.objects.get(pk=transfer_to)
#     board.created_by = new_owner
#
#     board.save()
#     messages.success(request, 'Board was successfully transferred!')
#     return redirect('board:boardList')


def itemSearch(request):

    template_name = 'patShop/itemList.html'

    searchNum = request.POST['searchNum']
    searchWord = request.POST['searchWord']

    if searchNum=='0':

        search_list = Item.objects.filter(
            Q(item_name__icontains=searchWord) | Q(item_type__icontains=searchWord)
        ).distinct()

        search_best = Item.objects.filter(
            Q(item_name__icontains=searchWord) & Q(item_salecount__gte=0)
        ).distinct()

    # elif searchNum=='1':
    #     results = Board.objects.filter(subject__icontains=searchWord).distinct()
    # elif searchNum=='2':
    #     results = Board.objects.filter(content__icontains=searchWord).distinct()

    else:
        results = []

    data = {
        'bestList': search_best,
        'itemList': search_list
    }
    return render(request, template_name, data)



@login_required
def orderForm(request):

    if request.method == 'POST':

        item_id = request.POST['item_id']
        member_id = request.session['member_id']
        order_count = request.POST['order_count']

        # print(item_id)
        # print(order_count)

        orderItem = get_object_or_404(Item, pk=item_id)
        member = get_object_or_404(User, pk=member_id)

        data = {
            'orderItem': orderItem,
            'member': member,
            'order_count': order_count
        }

        return render(request, 'patShop/orderForm.html', data)

@login_required
def orderPro(request):

    if request.method == 'POST':

        form = OrderForm(request.POST)

        if form.is_valid():

            form.save()
            messages.success(request, 'Order was successfully added!')

            return redirect('patShop:orderList')

@login_required
def orderList(request):

    order_list = Order.objects.filter(member_id = request.session['member_id'])
    orderItem = Order.objects.filter(member_id = request.session['member_id']).first()

    data ={
        'orderList': order_list,
        'orderItem': orderItem,
    }
    return render(request, 'patShop/orderList.html', data)

@login_required
def basketInsert(request):

    if request.method == 'POST':
        form = BasketForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Basket was successfully added!')
            return redirect('patShop:basketList')
    else:
        data = {
            'form': BasketForm(),
            'basket_id': 0,
        }
    return render(request, 'patShop/basketList.html', data)

@login_required
def basketList(request):

    basket_list = Basket.objects.select_related()    # select_related : foreign_key 와 연계 Basket - Item 연계(PK)

    data ={
        'basketList': basket_list,
    }

    return render(request, 'patShop/basketList.html', data)

@login_required
def basketDelete(request, basket_id):
    basket = get_object_or_404(Basket, pk=basket_id)
    basket.delete()
    messages.success(request, 'Basketitem was successfully deleted!')
    return redirect('patShop:basketList')

@login_required
def basketAllDelete(request):
    basket = Basket.objects.filter(member_id = request.session['member_id'])
    basket.delete()
    messages.success(request, 'Basket All item was successfully deleted!')
    return redirect('patShop:basketList')

@login_required
def commentAdd(request):

    item_id = request.POST['item_id']


    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form)

        if form.is_valid():
            form.save()
            messages.success(request, 'Comment was successfully added!')

            return HttpResponseRedirect(reverse('patShop:itemDetail', args=(item_id,)))
            # return render(request, 'patShop:itemDetail', request.POST['item_id'])

@login_required
def commentDelete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, 'Comment was successfully deleted!')

    return redirect('patShop:itemList')