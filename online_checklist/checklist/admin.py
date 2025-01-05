from django.contrib import admin
from .models import ChecklistItem
from django.core.exceptions import PermissionDenied
import logging
from .models import CustomUser


logger = logging.getLogger(__name__)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(ChecklistItem)
class ChecklistItemAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view (removed 'category')
    list_display = ('title', 'completed', 'phone_number', 'created_date', 'user')
    list_filter = ('completed', 'created_date', 'user')  # Removed 'category' from filters
    search_fields = ('title', 'phone_number')  # Allow search by title or phone number

    # Specify editable fields in the admin form (removed 'category')
    fields = ('title', 'completed', 'phone_number', 'user', 'created_date')
    readonly_fields = ('created_date',)  # Make certain fields read-only if needed

    def get_readonly_fields(self, request, obj=None):
        logger.debug(f"get_readonly_fields called for obj: {obj}")
        if obj and obj.completed and not request.user.is_superuser:
            logger.debug("User is not superuser and item is completed, making fields read-only.")
            return self.readonly_fields + ('title', 'phone_number', 'user')
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        logger.debug(f"save_model called for obj: {obj}, by user: {request.user}")
        if obj.completed and not request.user.is_superuser:
            logger.debug("Permission denied for non-superuser trying to edit a completed item.")
            raise PermissionDenied("You cannot edit completed items.")
        super().save_model(request, obj, form, change)