from django.shortcuts import render,redirect
from accounts.models import Movie,Theatre,Book1
from home.forms import BookForm
def homeview(request):
    movies = Movie.objects.all()
    args = {'movies': movies}
    return render(request,'home/home.html',args)


def movie_view(request,pk):
    x=''
    y=''
    pk=int(pk)
    movie=Movie.objects.all()
    for i in movie:
        if pk==i.sno:
            x=i.movie
    for i in movie:
        if pk==i.sno:
            y=i.videofile
    pk=str(pk)
    args={'x':x,'y':y,'pk':pk,'first':'first','second':'second','third':'third'}
    return render(request,'home/movieview.html',args)

def first_show_view(request,pk):
    x = ''
    y = []
    pk = int(pk)
    print(pk)
    movie = Movie.objects.all()
    theat=Theatre.objects.all()
    for i in movie:
        if pk == i.sno:
            x = i.movie
            print(x)
    for i in theat:
        if x==i.first:
            y.append(i.name)
    pk = str(pk)
    args = {'x': x, 'y': y, 'pk': pk,'first':'first'}
    return render(request, 'home/show.html', args)


def second(request,pk):
    x = ''
    y = []
    pk = int(pk)
    print(pk)
    movie = Movie.objects.all()
    theat = Theatre.objects.all()
    for i in movie:
        if pk == i.sno:
            x = i.movie
            print(x)
    for i in theat:
        if x == i.second:
            y.append(i.name)
    pk = str(pk)
    args = {'x': x, 'y': y, 'pk': pk,'second':'second'}
    return render(request, 'home/show.html', args)


def third(request,pk):
    x = ''
    y = []
    pk = int(pk)
    print(pk)
    movie = Movie.objects.all()
    theat = Theatre.objects.all()
    for i in movie:
        if pk == i.sno:
            x = i.movie
            print(x)
    for i in theat:
        if x == i.third:
            y.append(i.name)
    pk = str(pk)
    args = {'x': x, 'y': y, 'pk': pk,'third':'third'}
    return render(request, 'home/show.html', args)


def book_first(request,pk,theat):
    row=['A','B','C','D','E','F','G','H']
    col=['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13','s14','s15','s17']
    print(pk)
    pk=int(pk)
    x=''
    y=''
    text1=''
    text2=''
    book_row=[]
    book_col=[]
    movie=Movie.objects.all()
    for i in movie:
        if pk == i.sno:
            x = i.movie
            print(x)
    form = BookForm(request.POST)
    book = Book1.objects.all()
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.movie = x
        post.theatre = theat
        post.show_number = 'first'
        text1 = form.cleaned_data['row']
        text2 = form.cleaned_data['column']
        for i in book:
            if i.movie==x and i.theatre==theat and i.show_number=='first' and i.row==text1 and i.column==text2:
                return render(request,'home/booked_exep.html')
        post.save()
        form = BookForm()

    for i in book:
        if i.show_number=='first' and i.theatre==theat:
            book_row.append(i.row)
            book_col.append(i.column)
    print(book_row)
    print(book_col)

    args={'x':x,'pk':pk,'y':y,'text1':text1,'text2':text2,
          'row':row,'col':col,'show':'first','form':form,'theat':theat,
          'book_row':book_row,'book_col':book_col,
          }
    return render(request,'home/bookmyshow.html',args)

def book_second(request,pk,theat):
    row = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    col=['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13','s14','s15','s17']
    print(pk)
    pk = int(pk)
    x = ''
    y = ''
    text1 = ''
    text2 = ''
    book_row = []
    book_col = []
    movie = Movie.objects.all()
    for i in movie:
        if pk == i.sno:
            x = i.movie
            print(x)
    book = Book1.objects.all()
    form = BookForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.movie = x
        post.theatre = theat
        post.show_number = 'second'
        text1 = form.cleaned_data['row']
        text2 = form.cleaned_data['column']
        for i in book:
            if i.movie==x and i.theatre==theat and i.show_number=='second' and i.row==text1 and i.column==text2:
                return render(request,'home/booked_exep.html')
        post.save()
        form = BookForm()

    for i in book:
        if i.show_number == 'second' and i.theatre == theat:
            book_row.append(i.row)
            book_col.append(i.column)
    print(book_row)
    print(book_col)

    args = {'x': x, 'pk': pk, 'y': y,'text1': text1,'text2': text2,
            'row':row,'col':col,'show':'second','form':form,'theat':theat,
            'book_row': book_row, 'book_col': book_col,
            }
    return render(request, 'home/bookmyshow.html', args)


def book_third(request,pk,theat):
    row = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    col=['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13','s14','s15','s17']
    print(pk)
    pk = int(pk)
    x = ''
    y = ''
    text1 = ''
    text2 = ''
    book_row = []
    book_col = []
    movie = Movie.objects.all()
    for i in movie:
        if pk == i.sno:
            x = i.movie
            print(x)
    book = Book1.objects.all()

    form = BookForm(request.POST)
    if form.is_valid():
        post=form.save(commit=False)
        post.user=request.user
        post.movie=x
        post.theatre=theat
        post.show_number='third'
        text1 = form.cleaned_data['row']
        text2 = form.cleaned_data['column']
        for i in book:
            if i.movie==x and i.theatre==theat and i.show_number=='third' and i.row==text1 and i.column==text2:
                return render(request,'home/booked_exep.html')
        post.save()
        form = BookForm()

    for i in book:
        if i.show_number == 'third' and i.theatre == theat:
            book_row.append(i.row)
            book_col.append(i.column)
    print(book_row)
    print(book_col)

    args = {'x': x, 'pk': pk, 'y': y, 'text1': text1, 'text2': text2, 'show': 'third',
            'form': form,
            'row':row,'col':col,'theat': theat,
            'book_row': book_row, 'book_col': book_col,
            }
    return render(request, 'home/bookmyshow.html', args)
