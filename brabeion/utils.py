from django.conf import settings


def get_brabeion_user(user):
    if getattr(settings, 'BRABEION_BRABEION_USER_FROM_DJANGO_USER_METHOD', None):
        attrs = settings.BRABEION_BRABEION_USER_FROM_DJANGO_USER_METHOD.split(".")
        method = user
        for a in attrs:
            method = getattr(method, a)
        return method()[0]
    return user

def get_django_user(brabeion_model):
    if getattr(settings, 'BRABEION_DJANGO_USER_FROM_BRABEION_USER_METHOD', None):
        attrs = settings.BRABEION_DJANGO_USER_FROM_BRABEION_USER_METHOD.split(".")
        method = user
        for a in attrs:
            method = getattr(obj, a)
        return method()[0]
    return brabeion_model