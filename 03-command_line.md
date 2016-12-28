# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 1. ls, list files and folders
> > 2. cd, navigate the terminal
> > 3. pwd, state present working directory
> > 4. mv, move files or folders
> > 5. rm, remove unnecessary files or folders
> > 6. mkdir, create a directory
> > 7. grep, find strings
> > 8. find, find files
> > 9. man, terminal information
> > 10. history, history of command lines

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > ls, presents the files and folders in the current directory
> > ls -a, presents all of the files and folders including hidden ones
> > ls -l, presents files and folders and descriptions of the files like permissions, number of hard links, owner, group, size, date and time last modified, and name
> > ls -lh, same as -l, but changes size to k or M
> > ls -lah, includes functionalities of -l, -a, and -h
> > ls -t, lists files based on the time they were modified
> > ls -Glp, list in color, long format (descriptions), and / after directories

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > C, columnar format
> > g, long format listing without owner name
> > a, displaying all files
> > c, displaying by timestamp
> > u, displaying by access time

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs is usually used in conjunction with other commands like find, grep, remove or other commands. The advantage of using xargs with the other commands is that it can limit command execution to arguments used like -n, provide prompts with -d, and treat white space differently with -0

 

