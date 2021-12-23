from django.shortcuts import get_object_or_404, redirect, render
from .models import Review
from .forms import ReviewForm
# Create your views here.


def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('articles:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/form.html',context)
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews' : reviews
    }
    return render(request, 'articles/index.html', context)

def detail(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)
    context={
        'review' : review
    }
    return render(request, 'articles/detail.html', context)

def update(request,review_pk):
    review = get_object_or_404(Review, pk = review_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect('articles:detail',review.pk)
    else:
        form = ReviewForm(instance = review)
    context = {
        'form' : form
    }
    return render(request, 'articles/form.html', context)

def delete(request,review_pk):
    if request.method == 'POST':
        review = get_object_or_404(Review, pk = review_pk)
        review.delete()
    return redirect('articles:index')