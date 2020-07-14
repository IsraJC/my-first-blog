from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from. models import CV
from .forms import CVForm
from .models import WorkExperience
from .forms import WorkExperienceForm
from .models import Education
from .forms import EducationForm
from .models import Activity
from .forms import ActivityForm
from django.shortcuts import redirect

# Create your views here.
def home_page(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
	return render(request, 'blog/home_page.html', {'posts': posts})

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            text = form.cleaned_data['text']
            post.summary = text.splitlines()[0]
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            text = form.cleaned_data['text']
            post.summary = text.splitlines()[0]
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('post_list')

def cv_page(request, pk):
	cv = get_object_or_404(CV, pk=pk)
	work_experience = reversed(WorkExperience.objects.all())
	education = reversed(Education.objects.all())
	activities = reversed(Activity.objects.all())
	return render(request, 'blog/cv_page.html', {'cv':cv, 'work_experience': work_experience, 'education': education, 'activities': activities})