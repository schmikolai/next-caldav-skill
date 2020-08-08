import os
import datetime as DT
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
		self.speak("Let me check your calendar.")
		try:
			events = get_calendar_events()
		except:
			self.speak("I am sorry, I couldn't load your calendar. Please check your configuration.")
			return
		if len(events) > 0:
			self.speak("You have {} events in the next 7 days.".format(len(events)))
			for event in events[0:3]:
				self.say_event_info(event)
		else:
			self.speak_dialog('caldav.no.events')

	def say_event_info(self, event):
		if event["date"] == DT.date.today():
			daystring = "Today"
		elif event["date"] == DT.date.today() + DT.timedelta(1):
			daystring = "Tomorrow"
		else:
			daystring = event["date"].strftime("On %A")
		
		if "time" in event:
			timestring = "at {} {} {}".format(event["time"].hour, event["time"].minute or "", event["time"].strftime("%p"))
		else:
			timestring = ""

		self.speak("{} {} is {}".format(daystring, timestring, event["title"]))

def create_skill():
	return NextCaldav()