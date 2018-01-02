#!/bin/sh
# -*- coding: utf-8 -*-
''''which python2 >/dev/null && exec python2 "$0" "$@" # '''
''''which python  >/dev/null && exec python  "$0" "$@" # '''

import json

from pprint import pprint as p


def parse(source, debug=0):

    source = source.strip()

    stack = ['begin']
    media = []
    pos = 0
    length = len(source)

    def _skip_whitespace():
        nonlocal pos
        while pos < length and (source[pos] == ' ' or source[pos] == '\n' \
                or source[pos] == '\r' or source[pos] == '\r\n'\
                or source[pos] == '\t'):
            pos += 1

    def _error(msg):
        print ('parsed stack:\n%r'%stack)
        print ()
        print ('parsed result:\n%r'%media)
        print ()
        raise RuntimeError('%s:\n%s\033[31m--->\033[0m%s' % (msg, source[:pos], source[pos:]))

    while pos < length:
        if debug:
            print (stack, "-> ", media)
        state = stack[-1]
        if state == 'begin':
            _skip_whitespace()
            if source[pos] == '{':
                stack.append('begin_dict')
                media.append( {} )
            elif source[pos] == '[':
                stack.append('begin_list')
                media.append( [] )
            elif source[pos] == '"':
                stack.append('begin_string')
                media.append( "" )
            elif source[pos] == 'f':
                if source[pos:pos+5] == 'false':
                    pos += 4
                    media.append( False )
                    stack.pop()
                else:
                    _error('excepted false')
            elif source[pos] == 'n':
                if source[pos:pos+4] == 'null':
                    pos += 3
                    media.append( None )
                    stack.pop()
                else:
                    _error('excepted null')
            elif source[pos] == 't':
                if source[pos:pos+4] == 'true':
                    pos += 3
                    media.append(True)
                    stack.pop()
                else:
                    _error('excepted true')
            elif source[pos].isdigit():
                number_digit = []
                flag = 1
                while pos<length and (source[pos].isdigit() or (source[pos]=='.' and flag)):
                    number_digit.append(source[pos])
                    if source[pos] == '.':
                        flag = 0
                    pos += 1
                number_string = ''.join(number_digit)
                media.append(int(number_string) if flag else float(number_string))
                stack.pop()
                pos -= 1
            else:
                _error('invalid json')
            pos += 1
        elif state == 'begin_dict':
            _skip_whitespace()
            if source[pos] == '"':
                stack.append("begin")
                pos -= 1
            elif source[pos] == ':':
                key = media.pop()
                media[-1]["__key"] = key
                stack.append("begin")
            elif source[pos] == ',':
                val = media.pop()
                media[-1][ media[-1]['__key'] ] = val
                del media[-1]['__key']
            elif source[pos] == '}':
                if len(media) >= 2 and '__key' in media[-2]:
                    val = media.pop()
                    media[-1][ media[-1]['__key'] ] = val
                    del media[-1]['__key']
                stack.pop()
                stack.pop()
            else:
                _error('unexcepted char')
            pos += 1

        elif state == 'begin_list':
            _skip_whitespace()
            if source[pos] == ',':
                item = media.pop()
                media[-1].append(item)
                stack.append('begin')
            elif source[pos] == ']':
                if len(media) >= 2:
                    item = media.pop()
                    media[-1].append(item)
                stack.pop()
                stack.pop()
            else:
                stack.append("begin")
                pos -= 1
            pos += 1

        elif state == 'begin_string':
            if source[pos] == '\\':
                if source[pos+1] == 'n':
                    media[-1] += '\n'
                elif source[pos+1] == 't':
                    media[-1] += '\t'
                elif source[pos+1] == '"':
                    media[-1] += '"'
                elif source[pos+1] == 'u':
                    unicode_unit = source[pos:pos+6]
                    # if PY2: unicode_unit.decode('unicode-escape')
                    media[-1] += chr(int(unicode_unit[2:], 16))
                    pos += 4
                else:
                    media[-1] += source[pos]
                pos += 1
            elif source[pos] == '"':
                stack.pop()
                stack.pop()
            else:
                media[-1] += source[pos]
            pos += 1
        else:
            _error('unexcepted char')

    if stack != []:
        _error('unnormal json eof')

    return media[0]

def main():
    json_string = '''
    {
        "key1": "val1",
        "boolkey": false,
        "boolkey2": true,
        "listkey": [1,2,3],
        "nest_listkey": [
            {"key1": "val1"},
            {"key2": "val2"}
        ],
        "nest_obj": {
            "key1": "val1",
            "key2": [4,5,6]
            },
        "null_key": null
        }
    '''
    #json_string = '[1.3242353453, "2", 3]'
    #json_string = '[1,2,"3"]'
    p( parse(json_string) )

    return
    import time
    st = time.time()
    for i in range(10000):
        parse(json_string)
    print (time.time() - st)

    st = time.time()
    for i in range(10000):
        json.loads(json_string)
    print (time.time() - st)


def test_json_file():
    with open('/tmp/wiki.json') as fd:
        cnt = 0
        for line in fd:
            cnt += 1
            if cnt > 100:break
            p (parse(line))

if __name__ == '__main__':
    test_json_file()
    #main()

