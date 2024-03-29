from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import  HttpResponse
from django.template import loader
from .models import Board, Comment
from .forms import BoardForm, CommentForm

# Create your views here.
# board=[
#     {'id': 1, 'title': 'title1', 'content': 'content1'},
#     {'id': 2, 'title': 'title2', 'content': 'content2'},
#     {'id': 3, 'title': 'title3', 'content': 'content3'},
# ]

class IndexView(ListView):
    template_name = 'app/index.html'
    context_object_name = 'board'

    def get_queryset(self):
        return Board.objects.all()

# def index(request):
#     board = Board.objects.all()
#     context={
#         'board': board
#     }
#     return render(request, 'app/index.html', context)

class BoardView(DetailView):
    template_name = 'app/board.html'
    context_object_name = 'board'
    model = Board

    # def get_queryset(self):
    #     return Board.objects.filter(id=self.kwargs.get('pk'))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board'] = Board.objects.filter(id=self.kwargs.get('pk')).first()
        context['form'] = CommentForm
        return context

# def boardDetail(request, boardId):
#     retBoard = Board.objects.filter(id=boardId).first()
#     context={
#        'board': retBoard,
#     }
#     return render(request, 'app/board.html', context)

def newBoard(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/app')
    else:
        form = BoardForm()
        context={
            'form': form
        }
        return render(request, 'app/new.html', context)

def deleteBoard(request, pk):
    delBoard = Board.objects.filter(id=pk).first()
    delBoard.delete()
    return redirect('/app')

def newComment(request, pk):
    if request.method == 'POST':
        board = Board.objects.get(id=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.board = board
            comment.save()
        return redirect('/app/board/' + str(pk))