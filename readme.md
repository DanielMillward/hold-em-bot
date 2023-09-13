An attempt to use the CFR algorithm to solve heads up no limit Texas Hold'em. 

End goal - a .exe/python file that can take the following parameters:
 - abstraction path/to/abstraction/params.json (includes file path to big file) --o /path/to/last/infostate/found.txt
 - runcfr path/to/big/file --o /savestate/params.txt
 - gamer path/to/big/file

- abstraction makes an abstraction of heads up texas hold em to the specs of the file
- runcfr trains given the file
- gamer allows user input for running

Milestones:
- [ ] Make abstraction/middleman classes (allow saving on ctrl+c)
- [ ] Make runCFR class (allow saving on ctrl+c)
- [ ] Make gamer class
- [ ] Use the updated clustering algo in the paper instead of just histograms
- [ ] convert dictionary to perfect minimal hashmap, compare space of big files
- [ ] Make visual breakdown of function runtimes
- [ ] Within python, do algo optimization/adding multithreading
- [ ] Convert to c++ or cython
- [ ] Figure out how to run on an EC2 instance
