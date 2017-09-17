class tv_1:

    commands = {
        'power': 'KEY_1',
        'hdmi': 'KEY_2'
    }

    def run(self, cmd):
        if cmd not in self.commands:
            return False

        print("irsend SEND_ONCE tv_1 %s" % self.commands[cmd])
        os.system("irsend SEND_ONCE tv_1 %s" % self.commands[cmd])
            
        return True
