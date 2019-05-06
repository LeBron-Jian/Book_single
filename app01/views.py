from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from app01 import models

def books(request):
    book_list = models.Book_single.objects.all()
    return render(request, 'app01/books.html', locals())

def addbooks(request):

    # title = 'python1'
    # price = 100
    # publish = '机械出版社'
    # pub_date = '2019-3-3'
    # book_obj = models.Book_single.objects.create(title=title, price=price,
    #                                publish=publish, pub_date=pub_date)
    # book_obj.save()
    # return HttpResponse("OK")
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub-date')
        publish = request.POST.get('publish')
        if title == '' or price == '' or pub_date == '' or publish == '':
            return render(request, 'app01/addbook.html', {'ret': '所有选项不能为空'})

        models.Book_single.objects.create(title=title, price=price,
                                          pub_date=pub_date, publish=publish)
        return redirect('/app01/books')
    else:
        return render(request, 'app01/addbook.html')

def delbook(request, id):
    # return HttpResponse("OK")
    print(models.Book_single.objects.filter(id=id))
    models.Book_single.objects.filter(id=id).delete()

    # 两次请求
    return redirect('/app01/books/')

def changebook(request, id):
    book_obj = models.Book_single.objects.filter(id=id).first()
    print(book_obj)
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub-date')
        publish = request.POST.get('publish')
        if title == '' or price == '' or pub_date == '' or publish == '':
            return render(request, 'app01/addbook.html', {'ret': '所有选项不能为空'})

        models.Book_single.objects.filter(id=id).update(title=title, price=price, pub_date=pub_date, publish=publish)
        return redirect('/app01/books/')
    else:
        return render(request, 'app01/change.html', {'book_obj': book_obj})

def query(request):
    # 1, 查询Publish1出版过价格大于100的书籍
    book_list = models.Book_single.objects.filter(publish='Publish1', price__gt=100)
    print(book_list)

    # 2，查询2019年1月出版的所有以py开头的数据名称
    book_list = models.Book_single.objects.filter(title__startswith='py', pub_date__year=2019,
                                                  pub_date__month=1).values('title')
    print(book_list)

    # 3，查询价格为50,100 或者150 的所有书籍的名称及其出版社名称
    book_list = models.Book_single.objects.filter(price__in=[50, 100, 150]).values('title', 'publish')
    print(book_list)

    # 4，查询价格在100到200之间所有书籍名称及其价格
    book_list = models.Book_single.objects.filter(price__range = [100, 200]).values('title', 'price')
    print(book_list)

    # 5， 查询所有Publish1出版的书籍的价格（由高到底排序，去重）
    book_list = models.Book_single.objects.filter(publish='Publish1').values('price').distinct().order_by('-price')
    print(book_list)

    return HttpResponse('OK')


def test(request):
    return HttpResponse("OK")