def categories(request):
    try:
        from events.models import ServiceCategory
        cats = ServiceCategory.objects.all()
    except Exception:
        cats = []
    return {'categories': cats}
