from subprocess import PIPE, Popen

#proc = Popen(['curl', 'http://www.baidu.com'], stdin = PIPE, stderr = PIPE, stdout = PIPE)
proc = Popen(['changing_output.sh'], stdin = PIPE, stderr = PIPE, stdout = PIPE)
while proc.poll() == None:
    import fcntl
    import os
    import select
    fcntl.fcntl(
            proc.stdout.fileno(),
            fcntl.F_SETFL,
            fcntl.fcntl(proc.stdout.fileno(), fcntl.F_GETFL) | os.O_NONBLOCK,
            )

    fcntl.fcntl(
            proc.stderr.fileno(),
            fcntl.F_SETFL,
            fcntl.fcntl(proc.stderr.fileno(), fcntl.F_GETFL) | os.O_NONBLOCK,
            )

    while proc.poll() == None:
        readx = select.select([proc.stdout.fileno()], [], [], 0.1)[0]
        readx_err = select.select([proc.stderr.fileno()], [], [], 0.1)[0]
        if readx:
            chunk = proc.stdout.read()
            print chunk,
        elif readx_err:
            chunk = proc.stderr.read()
            print chunk,
        else:
            break
    #proc.stdin.write('input')
    #proc.stdin.flush()
proc.wait()
