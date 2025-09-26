from django.shortcuts import render, get_object_or_404, redirect
from .models import ServiceCategory, Service, Package, PortfolioItem, Booking
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def services_list(request):
    cats = ServiceCategory.objects.prefetch_related('services').all()
    selected = request.GET.get('category')
    services = Service.objects.all()
    if selected:
        services = services.filter(category__id=selected)  # ✅ This is fine (Category still has slug)
    return render(request, 'events/services.html', {
        'categories': cats,
        'services': services,
        'selected': selected
    })

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'events/service_detail.html', {'service': service})

def packages_list(request):
    packages = Package.objects.all()
    return render(request, 'events/packages.html', {'packages': packages})

def portfolio(request):
    items = PortfolioItem.objects.all()
    return render(request, 'events/portfolio.html', {'items': items})

@login_required(login_url='/login/')
def book_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    packages = Package.objects.all()
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        pkg = request.POST.get('package')
        reqs = request.POST.get('requests', '')

        package = Package.objects.filter(pk=pkg).first() if pkg else None
        Booking.objects.create(
            user=request.user,
            service=service,
            package=package,
            date=date,
            time=time,
            requests=reqs
        )
        messages.success(request, 'Your booking has been successfully confirmed!')
        return redirect('events:booking_success')
    return render(request, 'events/booking.html', {'service': service, 'packages': packages})

def booking_success(request):
    return render(request, 'events/booking_success.html')
