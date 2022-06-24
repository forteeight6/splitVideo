import PySimpleGUI as sg
import sys

def simpleGui():
	if len(sys.argv) == 1:
		# Obj Text
		text = "Document to open"
		obj_text = sg.Text(text)

		# Obj In
		obj_in = sg.In()

		# Obj FileBrowse
		obj_filebrowse = sg.FileBrowse()

		# Button Open and Cancel
		obj_open, obj_cancel = sg.Open(), sg.Cancel()

		# Config Window
		fname = sg.Window(
			'My Script',
			[
				[obj_text],
				[obj_in, obj_filebrowse],
				[obj_open, obj_cancel]
			]
		).read(close=True)[1][0]
	else:
		fname = sys.argv[1]

	if not fname:
		sg.popup("Cancel", "No filename supplied")
		raise SystemExit("Cancelling: no filename supplied")
	else:
		sg.popup("The filename you chose was", fname)