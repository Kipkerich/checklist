from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import ChecklistItem
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ChecklistItemForm

# Homepage view
def index(request):
    return render(request, 'index.html')

# Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('add_item')  # Redirect to the checklist page
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Login view
def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('add_item')  # Redirect to the checklist page
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Logout view
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page


@login_required
def checklist(request):
    if request.method == "POST":
        item_id = request.POST.get("item_id")
        action = request.POST.get("action")

        if action == "mark_complete":
            item = get_object_or_404(ChecklistItem, id=item_id, user=request.user)
            item.completed = True
            item.save()

        elif action == "delete":
            item = get_object_or_404(ChecklistItem, id=item_id, user=request.user)
            item.delete()

    # Filter items to show only those not completed
    items = ChecklistItem.objects.filter(user=request.user, completed=False)
    return render(request, "checklist/checklist.html", {"items": items})


# View checklist items
@login_required
def view_checklist(request):
    completed_items = ChecklistItem.objects.filter(user=request.user, completed=True)
    return render(request, "checklist/view_checklist.html", {"completed_items": completed_items})

# Add a checklist item
@login_required
def add_item(request):
    if request.method == 'POST':
        form = ChecklistItemForm(request.POST)
        if form.is_valid():
            # Save the new checklist item and associate it with the logged-in user
            checklist_item = form.save(commit=False)
            checklist_item.user = request.user  # Assign the logged-in user
            checklist_item.save()
            return redirect('checklist')  # Redirect to a success page after saving
    else:
        form = ChecklistItemForm()

    # Retrieve all checklist items created by the logged-in user
    checklist_items = ChecklistItem.objects.filter(user=request.user) 

    return render(request, 'checklist/checklist.html', {'form': form})

# Mark item as complete
@login_required
def complete_item(request, item_id):
    item = get_object_or_404(ChecklistItem, id=item_id, user=request.user)
    item.is_completed = True  # Assuming an `is_completed` field exists in the model
    item.save()
    return redirect('checklist')

# Delete an item
@login_required
def delete_item(request, item_id):
    item = get_object_or_404(ChecklistItem, id=item_id, user=request.user)
    item.delete()
    return redirect('checklist')
