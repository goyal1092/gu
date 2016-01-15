from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.views import generic
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.sites.models import Site
from django.utils.html import strip_tags
import logging

from . import models
from . import settings
from . import utils
from .forms import ArticleListForm


from blocks.models import Group

logger = logging.getLogger(__name__)

class ArticleList(generic.ListView):
   context_object_name = 'article_list'
   template_name = "newsroom/article_list.html"
   paginate_by = settings.ARTICLES_PER_PAGE

   def get_queryset(self):
      return models.Article.objects.list_view()

class HomePage(ArticleList):
   template_name = "newsroom/home.html"
   def get_context_data(self, **kwargs):
      context = super(HomePage, self).get_context_data(**kwargs)
      # Add extra context for the home page here
      # ...
      try:
         blocks = Group.objects.get(name="Home").get_blocks()
      except:
         blocks = []
      context["blocks"] = blocks
      return context

   def get(self, request, *args, **kwargs):
      # Add messages here. E.g.
      #messages.add_message(request, messages.INFO,
      #                     "We are closed until 5 January.")
      request = super(HomePage, self).get(request, args, kwargs)
      return request

class OpinionAnalysisList(ArticleList):
   def get_queryset(self):
      return models.Article.objects.list_view().filter(
         Q(category__name="Opinion") |
         Q(category__name="Analysis"))

   def get_context_data(self, **kwargs):
      context = super(OpinionAnalysisList, self).get_context_data(**kwargs)
      context['heading'] = "Opinion and Analysis"
      return context

class AuthorDetail(ArticleList):

   def get_queryset(self):
      self.author = get_object_or_404(models.Author, pk=self.args[0])
      return models.Article.objects.list_view().filter(
         Q(author_01=self.author) | Q(author_02=self.author) | \
         Q(author_03=self.author) | Q(author_04=self.author) | \
         Q(author_05=self.author) |
         Q(cached_byline_no_links__icontains=str(self.author)))

   def get_context_data(self, **kwargs):
      context = super(AuthorDetail, self).get_context_data(**kwargs)
      context['heading'] = "Articles by " + str(self.author)
      context['image'] = self.author.photo
      context['description'] = self.author.description
      return context



class CategoryDetail(ArticleList):
   def get_queryset(self):
      self.category = self.args[0]
      return models.Article.objects.list_view().filter(category=self.category)

   def get_context_data(self, **kwargs):
      context = super(CategoryDetail, self).get_context_data(**kwargs)
      context['heading'] = self.category
      return context


class RegionDetail(ArticleList):
   def get_queryset(self):
      self.region = get_object_or_404(models.Region, path=self.args[0])
      return models.Article.objects.list_view(). \
      filter(Q(region__in=self.region.get_descendants()) | \
             Q(region=self.region))

   def get_context_data(self, **kwargs):
      context = super(RegionDetail, self).get_context_data(**kwargs)
      context['heading'] = "Region: " + str(self.region)
      return context


class TopicDetail(ArticleList):
   def get_queryset(self):
      self.topic = get_object_or_404(models.Topic, slug=self.args[0])
      return models.Article.objects.published(). \
         filter(topics=self.topic)

   def get_context_data(self, **kwargs):
      context = super(TopicDetail, self).get_context_data(**kwargs)
      context['heading'] = "Topic: " + self.topic.name
      return context


class ArticleDetail(View):
   def get(self, request, slug):
      article = get_object_or_404(models.Article, slug=slug)
      if article.is_published() or request.user.is_staff:
         if request.user.is_staff and not article.is_published():
            messages.add_message(request, messages.INFO,
                            "This article is not published.")
         if article.region and article.region.name not in ["None", ""]:
            display_region = article.region.name.rpartition("/")[2]
         else:
            display_region = ""
         return render(request, article.template,
                       {'article': article,
                        'display_region': display_region})
      else:
         raise Http404


''' Redirect images on old Drupal site
'''
class RedirectOldImages(View):
   def get(self, request, path):
      url = "/media/old/" + path
      return redirect(url)

'''Redirect hand constructed features (mainly an old site phenomenon

'''
class RedirectHandConstructedFeatures(View):
   def get(self, request, path):
      url = "/media/features/" + path
      return redirect(url)

'''Redirect old /content/ articles to new /article/

'''
class RedirectContentToArticle(View):
   def get(self, request, path):
      url = "/article/" + path
      return redirect(url)


'''newsletter generator form
'''

@staff_member_required
def generate_article_list(request):
   output = []
   articles = []
   if request.method == "POST":
      form = ArticleListForm(request.POST)
      if form.is_valid():
         date_from = form.cleaned_data["date_from"]
         date_to = form.cleaned_data["date_to"]
         if date_to:
            articles = models.Article.objects.published(). \
                       filter(published__gte=date_from). \
                       filter(published__lte=date_to)
         else:
            articles = models.Article.objects.published(). \
                       filter(published__gte=date_from)
         site_url = 'http://' + Site.objects.get_current().domain
         for article in articles:
            output.append("<h3><a href='" + site_url + \
                          article.get_absolute_url() + \
               "'>" + article.title +"</a></h3>")
            output.append("<p>" + strip_tags(article.cached_summary_text) + "</p>")
            output.append("<p style='font-style:italic;'>" + article.cached_byline_no_links + "</p>\n")
   else:
      form = ArticleListForm()

   return render(request, "newsroom/article_list_form.html",
                 {'form':form,
                  'output': output,
                  'len_articles': len(articles)})

''' Used to test logging
'''

def testLoggingDebug():
    logger.debug("Debug logging test")

def testLoggingInfo():
    logger.debug("Info logging test")

def testLoggingWarning():
    logger.debug("Warning logging test")

def testLoggingError():
    logger.error("Error logging test")

def testLoggingCritical():
    logger.critical("Critical logging test")

def testLoggingAll():
   testLoggingDebug()
   testLoggingInfo()
   testLoggingWarning()
   testLoggingError()
   testLoggingCritical()
