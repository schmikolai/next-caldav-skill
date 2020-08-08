import os
import platform
from mycroft import MycroftSkill, intent_file_handler
from dotenv import load_dotenv
import sys
sys.path.append(os.path.dirname(__file__))
from cal import get_calendar_events


class NextCaldav(MycroftSkill):
	def __init__(self):
		MycroftSkill.__init__(self)

	def initialize(self):
		print("Initializing Caldav skill")
		load_dotenv()
		print(os.environ["UNAME"])

	@intent_file_handler('caldav.next.intent')
	def handle_caldav_next(self, message):
		self.speak("I am checking your calendar.")
		events = get_calendar_events()
		if len(events) > 0:
			self.speak("You have {} events in the next 7 days.".format(len(events)))
			for event in events[0:3]:
				say_event_info(event)
		else:
			self.speak_dialog('caldav.no.events')

	def say_event_info(self, event):
		self.speak()

def create_skill():
	return NextCaldav()