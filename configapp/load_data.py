from configapp.models import Viloyatlar, Tumanlar, Mahallalar
import datetime
now = int(datetime.datetime.now().year)
viloyatlar = []
viloyat_nomi = ["Toshkent", "Samarqand", "Farg'ona"]
for nom in viloyat_nomi:
    v = Viloyatlar.objects.create(title=nom, context=f"{nom} haqida")
    viloyatlar.append(v)
for viloyat in viloyatlar:
    for i in range(1, 4):
        tuman_nomi = f"{viloyat.title} Tuman {i}"
        tuman = Tumanlar.objects.create(
            title=tuman_nomi,
            context=f"{tuman_nomi} haqida",
            viloyat=viloyat,
            created_at=now,
            updated_at=now
        )
        for j in range(1, 4):
            mahalla_nomi = f"{tuman.title} Mahalla {j}"
            Mahallalar.objects.create(
                title=mahalla_nomi,
                context=f"{mahalla_nomi} haqida",
                tumanlar=tuman,
                created_at=now,
                updated_at=now
            )
