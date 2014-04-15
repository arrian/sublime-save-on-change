import sublime, sublime_plugin
import os, time

SETTINGS_FILE = 'SaveOnChange.sublime-settings'
DEFAULT_FILE = '../../vis.cache'

class SaveOnChangeCommand(sublime_plugin.EventListener):

	def on_selection_modified(self, view):
		self.save(view)#TODO: optimise to only write first line of file

	def on_modified(self, view):
		self.save(view)

	def save(self, view):
		#f = open(DEFAULT_FILE, "w")
		#f.write(str(view.sel()[0].begin()) + "," + str(view.sel()[0].end()) + "," + str(time.time()) + "\n" + view.substr(sublime.Region(0, view.size())))
		#f.close()

class SaveOnChangeStartCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		pass

class SaveOnChangeStopCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		pass



