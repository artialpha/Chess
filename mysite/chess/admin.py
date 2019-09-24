from django.contrib import admin
from django.http import HttpResponseRedirect
import wikipedia
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
        chess_open = wikipedia.page("List_of_chess_openings")
        print(chess_open.section)
        return HttpResponseRedirect("../")













