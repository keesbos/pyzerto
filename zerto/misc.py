# -*- coding: utf-8 -*-
'''
Module for miscellaneous functions
'''

import datetime
import re

re_date = re.compile('/Date[(](\d+)([+-]\d+)?[)]/')
# Date: /Date(1444792425000+0200)/
# Date: /Date(1444792425365)/


def parse_timestamp(timestamp):
    '''Parse zerto timestamp and return datetime object'''
    m = re_date.match(timestamp)
    if m:
        t = int(m.group(1))/1000.0
        return datetime.datetime.fromtimestamp(t)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
