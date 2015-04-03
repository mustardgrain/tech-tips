Cheat Sheets
============

https://gist.github.com/JoshuaEstes/2627607#file-git-cheat-sheat-md

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

To rebase against master, first update master, then `git checkout` to your branch, then do the following:

```bash
git rebase origin/master
```

Branching
---------

To prune remote branches run:

```bash
git remote prune origin
```
