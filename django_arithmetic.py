from django import template
register = template.Library()


class DefineNode(template.Node):

    def __init__(self, var):
        self.var = var

    def render(self, context):
        context[self.var] = 0
        return u''


class DeleteNode(template.Node):

    def __init__(self, var):
        self.var = var

    def render(self, context):
        try:
            del context[self.var]
        except NameError:
            pass
        finally:
            return u''


class IncreaseNode(template.Node):

    def __init__(self, var):
        self.var = var

    def render(self, context):
        try:
            value = int(template.Variable(self.var).resolve(context))
        except ValueError, VariableDoesNotExist:
            pass
        else:
            context[self.var] = value + 1
        finally:
            return u''


class DecreaseNode(template.Node):

    def __init__(self, var):
        self.var = var

    def render(self, context):
        try:
            value = int(template.Variable(self.var).resolve(context))
        except ValueError, VariableDoesNotExist:
            pass
        else:
            context[self.var] = value - 1
        finally:
            return u''


class ArithmeticNode(template.Node):
    from operator import *

    base_op = {
        '+': add, '-': sub, '*': mul, '/': div,
        '%': mod, '**': pow, '//': floordiv
    }

    def __init__(self, var_a, op, var_b):
        # {% op <var_a> <op> <var_b> %}
        self.var_a = var_a
        self.var_b = var_b
        self.op = op
        if not self.is_legal_op():
            raise template.TemplateSyntaxError("Illegal operate '%s'" % self.op)

    def is_legal_op(self):
        return self.op == '=' or self.op.rstrip('=') in self.base_op.keys()

    def is_assignable_op(self):
        return self.is_legal_op() and '=' in self.op

    def render(self, context):
        try:
            # get '{{ var_b }}' value
            value_b = int(template.Variable(self.var_b).resolve(context))
        except (ValueError, NameError, template.VariableDoesNotExist):
            return u''
        if self.op != '=':
            try:
                value_a = int(template.Variable(self.var_a).resolve(context))
            except (ValueError, NameError, template.VariableDoesNotExist):
                return u''
            # calculate expression 'value_a op value_b', such as '{% op 1 + 2 %}'
            value_b = self.base_op[self.op.rstrip('=')](value_a, value_b)
        if self.is_assignable_op():
            context[self.var_a] = value_b
            return u''
        else:
            return value_b


def get_one_arg(token):
    parts = token.split_contents()
    if len(parts) != 2:
        raise template.TemplateSyntaxError(
            "Useage: {%% %s <foo> %%}" % parts[0])
    return parts[1]

# Useage:
#   {% var foo %}
@register.tag(name="var")
def do_define(parser, token):
    return DefineNode(get_one_arg(token))

# Useage:
#   {% del foo %}
@register.tag(name="del")
def do_delete(parser, token):
    return DeleteNode(get_one_arg(token))

# Useage:
#   {% inc foo %}
@register.tag(name="inc")
def do_increase(parser, token):
    return IncreaseNode(get_one_arg(token))

# Useage:
#   {% dec foo %}
@register.tag(name="dec")
def do_decrease(parser, token):
    return DecreaseNode(get_one_arg(token))

# Useage:
#   {% op foo = 147 %}
#   {% op foo + 10 %}
#   {% op foo -= 10 %}
@register.tag(name="op")
def do_arithmetic(parser, token):
    parts = token.split_contents()
    if len(parts) != 4:
        raise template.TemplateSyntaxError(
            "Useage: {%% %s <var_a> <op> <var_b> %%}" % parts[0])
    return ArithmeticNode(parts[1], parts[2], parts[3])
