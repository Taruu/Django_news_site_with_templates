from django.template import RequestContext

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
from django.shortcuts import render
from django.template.loader import render_to_string
from News_Site.forms import AddNews
from django.shortcuts import redirect


# View for 'Mods' model
class NewsView(View):

    def get(self, request, page=0):
        max_page = round(News.objects.count() / settings.NEWS_ON_PAGE)
        if page > max_page:
            page = max_page
        if page < 0:
            page = 0
        start = page * settings.NEWS_ON_PAGE
        end = start + settings.NEWS_ON_PAGE
        sort = request.GET.get('sort', 'new')
        list_news = News.objects.order_by(
            "-created_at" if sort == "new" else "created_at").all()[start:end]

        # Мне нужно спать. так что простите за решение в лоб
        backpage = page - 1
        backpage = backpage if backpage >= 0 else 0
        nextpage = page + 1
        nextpage = nextpage if nextpage <= max_page else max_page
        return render(request, 'News_Site/news.html',
                      {"list_news": list_news, "nextpage": nextpage,
                       "backpage": backpage, "sort": sort,
                       "change": "new" if sort == "old" else "old"})


class NewsPage(View):
    def get(self, request, news_id=0):
        news = News.objects.get(pk=news_id)
        if not news:
            return
        return render(request, 'News_Site/news_page.html',
                      {"news": news})


class NewsAdd(View):

    def get(self, request, news_id=0):
        form = AddNews()
        response = render_to_string('News_Site/news_add.html',
                                    {"form": form},
                                    request=request)
        return HttpResponse(response)

    def post(self, request):
        form = AddNews(request.POST, request.FILES)
        if form.is_valid():
            form_values = form.cleaned_data
            news = News(name=form_values["name"],
                        content=form_values["content"],
                        image=form_values["image"])
            news.save()
            print(news.pk)
            return redirect(f"/news/page/{news.pk}")

        pass
