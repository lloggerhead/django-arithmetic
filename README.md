Django template tags for basic arithmetic
=================
Usage:
-----------------
  The legel operations include __"+ - \* / % \*\* //"__ and __"= += -= ..."__  
  **Notice: the output is same as console**
  ```
  {% <var> <op> <var|value> %}
  ```
  Corresponding relation:  
  __'var foo' ==> 'foo=0'__  
  __'inc' or 'dec' ==> '+1' or '-1'__
  ```
  {% (var|del|inc|dec) <var_name> %}
  ```
Example:
-----------------
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
Output:
-----------------
  ```
  0 1 0 
  147 147 49 490 480
  ```
