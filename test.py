#!/usr/bin/env python
#coding=utf-8

#
# Copyright (C) 2014 - S. Zachariah Sprackett <zac@sprackett.com>
#

from sensu_plugin import SensuPluginCheck


class FooBarBazCheck(SensuPluginCheck):
    def setup(self):
        self.parser.add_argument(
            '-w',
            '--warning',
            required=True,
            type=int,
            help='Integer warning level to output'
        )
        self.parser.add_argument(
            '-m',
            '--message',
            default=None,
            help='Message to print'
        )


    def run(self):
        self.message("this is a throwdown")

        if self.options.warning == 0:
            self.ok(self.options.message)
        elif self.options.warning == 1:
            self.warning(self.options.message)
        elif self.options.warning == 2:
            self.critical(self.options.message)
        else:
            self.unknown(self.options.message)

if __name__ == "__main__":
    f = FooBarBazCheck()
