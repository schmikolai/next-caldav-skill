# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/calendar-day.svg" card_color="#0082C9" width="50" height="50" style="vertical-align:bottom"/> Nextcloud Caldav
Retreives appointments from nextcloud calendar

## About
Retreives all appointment in the upcoming days from a linked nextcloud calendar

## Installation

### Getting the skill
You can install this skill with msm by running the following command:
```
msm install https://github.com/schmikolai/next-caldav-skill.git
```

### Skill setup
Navigate to the directory, where the skill was installed. If not otherwise specified, it should be `/path/to/mycroft-core/skills/next-caldav-skill.schmikolai`

Run the configuration script:
```
python3 config.py
```
Enter the the adress to your Nextcloud server, other systems with the CalDAV protocol may work, too.  
Enter you login information of that Nextcloud server.  

_Note: Your credentials will be stored in cleartext on your local machine. You can remove them, by deleting the created `.env` file._

### If skill can't be initialized when starting mycroft
Try:
- Check that your credentials are correct in the `.env` file.
- Manually install the dependencies for the skill:
```
cd /path/to/mycroft-core
source venv-activate.sh
pip install -r skills/next-caldav-skill.schmikolai/requirements.txt
```
- restart mycroft services

## Examples
* "What are my appointments"
* "Appointments this week"
* "What appointments do i have"
* "Do i have appointments"
* "Do i have an appointment"
* "Do i have a meeting"
* "Are there any appointments"
* "What is on my calendar"

## Credits
Nikolai Schmidt

## Category
**Productivity**

## Tags
#Calendar

