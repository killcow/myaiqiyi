from flask import make_response, Response
import json


def output_json(data, code, headers=None):
    my_response = {
        'code': code,
        'data': data,
        'msg': 'ok'
    }
    # """Makes a Flask response with a JSON encoded body"""
    # settings = current_app.config.get('RESTFUL_JSON', {})
    # # If we're in debug mode, and the indent is not set, we set it to a
    # # reasonable value here.  Note that this won't override any existing value
    # # that was set.  We also set the "sort_keys" value.
    # if current_app.debug:
    #     settings.setdefault('indent', 4)
    #     settings.setdefault('sort_keys', not PY3)
    #
    # # always end the json dumps with a new line
    # # see https://github.com/mitsuhiko/flask/pull/1262
    # dumped = json.dumps(my_response, **settings) + "\n"

    resp = make_response(my_response, code)
    resp.headers.extend(headers or {})
    return resp


def output_html(data, code, headers):
    resp = make_response(data, code)
    if resp.mimetype == 'text/html':
        pass
    elif resp.mimetype == 'application/json':
        my_response = {
            'code': code,
            'data': data,
            'msg': 'ok'
        }
        resp.data = json.dumps(my_response)

    resp.headers.extend(headers or {})
    return resp


def output_html2(data, code, headers):
    if isinstance(data, str) and data.index('html') != -1:
        # 在representation装饰的函数中，必须返回一个Response对象
        resp = Response(data)
        # resp = make_response(data, code)
        resp.headers.extend(headers or {})
        return resp
    else:
        my_response = {
            'code': code,
            'data': data,
            'msg': 'ok'
        }
        resp = make_response(my_response, code)
        resp.headers.extend(headers or {})
        return resp
