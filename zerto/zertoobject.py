# -*- coding: utf-8 -*-
'''Basic zerto object'''


class ZertoObject(object):

    def __str__(self):
        return str(getattr(self, 'values', None))

    def __repr__(self):
        return '<{0} {1}>'.format(
            self.__class__.__name__, getattr(self, 'values', None))


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
