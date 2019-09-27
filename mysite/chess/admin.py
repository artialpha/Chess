from django.contrib import admin
from django.http import HttpResponseRedirect
import wikipedia
from .models import *
from django.urls import path
import csv
from django.contrib.staticfiles.storage import staticfiles_storage
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
        #chess_open = wikipedia.page("List_of_chess_openings")
        print("tutaj zydzie")
        p = staticfiles_storage.path("ECO/a.tsv")
        with open(p) as fd:
            rd = csv.reader(fd, delimiter="\t", quotechar='"')
            print("w srodku")
            for row in rd:
                print(row[2])

        return HttpResponseRedirect("../")


#"C:/Users/Dymitr/PycharmProjects/django/mysite/chess/static/chess/ECO/a.tsv"










