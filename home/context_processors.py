from .models import Variety


def extras(request):
    """
    Show categories list in the entire application
    """
    varieties = Variety.objects.all()
    context = {
        'cat_menu': varieties
    }

    return context
