# An exception is an error that occurs during program execution.
# Python generates an exception that will be handled using try..except
"""
try:
    statement (s)
except:
    statement (s)
"""

a = 35
b = 57

try:
    c = a + b
    print("The value of c is: ", c)
    d = b/0
    print("The value of d is: ", d)
except:
    print("Division by zero is not possible")

print("Out of try...except block")


# The pdb debugger tools
# The pdb module is used to debug Python programs
# The pdb set breakpoints and inspects the stack frames, and lists the source code.
# There are three ways to use this debugger:

"""
# 1-Within an interpreter
To start the debugger from the Python interactive console,
using run() or runeval().
Start your python3 interactive console. 
Run the following command to start the console:

$ python3
>>> import pdb_example
>>> import pdb
>>> pdb.run('pdb_example.Student(5).print_std()')
> <string>(1)<module>()
(Pdb)

To continue debugging, enter continue after the (Pdb) prompt and press Enter. 
If you want to know the options we can use in this, 
then after the (Pdb) prompt press the Tab key twice
"""

"""
# 2. From a command line

$ python3 -m pdb pdb_example.py

When you run the debugger from the command line, source code will be loaded and it will
stop the execution on the first line it finds. Enter continue to continue the debugging
"""


"""
# 3 With a Python script
To start the debugger within a script, use 

pdb.set_trace().
"""

#Debugging basic program crashes
"""
The trace module helps in tracing the program execution. 
So, whenever your Python program crashes, we can understand where it crashes. 
We can use trace module by importing it into your script as well as from the
command line.

Example:
# file trace_example.py

    class Student:
        def __init__(self, std):
            self.count = std

        def go(self):
            for i in range(self.count):
                    print(i)
            return

if __name__ == '__main__':
Student(5).go()

 $ python3 -m trace --trace trace_example.py

By using trace --trace at the command line, the developer can trace the program
line-by-line. So, whenever the program crashes, the developer will know the instance
where it crashes.
"""


"""
Profiling a Python program means measuring an execution time of a program. It measures
the time spent in each function. Python's cProfile module is used for profiling a Python
program.


$ python3 -m cProfile cprof_example.py

using cProfile, all functions that are called will get printed with the time spent on
each function. Now, we will see what these column headings mean:
- ncalls: Number of calls
- tottime: Total time spent in the given function
- percall: Quotient of tottime divided by ncalls
- cumtime: Cumulative time spent in this and all subfunctions
- percall: Quotient of cumtime divided by primitive calls
- filename:lineno(function): Provides the respective data of each function

"""


"""
# timeit
Using timeit, we can decide what piece of code we want to measure the performance of.
So, we can easily define the setup code as well as the code snippet on which we want to
perform the test separately. 
The main code runs 1 million times, which is the default time,whereas the setup code runs only once.
"""

# Making program run faster
# There are various ways to make your Python programs run faster, such as the following:
# 1- Profile your code so you can identify the bottlenecks
# 2- Use built-in functions and libraries so the interpreter doesn't need to execute loops
# 3- Avoid using globals as Python is very slow in accessing global variables
# 4- Use existing packages
