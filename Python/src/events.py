class EventArgs:
	def __init__(self, event, invoker, data):
		self.event = event
		self.invoker = invoker
		self.data = data

class EventListener:
	def __init__(self, callback):
		self.callback = callback
	def trigger(self, event_args):
		self.callback(event_args)

class Event:
	def __init__(self, event_name):
		self.event_name = event_name
		self.listeners = []
	def add_listener(self, listener):
		if not (listener in self.listeners):
			self.listeners.append(listener)
	def remove_listener(self, listener):
		if (listener in self.listeners):
			self.listeners.remove(listener)
	def trigger(self, invoker, data):
		#if (self.event_name != "event_fire"):
		#	print("EVENT: " + self.event_name)
		# if (self.event_name == "event_request_score"):
		# 	print("Dispatching event with data type: " + repr(data) + str(data.score))
		args = EventArgs(self, invoker, data)
		for listener in self.listeners:
			#print("    (notified " +repr(listener))
			listener.trigger(args)
			# if (self.event_name == "event_request_score"):
			# 	print("Dispatch complete with score: " + repr(data) + " " + str(data.score))

