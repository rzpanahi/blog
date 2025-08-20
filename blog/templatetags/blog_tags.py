from django import template
from django.db.models import Count

from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag("blog/post/latest_posts.html")
def latest_posts(count=4):
    latest_posts = Post.published.order_by("-publish")[:count]
    return {
        "latest_posts": latest_posts,
    }


@register.inclusion_tag("blog/post/most_commented.html")
def most_commented(count=4):
    most_commented_posts = Post.published.annotate(
        comments_count=Count("comments")
    ).order_by("-comments_count")[:count]

    return {
        "most_commented_posts": most_commented_posts
    }
