
from django.http import HttpResponse
from .models import Viloyatlar

def index(request):
    s = "<h1>Viloyatlar</h1>"

    for vil in Viloyatlar.objects.all():
        s += f"<h2>Viloyat: {vil.title}</h2>\n"
        s += f"<p>{vil}</p>\n"

        tumanlar = vil.tumanlar_set.all()
        for tum in tumanlar:
            s += f"<h3>&nbsp;&nbsp;Tuman: {tum.title}</h3>\n"
            s += f"<p>&nbsp;&nbsp;{tum}</p>\n"


            mahallalar = tum.mahallalar_set.all()
            for mah in mahallalar:
                s += f"<h4>&nbsp;&nbsp;&nbsp;&nbsp;Mahalla: {mah.title}</h4>\n"
                s += f"<p>&nbsp;&nbsp;&nbsp;&nbsp;{mah}</p>\n"
            s += "<hr>\n"
        s += "<hr><br>\n"

    return HttpResponse(s)

