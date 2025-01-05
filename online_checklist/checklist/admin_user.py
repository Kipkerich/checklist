from django.shortcuts import render, redirect, get_object_or_404
from .models import ChecklistItem
from .forms import ChecklistItemEditForm
from django.contrib.auth.decorators import user_passes_test

# Helper function to check if the user is an admin
def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def verify_checklist(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        item_id = request.POST.get('item_id')
        item = get_object_or_404(ChecklistItem, id=item_id)

        if action == 'mark_complete':
            item.completed = True
            item.save()
        elif action == 'mark_verified':
            item.verified = True  # Mark the item as verified
            item.save()
        elif action == 'delete':
            item.delete()

    # Get all items (admin can view all items)
    items = ChecklistItem.objects.all()
    return render(request, 'checklist/verify_checklist.html', {'items': items})
