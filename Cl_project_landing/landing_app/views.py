from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from scripts import receiptsner
from .models import Input
from scripts.receiptsner import get_entities


from django.shortcuts import render
from .forms import ImageForm


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            if img_obj.photo.path[-4:] != 'None':
                receipt_date, total_amount, supplier_name, supplier_address = get_entities(img_obj.photo.path)
                return render(request, 'landing/index.html', {'form': form, 'img_obj': img_obj, "receipt_date": receipt_date,
                                                              "total_amount": total_amount, "supplier_name": supplier_name,
                                                              'supplier_address': supplier_address})
    else:
        form = ImageForm()
    return render(request, 'landing/index.html', {'form': form})

