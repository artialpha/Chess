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
        path = "ECO/{}.tsv"
        for i in range(5):
            p = staticfiles_storage.path(path.format(chr(i+97)))
            with open(p) as fd:
                rd = csv.reader(fd, delimiter="\t", quotechar='"')
                #list_rd = list(rd)
                for row in rd:
                    chess_opening = ChessOpening(eco=row[0], name=row[1],
                                                 epd=row[2], algebraic_notation=row[3])
                    chess_opening.save()
                    print(row)

        return HttpResponseRedirect("../")


#"C:/Users/Dymitr/PycharmProjects/django/mysite/chess/static/chess/ECO/a.tsv"










