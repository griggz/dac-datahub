from django.http import HttpResponseRedirect


def portal_redirect(request):
    return HttpResponseRedirect("/admin/")
