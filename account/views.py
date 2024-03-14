# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from account.forms import GroupForm, UserProfileForm
from account.models import CustomGroup


def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in.')
            return redirect('index')  # Change 'index' to your desired redirect path
        else:
            print("muvaffaqiyatsiz")
            messages.error(request, 'Invalid email or password.')
    return render(request, 'register/login.html')  # Change 'your_app' to your app name


@login_required
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data['name']
            # tekshirish: agar kiritilgan nom bazada mavjud bo'lsa, uni o'zgartirishni so'rab qo'ymaslik uchun
            existing_group = Group.objects.filter(name=group_name).first()
            if existing_group:
                return render(request, 'create_group.html', {'form': form,
                                                             'error_message': 'Bu nom bilan guruh mavjud, iltimos boshqa nom kiriting.'})

            group = form.save(commit=False)
            base_group = Group.objects.create(name=group_name)
            group.base_group = base_group
            group.save()
            form.save_m2m()
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'create_group.html', {'form': form})


@login_required
def group_list(request):
    groups = CustomGroup.objects.all()
    return render(request, 'group_list.html', {'groups': groups})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})