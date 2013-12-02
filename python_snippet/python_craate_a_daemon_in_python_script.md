[How do you create a daemon in Python?](http://stackoverflow.com/questions/473620/how-do-you-create-a-daemon-in-python)


```python
#!/usr/bin/env python2
# not supported in python3
import time
from daemon import runner

class App():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/foo.pid'
        self.pidfile_timeout = 5
    def run(self):
        while True:
            print("Howdy!  Gig'em!  Whoop!")
            time.sleep(10)

app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
```
