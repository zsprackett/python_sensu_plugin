#!/usr/bin/env python
#coding=utf-8

#
# Copyright (C) 2014 - S. Zachariah Sprackett <zac@sprackett.com>
#
# Released under the same terms as Sensu (the MIT license); see LICENSE
# for details.

from plugin import SensuPlugin

class SensuPluginCheck(SensuPlugin):
  def check_name(self, name=None):
    if name:
      self._check_name = name

    if hasattr(self,'_check_name'):
      return self._check_name

    return self.__class__.__name__

  def message(self, *m):
    self._message = m

  def output(self, m):
    msg = ''
    if m == None or (m[0] == None and len(m) == 1):
      m = self._message

    if not m == None and not (m[0] == None and len(m) == 1):
      msg = ": {}".format(' '.join(str(message) for message in m))

    print "{} {}{}".format(self.check_name(), self.status, msg)
