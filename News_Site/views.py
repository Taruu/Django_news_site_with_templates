from News_Site.models import News
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
import json
from django.contrib.auth.hashers import make_password
from django.db.utils import IntegrityError
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


# View for 'Mods' model
class NewsView(View):

    def get(self, request, page=0):
        start = page * settings.NEWS_ON_PAGE
        end = start + settings.NEWS_ON_PAGE
        sort = request.GET.get('sort', 'new')
        list_news = News.objects.order_by(
            "-created_at" if sort == "new" else "created_at").all()[start:end]
        response = render_to_string('News_Site/index.html')

        return HttpResponse(response)
