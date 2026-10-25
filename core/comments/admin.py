from django.contrib import admin
from .models import Comment

# Register your models here.

class ReplyCommentInlineAdmin(admin.StackedInline):
    model = Comment
    extra = 0
    verbose_name = "reply"
    verbose_name_plural = "replies"
    show_change_link = True


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id","user__email","product__id","replyed__id"]
    search_fields = ["user__username","user__email","product__name","id"]
    inlines = [ReplyCommentInlineAdmin]

