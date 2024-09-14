from django.shortcuts import render
from .models import ashuvarity, Store  # Make sure to import Store model if it exists
from django.shortcuts import get_object_or_404
from .forms import ashuvarityform

def all_ashu(request):
    ashus = ashuvarity.objects.all()
    return render(request, 'ashu/all_ashu.html', {'ashus': ashus})

def ashu_detail(request, ashu_id):
    ashu = get_object_or_404(ashuvarity, pk=ashu_id)
    return render(request, 'ashu/ashu_detail.html', {'ashu': ashu})

def ashu_store_view(request):
    stores = None
    if request.method == 'POST':
        form = ashuvarityform(request.POST)
        if form.is_valid():
            ashu_variety = form.cleaned_data['ashu_varity']
            # Assuming 'Store' is the model related to 'ashu_variety'
            stores = Store.objects.filter(ashu_varieties=ashu_variety)
    else:
        form = ashuvarityform()

    return render(request, 'ashu/ashu_stores.html', {'stores': stores, 'form': form})
