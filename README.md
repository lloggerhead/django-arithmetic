Django template tags for basic arithmetic
=================
##Usage:##
  legel operations include "+ - \* / % \*\* //" and "= += -= ..."  
  notice: the output is same as console
  ```
  {% <var> <op> <var|value> %}
  ```
  below syntax will do some very simple operate  
  'var foo' same as 'foo = 0'
  'inc' or 'dec' equals '+ 1' or '- 1'
  ```
  {% (var|del|inc|dec) <var_name> %}
  ```
##Example:##
  ```
  {% load arithmetic %}
  <!-- simple operations  -->
  {% var foo %}    {{ foo }}
  {% inc foo %}    {{ foo }}
  {% dec foo %}    {{ foo }}
  {% del foo %}    {{ foo }}
  <br>
  <!-- base operations -->
  {% op foo = 147 %}    {{ foo }}
  {% op bar = 3 %}      {{ foo }}
  {% op foo //= bar %}  {{ foo }}
  {% op foo *= 10 %}    {{ foo }}
  {% op foo - 10 %}
  ```
##Result:##
  ```
  0 1 0 
  147 147 49 490 480
  ```
