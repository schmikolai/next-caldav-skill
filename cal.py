import datetime as DT
import caldav
import os
import json


def parse_caldav_data(caldav_data):
	lines = caldav_data.split("\r\n")
	obj = {}
	print('=================')
	context = obj
	for line in lines:
		print(line)
		if line.startswith('BEGIN:'):
			context[line[6:]] = {"parent": context}
			context = context[line[6:]]
		elif line.startswith('END:'):
			context = context['parent']
		else:
			context[line[:line.index(':')]] = line[line.index(':')+1:]

	result = {}

	event = obj["VCALENDAR"]["VEVENT"]

	if event["SUMMARY"]:
		result["title"] = event["SUMMARY"]

	for key in event:
		if key.startswith("DTSTART"):
			timestamp = event[key]
			result["date"] = DT.date(int(timestamp[:4]), int(timestamp[4:6]), int(timestamp[6:8]))
			if len(timestamp) > 8:
				result["time"] = DT.time(int(timestamp[9:11]), int(timestamp[11:13]), int(timestamp[13:15]))

	return result


def get_calendar_events():
	url = "https://next.social-robot.info/nc/remote.php/dav"
	username = os.environ["UNAME"]
	password = os.environ["PWORD"]

	client = caldav.DAVClient(url=url, username=username, password=password)

	all_events = []

	my_principal = client.principal()
	calendars = my_principal.calendars()
	if calendars:
		# Some calendar servers will include all calendars you have
		# access to in this list, and not only the calendars owned by
		# this principal.  TODO: see if it's possible to find a list of
		# calendars one has access to.
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
