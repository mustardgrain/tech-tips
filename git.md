Commits
-------

To see the last commit message and diff:

```bash
git whatchanged -p -n 1
```

To determine the number of commits your branch is ahead of master:

```bash
git log master..HEAD --pretty=oneline | wc -l
```

Rebasing
--------

To rebase against master do the following:

Make sure you've pulled to master.
git checkout foo
git rebase origin/master
