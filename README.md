# Python Sensu Plugin

This is a framework for writing your own Sensu plugins in Python.
It's not required to write a plugin (most Nagios plugins will work
without modification); it just makes it easier.

## Checks

To implement your own check, subclass SensuPluginCheck, like
this:

    from sensu_plugin import SensuPluginCheck

    class MyCheck(SensuPluginCheck):
      def setup(self):
        # Setup is called with self.parser set and is responsible for setting up
        # self.options before the run method is called

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
        # this method is called to perform the actual check

        self.check_name('my_awesome_check') # defaults to class name

        if self.options.warning == 0:
          self.ok(self.options.message)
        elif self.options.warning == 1:
          self.warning(self.options.message)
        elif self.options.warning == 2:
          self.critical(self.options.message)
        else:
          self.unknown(self.options.message)

    if __name__ == "__main__":
      f = MyCheck()

## License

* Based heavily on [sensu-plugin](https://github.com/sensu/sensu-plugin) Copyright 2011 Decklin Foster
* Python port Copyright 2014 S. Zachariah Sprackett

Released under the same terms as Sensu (the MIT license); see LICENSE
for details

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/zsprackett/python_sensu_plugin/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
