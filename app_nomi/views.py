from django.shortcuts import render, redirect
from .models import Region, Country
from django.core.files.images import ImageFile
import os
from django.conf import settings

def create_region(request):
    countries = Country.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        country_id = request.POST.get('country')
        country = Country.objects.get(id=country_id)

        if not image:
            # 'media/default.jpg' faylidan ImageFile obyektini yaratamiz
            default_image_path = os.path.join(settings.MEDIA_ROOT, 'default.jpg')
            with open(default_image_path, 'rb') as f:
                image = ImageFile(f, name='default.jpg')

        Region.objects.create(
            title=title,
            image=image,
            country=country
        )

        return redirect('home')  # bu yerda o'zingizga mos URL nomi bo'lishi kerak

    return render(request, 'region_form.html', {'countries': countries})
