from django import template
from slimit import minify

register = template.Library()


class MinifyNode(template.Node):

    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        return minify(
            self.nodelist.render(context),
            mangle=True,
            mangle_toplevel=True
        )


@register.tag
def minify_js(parser, token):
    nodelist = parser.parse(('endminify_js',))
    parser.delete_first_token()
    return MinifyNode(nodelist)
