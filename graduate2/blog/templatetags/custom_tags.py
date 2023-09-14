from django import template

register = template.Library()


@register.filter
def is_owner(user, post):
    return user == post.owner


@register.simple_tag(name='mediapath')
def get_media_path_tag(image_path):

    if image_path:
        return f"/media/post/{image_path}"

    return 'No image'