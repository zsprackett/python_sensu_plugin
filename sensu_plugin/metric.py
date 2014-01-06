#!/usr/bin/env python
#coding=utf-8

#
# Copyright (C) 2014 - S. Zachariah Sprackett <zac@sprackett.com>
#
# Released under the same terms as Sensu (the MIT license); see LICENSE
# for details.

import json, time
from plugin import SensuPlugin

class SensuPluginMetricJSON(SensuPlugin):
  def output(self, m):
    obj = m[0]
    if type(obj) is str or type(obj) is Exception:
      print obj
    elif type(obj) is dict or type(obj) is list:
      print json.dumps(obj)

class SensuPluginMetricGraphite(SensuPlugin):
  def output(self, *m):
    if m[0] == None:
      print
    elif type(m[0]) is Exception or m[1] == None:
      print m[0]
    else:
      l = list(m)
      if len(l) < 3:
        l.append(None)
      if l[2] == None:
        l[2] = int(time.time())
      print "\t".join(str(s) for s in l[0:3])

class SensuPluginMetricStatsd(SensuPlugin):
  def output(self, *m):
    if m[0] == None:
      print
    elif type(m[0]) is Exception or m[1] == None:
      print m[0]
    else:
      l = list(m)
      if len(l) < 3 or l[2] == None:
        stype = 'kv'
      else:
        stype = l[2]
      print "|".join([":".join(str(s) for s in l[0:2]), stype])
