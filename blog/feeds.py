from markdown import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy

from .models import Post


class LatestPostFeed(Feed):

    title = "Reza Panahi's Blog"
    link = reverse_lazy("blog:post_list")
    description = "Recent Posts of my Blog"


    def items(self):
        return Post.published.all()[0:5]

    
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html(markdown(item.body), 50)
    
    def item_pubdate(self, item):
        return item.publish