"""
A set of request processors that return dictionaries to be merged into a
template context. Each function takes the request object as its only parameter
and returns a dictionary to add to the context.

These are referenced from the setting TEMPLATE_CONTEXT_PROCESSORS and used by
RequestContext.
"""

from biblion.settings import DISQUS_SHORTNAME

def default(request):
    "Returns context variables specific to biblion"

    context_extras = {
        "DISQUS_SHORTNAME" : DISQUS_SHORTNAME,
    }

    return context_extras
