django-arithmetic
=================

Django template filters for basic arithmetic

Useage:
  ```
  {% load arithmetic %}
  <!-- declare the variable 'a' -->
  {% var a = 147 %}
  <!-- 157 -->
  {{ a|add:10 }}
  <!-- 148 -->
  {{ a|add }}
  <!-- 137 -->
  {{ a|sub:10 }}
  <!-- 146 -->
  {{ a|sub }}
  <!-- 1470 -->
  {{ a|mul:10 }}
  <!-- 0 -->
  {{ a|mul }}
  <!-- 14 -->
  {{ a|div:10 }}
  <!-- 1 -->
  {{ a|div }}
  <!-- 7 -->
  {{ a|mod:10 }}
  <!-- 47 -->
  {{ a|mod }}
  ```
