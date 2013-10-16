#!/usr/bin/env python3

import fcntl
import os
import select
from subprocess import Popen, PIPE


def non_block_read(output):
    fd = output.fileno()
    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
    try:
        return output.read()
    except:
        return ""

class SSHClient(object):
    shell = "/bin/sh"
    ssh_path = "/usr/bin/ssh"

    started = False
    stoped = False
    returncode = None

    def __init__(self, user, host, shell=None, ssh=None): 
        self.user = user
        self.host = host

        if shell is not None:
            self.shell = shell
        
        if ssh is not None:
            self.ssh_path = ssh


    def _start_ssh_process(self):
        user_host = "{user}@{host}".format(user=self.user, host=self.host)
        self.proc = Popen([self.ssh_path, user_host, self.shell],
            stdin=PIPE, stdout=PIPE, stderr=PIPE)

        import time
        start = time.time()
        while not self.proc.poll():
          if time.time() - start > 10:
            print('time out!')
            return 'error'
          time.sleep(0.1)
        poll_result = self.proc.poll()
        if poll_result is not None:
            self.returncode = poll_result
            return self.read_stderr()
        
        self.started = True
        return None


    """
    Low level methods.
    """

    def _read(self, _file):
        output = []

        while True:
            _r, _w, _e = select.select([_file],[],[], 0.2)
            if len(_r) == 0:
                break
            
            data = non_block_read(_r[0])
            if data is None:
                break

            output.append(data)
        return b"".join(output)

    def write(self, data, encoding='utf-8'):
        if isinstance(data, str):
            data = bytes(data, encoding)

        num = self.proc.stdin.write(data)
        self.proc.stdin.flush()
        return num

    def read_stdout(self):
        return self._read(self.proc.stdout)

    def read_stderr(self):
        return self._read(self.proc.stderr)


    """
    High level methods.
    """

    def start(self):
        if self.started:
            raise Exception("Already started")

        self._start_ssh_process()

    def stop(self):
        if self.stoped:
            raise Exception("Already stoped")

        self.proc.terminate()

    def execute(self, command, encoding='ascii'):
        if isinstance(command, str):
            command = bytes(command, encoding)
        if command[-1] != b"\n":
            command = command + b"\n"

        command += b"echo $?\n"
        n = self.write(command)
        result, rcode, *o = self.read_stdout().rsplit(b"\n", 2)
        return int(rcode), result


if __name__ == '__main__':
    c = SSHClient(user="yukangle", host="localhost")
    c.start()
    print(c.execute("uname -a"))
    print(c.execute("cat /proc/cpuinfo"))
    while 1:
      cmd = input('cmd:')
      print(c.execute(cmd))
