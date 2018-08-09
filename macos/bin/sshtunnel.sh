#!/bin/sh

# Ref: https://superuser.com/questions/37738/how-to-reliably-keep-an-ssh-tunnel-open
#      https://stackoverflow.com/questions/25084288/keep-ssh-session-alive

while true
do
  echo "[$(date)] ssh tunneling"
  # If we don't disable the proxy, since after new update, the ssh get following error: ssh: connect to host server port 22: Connection refused
  # Ref: https://gist.github.com/xiaohui/87d4b54748ae9004d5fd

  networksetup -setsocksfirewallproxystate "WI-FI" off
  #ssh user@server -D 127.0.0.1:8086 -Nf
  ssh user@server -D 127.0.0.1:8086 -o ServerAliveInterval=30 -Nf
  networksetup -setsocksfirewallproxystate "WI-FI" on
  networksetup -getsocksfirewallproxy "WI-FI"

  while true
  do
    ps -ef | grep "ssh " | grep -v grep > /dev/null
    if [ $? -ne 0 ]; then
      echo "Restarting ssh tunnel..."
      break
    fi
    sleep 10
  done
  sleep 1
done
