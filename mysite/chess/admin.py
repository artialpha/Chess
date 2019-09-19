from django.contrib import admin
from django.http import HttpResponseRedirect

from .models import *
from django.urls import path
# Register your models here.


admin.site.register(Variant)


@admin.register(ChessOpening)
class ChessOpeningAdmin(admin.ModelAdmin):
    change_list_template = "admin/chess_open_add.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('immortal/', self.add),
        ]
        return my_urls + urls

    def add(self, request):
        print("buahahuah")
        return HttpResponseRedirect("../")













