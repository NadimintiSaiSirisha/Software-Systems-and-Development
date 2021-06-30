# LAB ASSIGNMENT 2

## Awk Activity
* Please pass the name of the file as the command line argument for all the questions.
* Created 5 files named: `Q1.sh`, `Q2.sh`,`Q3.sh`,`Q4.sh`and`Q5.sh`containing the command for each question. 

## Git Lab Activity 
[Repository link: https://github.com/NadimintiSaiSirisha/SSD-Lab-Activity-2]
1. Installed git using sudo apt-get install git.
2. Configured git using `git config --global user.email "nsaisirisha1997@gmail.com"`

## Git Workflow
1. Created a New Repository named `SSD Lab Activity 2` using GUI
2. Cloned that Repository to my local machine using the command `git clone https://github.com/NadimintiSaiSirisha/SSD-Lab-Activity-2.git`
3. Verified that the cloning has worked by listing the files in `SSD-Lab-Activity-2`
4. Created a folder using command `mkdir Lab-Activity-2`
5. Went inside the folder using `cd Lab-Activity-2/` and created a README.md file using `touch README.md
6. Checked the status using `git status` which gave the output as :
   
    Untracked files:
    (use "git add <file>..." to include in what will be committed)
	Lab-Activity-2/
    
    Since I have not added the directory `Lab-Activity-2` in the git repository, it is showing that the directory is untracked. So, I will add the entire directory in the next step. I hope this is okay.

7. Adding the directory in the reposity using the command `git add Lab-Activity-2/
`
8. Checked the status using `git status` to get the output as:
   Changes to be committed:
   (use "git restore --staged <file>..." to unstage)
   new file:   Lab-Activity-2/README.md

9.  Committed using `git commit -m "Add README.md"` and got output as:
    [master 1388d7d] Add README.md
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 Lab-Activity-2/README.md

10. Checked status using `git status` and got output as:
    On branch master
    Your branch is ahead of 'origin/master' by 1 commit.
        (use "git push" to publish your local commits)
    nothing to commit, working tree clean

11. Checked the log using `git log` and saw the activities as:
    commit 1388d7dd15dbc536e66351e51efd8df4f69caf58 (HEAD -> master)
    Author: saisirishan <nsaisirisha1997@gmail.com>
    Date:   Tue Sep 1 18:56:27 2020 +0530
    Add README.md

## Add another file
1. Created a new file using `touch Lab-Activity-2/hello_world.txt`
2. Run `git status` to see that the file is not staged.
3. Opened the README.md file to add "This is my first git project!" to it and checked `git status`.
4. Ran the command `git add README.md` and now it showed the README.md file in green colour, meaning it is staged. The file hello_world.txt is still in red colour.
5. After running `git add .` both files are in green colour.
6. Committed all the files using `git commit -m "Add hello_world.txt and edit README.md"` to get output as:
     [master 37241c8] Add hello_world.txt and edit README.md
     2 files changed, 1 insertion(+)
     create mode 100644 Lab-Activity-2/hello_world.txt
7. `git status` shows: nothing to commit, working tree clean.
8. Ran `git log` to get all the entries of the log:
    
    commit 37241c84e4367a1ae841808f4249b7ebac9b1263 (HEAD -> master)
    Author: saisirishan <nsaisirisha1997@gmail.com>
    Date:   Tue Sep 1 19:11:04 2020 +0530
    
        Add hello_world.txt and edit
        README.md
    
    commit 1388d7dd15dbc536e66351e51efd8df4f69caf58
    Author: saisirishan <nsaisirisha1997@gmail.com>
    Date:   Tue Sep 1 18:56:27 2020 +0530
    
        Add README.md
    
    commit cc333bb4100f6fbf9e1578f97789f0dedb277bff (origin/master, origin/HEAD)
    Author: NadimintiSaiSirisha <37271933+NadimintiSaiSirisha@users.noreply.github.com>
    Date:   Tue Sep 1 18:26:50 2020 +0530
    
        Initial commit

## Pushing the work to github

1. Ran the command `git push origin master` to push all the files into the repository. It asked for username and password and I supplied those values.
2. Ran `git status` to get 
    On branch master
    Your branch is up to date with 'origin/master'.
    nothing to commit, working tree clean
3. When I reloaded the repository on GitHub, I could see the `README.md` and `hello_world.txt` files in the `Lab-Activity-2` folder that I pushed from my machine.

## Create a Pull Request and Merge a new Branch

1. Used `git checkout -b new-branch` to create a new branch, output:
    Switched to a new branch 'new-branch'
2. Created new file using  `touch test.txt`
3. Committed changes using `git push --set-upstream origin new-branch` and giving the username and password.
4. Created a pull request using `git pull`
5. Checked the branch using `git branch`
6. Used `git checkout master` to return to master branch
7.  Merged the branch with master using `git merge new-branch`
8.  Deleted the local branch using `git branch -d new-branch` to get output as:
    Deleted branch new-branch (was 37241c8).








`



