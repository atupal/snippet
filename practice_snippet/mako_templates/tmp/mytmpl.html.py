# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1376575235.451807
_enable_loop = True
_template_filename = './mytmpl.html'
_template_uri = 'mytmpl.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        name = context.get('name', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'hello ')
        __M_writer(unicode(name))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


