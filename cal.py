import datetime as DT
import caldav
import os
import json

# Parse answer from caldav library to usable format
def parse_caldav_data(caldav_data):
	lines = caldav_data.split("\r\n")
	# obj will hold a hierarchical caldav data
	obj = {}
	print('=================')
	context = obj
	for line in lines:
		# Add a layer to the hierachy
		if line.startswith('BEGIN:'):
			context[line[6:]] = {"parent": context}
			context = context[line[6:]]
		# Go one layer up in the hierachy
		elif line.startswith('END:'):
			context = context['parent']
		# Add data to the current node
		else:
			context[line[:line.index(':')]] = line[line.index(':')+1:]

	print(obj)

	result = {}

	# find the actual relevant part of the event data
	event = obj["VCALENDAR"]["VEVENT"]

	# store the title of the event
	if event["SUMMARY"]:
		result["title"] = event["SUMMARY"]

	# find the beginning of the event
	for key in event:
		# key always starts with DTSTART, but differs for events with specific time, or whole day
		if key.startswith("DTSTART"):
			timestamp = event[key]
			result["date"] = DT.date(int(timestamp[:4]), int(timestamp[4:6]), int(timestamp[6:8]))
			if len(timestamp) > 8:
				result["time"] = DT.time(int(timestamp[9:11]), int(timestamp[11:13]), int(timestamp[13:15]))

	return result

# used to retreive parsed caldav event data
def get_calendar_events():
	url = os.environ["CALDAV_ADRESS"]
	username = os.environ["UNAME"]
	password = os.environ["PWORD"]

	# initialize the caldav client
	client = caldav.DAVClient(url=url, username=username, password=password)

	all_events = []

	my_principal = client.principal()
	calendars = my_principal.calendars()
	if calendars:
		print("your principal has %i calendars:" % len(calendars))
		for c in calendars:
			print("    Name: %-20s  URL: %s" % (c.name, c.url))
			events = c.date_search(start=DT.datetime.now(
			), end=DT.datetime.now() + DT.timedelta(days=7), expand=True)
			all_events.extend(events)
	else:
		print("your principal has no calendars")

	for i in range(len(all_events)):
		all_events[i].load()
		all_events[i] = parse_caldav_data(all_events[i].data)

	return sorted(all_events, key=lambda k: (k['date'], k['time'] if 'time' in k else DT.time()))


if __name__ == "__main__":
	print(get_calendar_events())
