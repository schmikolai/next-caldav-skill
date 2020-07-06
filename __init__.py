from mycroft import MycroftSkill, intent_file_handler


class NextWebdav(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('webdav.next.intent')
    def handle_webdav_next(self, message):
        self.speak_dialog('webdav.next')


def create_skill():
    return NextWebdav()

