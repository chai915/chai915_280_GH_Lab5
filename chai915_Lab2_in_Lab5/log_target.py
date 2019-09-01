class LogTarget(object):

    def set_message(self, msg):
        self._msg = msg
        
    def get_message(self):
        return self._msg
    