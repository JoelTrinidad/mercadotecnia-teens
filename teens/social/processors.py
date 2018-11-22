from .models import Link

def extensionDC(request):
    ext = {}
    links = Link.objects.all()
    for link in links:
        ext[link.key] = link.url
    return ext