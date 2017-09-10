from pyps import Connection, EventListener, ConnectionError
import json
import multiprocessing
import os

class PSif(Connection):
	"""High level interface for Photoshop"""
	def __init__(self):
		super(PSif, self).__init__()
		self.includeHeader = ""

	def addJvsLib(self,filepath):
		if os.path.isfile(filepath):
			self.includeHeader += "#include '{}'\n".format(filepath)
		else:
			raise FileNotFoundError("Javascript Library file not found: {}".format(filepath))

	def execJvsFunc(self,function,args,timeout=0):
		JavascriptCode = self.includeHeader
		JavascriptCode += function + "("+ json.dumps(args) + ");\n"
		response = self.send_sync(JavascriptCode)

		return True,response



		