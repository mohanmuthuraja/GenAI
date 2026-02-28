# python
Python
1. install git for windows 
2. open VS code
3. select a folder ( named : Python-training )
4. create a python file with some sample code
5. open Git hub, and create a repo (either public or private)
6. open VS code and select Gitbash
7. make sure your vs code path is in Python-training ( ex: mohan@Mohanraj MINGW64 ~/OneDrive/Documents/Python/python-training )
8. in git bash enter below to Initialize Git
	git init
9. to add files enter
	git add .
10. Commit as "Initial-version"
	git commit -m "Initial-version"
	##output#####
	
	git commit -m "Initial-version"
[master (root-commit) b3a7e6c] Initial-version
 2 files changed, 283 insertions(+)
 create mode 100644 Day1-Python.py
 create mode 100644 Day2-String.py
	## end of output

11. Connect to your GitHub repo using below 
this URL exist in GitHub

git remote add origin https://github.com/mohanmuthuraja/python.git

12. to check the remote repository your local git repo is connect to like, where will my code PUSH to and PULL from?

git remote -v
origin  https://github.com/mohanmuthuraja/python.git (fetch)
origin  https://github.com/mohanmuthuraja/python.git (push)

| Part     | Meaning                         |
| -------- | ------------------------------- |
| `origin` | Default name of remote repo     |
| `fetch`  | Where `git pull` downloads from |
| `push`   | Where `git push` uploads to     |
| URL      | Your GitHub repo link           |

13. push to GitHub
git push -u origin main

14. when error comes :
git push -u origin main
To https://github.com/mohanmuthuraja/python.git
#Error 
! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/mohanmuthuraja/python.git'
# end of error

15. pull first, then push ( it iwll merge GitHub + your local files.)
git pull origin main --allow-unrelated-histories

#error
Merge branch 'main' of https://github.com/mohanmuthuraja/python
# Please enter a commit message to explain why this merge is necessary,
# especially if it merges an updated upstream into a topic branch.
#
# Lines starting with '#' will be ignored, and an empty message aborts
# the commit.
# end of error

16. to resolve this error
Esc
:wq
Enter

That means:
Esc → exit edit mode
:wq → write (save) + quit
Enter → confirm

17. to push the code to main branch
	git push -u origin main

#Output 
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 2.81 KiB | 2.81 MiB/s, done.
Total 6 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/mohanmuthuraja/python.git
   7611913..64b2d31  main -> main
branch 'main' set up to track 'origin/main'.
#End of Output

18. Refresh GitHub and check the files
you will be able to see the files from vscode to git repo

19. if you want to add some notes in README.md then you can directly edit in git and commit the changes ( enter commit note and to edit click on pencil button to edit )

20. after editing the notes, you can go to VS Code and do the below commend
	git pull

21. go to source control page ( ctrl + shift + G ) to save pending changes.
22. enter the comment for commit changes.
and press Commit button.
23. popup appears as "would you like ot stage all your changes and commit them directly?"
press "Yes"

24. then push the commit click on OK.


