class Run_Once:
    _init = False

    def __call__(self):
        if self._init:
            print('Already initialized')
            pass
        else:
            print("Initializing...")

            self._init = True


if __name__ == '__main__':
    runonce = Run_Once()
    runonce()
    runonce()
    runonce()
