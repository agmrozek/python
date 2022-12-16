# [your_app]/templatetags/tags.py

from django import template
register = template.Library()

@register.simple_tag(takes_context=True)
def set_breakpoint(context):
    breakpoint()


# in template
{% load tags %}
...
{% set_breakpoint %}
{% for error in form.non_field_errors %}
  {{error}}
{% endfor %}


# inspecting form in pdb ... ok I need to look at errors, not only non_field_errors

(Pdb) vars(context)['dicts'][3]['form'].errors.as_ul()
'<ul class="errorlist"><li>password2<ul class="errorlist"><li>The two password fields didn&#39;t match.</li></ul></li></ul>'