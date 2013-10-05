I needed this as well, and with the help of Bombe's answer + some fiddling around, I got it working. Here's the recipe:

Import git -> svn

```
1. cd /path/to/git/localrepo
2. svn mkdir --parents protocol:///path/to/repo/PROJECT/trunk -m "Importing git repo"
3. git svn init protocol:///path/to/repo/PROJECT -s
4. git svn fetch
5. git rebase trunk
5.1.  git status
5.2.  git add (conflicted-files)
5.3.  git rebase --continue
5.4.  (repeat 5.1.)
6. git svn dcommit
```
After #3 you'll get a cryptic message like this:

Using higher level of URL: `protocol:///path/to/repo/PROJECT => protocol:///path/to/repo`

Just ignore that.

When you run #5, you might get conflicts. Resolve these by adding files with state "unmerged" and resuming rebase. Eventually, you'll be done; Then sync back to the svn-repo, using dcommit. That's all.

Keeping repos in sync

You can now sync from svn -> git, using the following commands:

```
git svn fetch
git rebase trunk
```
And to sync from git -> svn, use:

```
git svn dcommit
Final note
```

You might want to try this out on a local copy, before applying to a live repo. You can make a copy of your git-repo to a temporary place, simply using cp -r, as all data is in the repo itself. You can then set up a file-based testing repo, using:

svnadmin create /home/name/tmp/test-repo
And check a working copy out, using:

```
svn co file:///home/name/tmp/test-repo svn-working-copy
```
That'll allow you to play around with things before making any lasting changes.

Addendum: If you mess up git svn init

If you accidentally run git svn init with the wrong url, and you weren't smart enough to take a backup of your work (don't ask ...), you can't just run the same command again. You can however undo the changes by issuing:

rm -rf .git/svn
edit .git/config
And remove the section [svn-remote "svn"] section.

You can then run git svn init anew.
