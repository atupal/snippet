```
Git over an ssh tunnel (like through a firewall or VPN)
Submitted by rfay on Mon, 2010-10-11 18:41
gitssh
It's a treasured geek secret that ssh can tunnel TCP connections like ssh all over the internet. What does that mean? It means that you can access machines and ports from your local machine that you never thought you could, including git repositories that are behind firewalls or inside VPNs.

There are two steps to this. First, we have to set up an ssh tunnel. We have 3 machines we're interacting with here:

The local machine where we want to be able to do a git clone or git pull or whatever. I'll call it localhost.
The internet or VPN host that has access to your git repository. Let's call it proxy.example.com.
The host that has the git repository on it. We'll call it git.example.com, and we'll assume that access to git is via ssh on port 22, which is very common for git repos with commit access.
Step 1: Set up a tunnel (in one window). ssh -L3333:git.example.com:22 you@proxy.example.com

This ssh's you into proxy.example.com, but in the process sets up a TCP tunnel between your localhost port 3333 through the proxy internet host and to port 22 on git.example.com. (You can use any convenient port; 3333 is just an example.)

Note that we have to have permission to do this on the proxy.example.com server; the default is for it to be on, but it might not be. The relevant permission is PermitTunnel and it must be allowed (or omitted) in /etc/ssh/sshd_config (debian). But now we'll test to see whether it's working or not:

telnet localhost 3333

If you get an answer like SSH-2.0-OpenSSH_5.1p1 Debian-5 you are in business.
If "telnet" is not found, then install it with apt-get install telnet or yum install telnet or whatever for your distro.

Step 2: Use git with an ssh URL to connect through the tunnel to your behind-the-VPN git repo:
git clone ssh://git@localhost:3333/example.git

"git@" is the user you use to connect to the git repo; it might be something else, of course. And your project might be in a subdirectory, etc. So it might be git clone ssh://rfay@localhost:3333/project/someproject.git.

You should have a repo cloned.

Remember that you have to have the tunnel up in the future to do a pull or fetch or similar operation. You may want to look into the excellent autossh package that automatically establishes ssh connections and keeps them up.

There are lots of resources on ssh tunneling including this simple one. You can also use ssh -R to put a port on the machine you ssh into that will access your own local machine.
```
