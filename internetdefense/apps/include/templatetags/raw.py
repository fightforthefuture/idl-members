from django import template
register = template.Library()


@register.tag
def raw(parser, token, block=[]):
    """
    Block-level template tag that renders the contents of the tag unparsed.
    This is useful when including Handlebars.js templates.

    {% raw %}
        {{ handlebar_expression }}
    {% endraw %}
    """
    close = 'endraw'
    tokens = {
        template.TOKEN_TEXT: ('', ''),
        template.TOKEN_VAR: ('{{', '}}'),
        template.TOKEN_BLOCK: ('{%', '%}'),
        template.TOKEN_COMMENT: ('{#', '#}'),
    }
    while parser.tokens:
        token = parser.next_token()
        if token.token_type == template.TOKEN_BLOCK and token.contents == close:
            return template.TextNode(u''.join(block))
        start, end = tokens[token.token_type]
        block.append(u'%s%s%s' % (start, token.contents, end))
    parser.unclosed_block_tag(close)
