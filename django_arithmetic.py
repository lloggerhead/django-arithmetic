from django import template
register = template.Library()


class VarNode(template.Node):

    def __init__(self, var_name, var_value):
        self.var_name = var_name
        self.var_value = var_value

    def render(self, context):
        try:
            value = template.Variable(self.var_value).resolve(context)
        except template.VariableDoesNotExist:
            value = ""
        context[self.var_name] = value
        return u""


@register.tag(is_safe=False)
def var(parser, token):
    """{% var <var_name> = <var_value> %}"""
    parts = token.split_contents()
    if len(parts) < 4:
        raise template.TemplateSyntaxError(
            "'%s' tag must be of the form:  {% 'var' <var_name> = <var_value> %}" % parts[0])
    return SetVarNode(parts[1], parts[3])


@register.filter(is_safe=False)
def add(value, arg='1'):
    try:
        return int(value) + int(arg)
    except (ValueError, TypeError):
        try:
            return value + arg
        except Exception:
            return ''


@register.filter(is_safe=False)
def sub(value, arg='1'):
    try:
        return int(value) - int(arg)
    except (ValueError, TypeError):
        try:
            return value - arg
        except Exception:
            return ''


@register.filter(is_safe=False)
def mul(value, arg='0'):
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        try:
            return value * arg
        except Exception:
            return ''


@register.filter(is_safe=False)
def div(value, arg='100'):
    try:
        return int(value) / int(arg)
    except (ValueError, TypeError):
        try:
            return value / arg
        except Exception:
            return ''


@register.filter(is_safe=False)
def mod(value, arg='100'):
    try:
        return int(value) % int(arg)
    except (ValueError, TypeError):
        try:
            return value % arg
        except Exception:
            return ''
