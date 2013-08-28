django-arithmetic
=================

Django template tags and filters for basic arithmetic

###Example:###
  ```
  {% load arithmetic %}
  <!-- '=', '+=', '-=', '/=', '*=', '%=', '**=', '+', '-', '*', '/', '%', '**' -->
  {% op foo = 147 %}
  <!-- add, sub, mul, div -->
  {{ foo|add:10 }}
  {{ foo|add }}
  <!-- Notice: any don't change 'foo' operations will show operate result -->
  {% op foo + 10 %}
  {% op foo -= 10 %}
  {{ foo }}
  ```
###Result:###
  ```
  157 148 157 137
  ```
