#!/usr/bin/env python
#coding=utf-8

#
# Copyright (C) 2014 - S. Zachariah Sprackett <zac@sprackett.com>
#
# Released under the same terms as Sensu (the MIT license); see LICENSE
# for details.

import atexit, sys, argparse
from exitcode import ExitCode
from exithook import ExitHook

class SensuPlugin(object):
  def __init__(self):
    self._message = None
    self.hook = ExitHook()
    self.hook.hook()
    for method in dir(ExitCode):
      if not (method.startswith('__') and method.endswith('__')):
        self.__make_dynamic(method)

    atexit.register(self.__exitfunction)

    self.parser = argparse.ArgumentParser()
    if (hasattr(self, 'setup')):
      self.setup()
    self.options = self.parser.parse_args()

    self.run()

  def output(self, args):
    print "SensuPlugin: %s" % ' '.join(str(a) for a in args)

  def __make_dynamic(self, method):
    ec = ExitCode()
    def dynamic(*args):
      self.status = method
      if (len(args) == 0):
        args = None
      self.output(args)
      sys.exit(getattr(ec, method))

    method_lc = method.lower()
    dynamic.__doc__ = "%s method" % method_lc
    dynamic.__name__ = method_lc
    setattr(self, dynamic.__name__, dynamic)

  def run(self):
    self.warning("Not implemented! You should override SensuPlugin.run()")

  def __exitfunction(self):
    if self.hook.exit_code == None and self.hook.exception == None:
      print "Check did not exit! You should call an exit code method."
    elif self.hook.exception:
      print "Check failed to run: %s" % self.hook.exception
