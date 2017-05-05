#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def logged(func):
    """verify if an open session exists."""
    def func_wrapper(request, *args, **kwargs):
        id_user = None
        id_server = request.session.session_key
        if id_server is not None:
            id_client = request.COOKIES['sessionid']
            id0 = request.session.get('id_user')
            if id_client == id_server and id0:
                id_user = id0
        return func(request, id_user, *args, **kwargs)
    func_wrapper.__doc__ = func.__doc__
    func_wrapper.__name__ = func.__name__
    return func_wrapper
