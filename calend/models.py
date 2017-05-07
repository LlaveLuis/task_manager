#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from calendar import HTMLCalendar
from datetime import date


class TaskCalendar(HTMLCalendar):
    """Class Calendar based to use with Tasks."""

    def __init__(self):
        HTMLCalendar.__init__(self)
        self.year = self.month = None

    def formatday(self, day, week):
        try:
            date_eval = date(self.year, self.month, day)
        except ValueError:
            day = 0   # force to mark as no valid day
        if day == 0:
            return self.calend_day('no-day', '&nbsp')   # no valid day
        elif date_eval == date.today():
            return self.calend_day('today', '<a href="" class="no-link" '
                                          'data-toggle="tooltip" '
                                          'title="Today" onclick="return false;"'
                                          '>' + str(day) + '</a>')
        else:
            return self.calend_day('day', day)   # normal day

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(TaskCalendar, self).formatmonth(year, month, True)

    def calend_day(self, css_name, text):
        """Generate HTML code for a calendar day, to show.
        :param css_name: name of class css to assign
        :param text: text or HTML code HTML to put inside a <td> element
        :return: HTML code for a <td> element related to a calendar day
        """
        return '<td class="%s">%s</td>' % (css_name, text)
