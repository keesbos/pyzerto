# -*- coding: utf-8 -*-
'''
Module with zerto error types
'''


class ZertoError(Exception):
    pass


class ZertoUnsupportedApi(ZertoError):
    pass


class ZertoServiceError(ZertoError):

    def __init__(self, status_code, errcode, errmsg, *args):
        super(ZertoServiceError, self).__init__(
            status_code, errcode, errmsg, *args)
        self.status_code = status_code
        self.errcode = errcode
        self.errmsg = errmsg
        if errmsg:
            if errcode:
                self.message = "{0}: {1}".format(
                    errcode, errmsg)
            else:
                self.message = str(errmsg)
        elif errcode:
            self.message = str(errcode)
        elif status_code:
            self.message = str(status_code)

    def __str__(self):
        if self.message:
            return self.message
        return repr(self)


class ZertoAuthError(ZertoServiceError):

    def __init__(self, errmsg, *args):
        super(ZertoAuthError, self).__init__(
            500, 'AuthError', errmsg, *args)


# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

class Zerto4xx(ZertoServiceError):
    pass


class ZertoBadRequest(Zerto4xx):
    # 400
    pass


class ZertoUnauthorized(Zerto4xx):
    # 401
    pass


class ZertoForbidden(Zerto4xx):
    # 403
    pass


class ZertoNotFound(Zerto4xx):
    # 404
    pass


class ZertoMethodNotAllowed(Zerto4xx):
    # 405
    pass


class ZertoFailure(ZertoServiceError):
    pass


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
