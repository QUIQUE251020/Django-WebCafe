from .models import Page


def page_info(request):
  page_info = Page.objects.all()
  return {'page_info':page_info}