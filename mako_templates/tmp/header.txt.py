# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1376576188.682428
_enable_loop = True
_template_filename = 'docs/header.txt'
_template_uri = 'header.txt'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        locals = context.get('locals', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'hello \n  ')
        # SOURCE LINE 2
        __M_writer(unicode(locals()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


