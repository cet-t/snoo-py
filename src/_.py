from pynput import keyboard


class MonKeyBoard:
    def on_press(self, key):
        return key

    def on_release(self, key):
        return key

    def start(self):
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )
        self.listener.start()

    def getstatus(self):
        if (self.listener == None):
            return False
        return True


if __name__ == '__main__':
    key_input = MonKeyBoard()
    key_input.start()

    while (True):
        status = key_input.getstatus()
        # print(str(status))
        if (status == False):
            print("break")
            break
