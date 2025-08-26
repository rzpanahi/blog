from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from taggit.models import Tag, TaggedItem

from .models import Post


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated


class TagSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        published_posts = Post.published.all()
        tagged_items = TaggedItem.objects.filter(object_id__in=published_posts.values_list("id", flat=True), content_type__model='post')
        return Tag.objects.filter(id__in=tagged_items.values_list("tag_id", flat=True)).distinct()
    
    def location(self, obj):
        return reverse('blog:post_list_by_tag', args=[obj.slug])