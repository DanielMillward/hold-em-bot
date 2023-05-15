End goal - a .exe/python file that can take the following parameters:
--abstraction path/to/abstraction/params.json
--continueabstraction path/to/big/file optional/path/to/last/infostate/found.txt
--runcfr path/to/big/file optional/save/params.txt
--gamer path/to/big/file

- abstraction makes an abstraction of heads up texas hold em to the specs of the file
- continueabstraction continues the work if needs to continue

Milestones:
- [ ] Make abstraction/middleman classes (allow saving on ctrl+c)
- [ ] Make runCFR class (allow saving on ctrl+c)
- [ ] Make gamer class
- [ ] convert dictionary to perfect minimal hashmap, compare space of big files
- [ ] Make visual breakdown of function runtimes
- [ ] Within python, do algo optimization/adding multithreading
- [ ] Convert to c++ or cython
- [ ] Figure out how to run on an EC2 instance
