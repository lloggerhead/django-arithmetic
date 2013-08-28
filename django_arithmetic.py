from django import template
register = template.Library()


class OperateError(Exception):
    pass


class ArithmeticNode(template.Node):
    assign_op = ('=', '+=', '-=', '/=', '*=', '%=', '**=')
    simple_op = ('+', '-', '*', '/', '%', '**')

    def __init__(self, parts):
        # {% op var_a <op> var_b %}
        self.var_a = parts[0]
        self.var_b = parts[2]
        self.op = parts[1]

    def is_assignment(self):
        return self.op == '='

    def is_assign_op(self):
        return self.op in self.assign_op

    def is_legal_op(self):
        return self.is_assign_op() or self.op in self.simple_op

    # return True if '{{ var }}' is int or float
    def is_legal_type(self, var):
        try:
            int(var)
        except ValueError:
            try:
                float(var)
            except ValueError:
                return False
        return True

    def get_value(self):
        try:
            # equal '{{ var_a }}'
            self.value_a = template.Variable(self.var_a).resolve(self.context)
            if not self.is_legal_type(self.value_a):
                raise TypeError
        except (TypeError, template.VariableDoesNotExist) as e:
            self.value_a = None
        try:
            # equal '{{ var_a }}'
            self.value_b = template.Variable(self.var_b).resolve(self.context)
            if not self.is_legal_type(self.value_b):
                raise TypeError
        except (TypeError, template.VariableDoesNotExist) as e:
            self.value_b = None

    def is_lvalue_exist(self):
        return self.value_a != None

    def is_rvalue_exist(self):
        return self.value_b != None

    def calculate(self):
        if self.is_assignment():
            self.context[self.var_a] = self.value_b
        else:
            value = eval("%s %s %s" %
                         (self.value_a, self.op.rstrip('='), self.value_b), {"__builtins__": None}, {})
            if not self.is_assign_op():
                # show operate result, like '{% op 1 + 1 %}'
                return str(value)
            self.context[self.var_a] = value
        return u''

    def render(self, context):
        try:
            if not self.is_legal_op():
                raise OperateError
            self.context = context
            self.get_value()
            if not self.is_rvalue_exist():
                raise ValueError
            if not self.is_lvalue_exist() and not self.is_assignment():
                raise ValueError
            return self.calculate()
        except (TypeError, ValueError, OperateError) as e:
            raise e


# tags
# Useage:
#   {% op foo = 147 %}
#   {% op foo + 10 %}
#   {% op foo -= 10 %}
@register.tag(name="op")
def do_arithmetic(parser, token):
    """{% op <var_a> <op> <var_b> %}"""
    parts = token.split_contents()
    if len(parts) != 4:
        raise template.TemplateSyntaxError(
            "'%s' tag must be of the form:  {%% %s <var_a> %s <var_b> %%}" % (parts[0], parts[2], parts[0]))
    return ArithmeticNode(parts[1:])

# filter
# Useage:
#   {{ 147|add }}
#   {{ 147|add:1 }}


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
