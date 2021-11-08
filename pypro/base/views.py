from django.http import HttpResponse


def home(request):
    return HttpResponse('<html> <body> <h3> Olá Django </h3> </body> </html>', content_type='text/html')
