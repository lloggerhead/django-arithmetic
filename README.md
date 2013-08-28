django-arithmetic
=================

Django template tags for basic arithmetic
###Useage:###
  ```
  {% <var> <op> <var|value> %}
  ```

###Example:###
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
###Result:###
  ```
  0 1 0 
  147 147 49 490 480
  ```
