# MAXIMUM LOAD
:floppy_disk: Created with Python 3.7.0, 64-bit, with Visual Studio Code, MacOS Mojave 10.14.3

The program calculates a maximum load that can be placed on top of a given wall.

Author: _Pawel Flajszer, April 2019, pflajszer@gmail.com_ :envelope:

## Requirements:

- Python3

In order to run the application please install the following modules:
- **re**, version==**2.2.1**
- **sys**, version==**3.7.0**

## Usage:

The application takes two command line arguments:
- the path to the text file formatted as a "wall" in ```*.txt``` file with extension included
  (if the file is not located in the same folder as the program make sure to use an absolute path).
- the initial position to start measuring maximum load for the given wall (index ```0``` starts at ```1``` as per specification)

Example usage:  

	Pawels-MacBook-Pro:~ username$ python application.py wall0.txt 10

	Pawels-MacBook-Pro:~ username$ python application.py /Users/Username/Desktop/brick_problem/textfile.txt 20

## Performance:

:chart_with_upwards_trend: Notation: ```O(n)```

The algorithm starts at a row of index ```1``` and multiplies 2 values directly above (if they exist), then chooses the smaller value, assigns it to the current brick and continues. At the end of the row all rows above can be completely ignored, since all the weakest pathways from the top to the current row are stored in the current row. After finishing with a row it moves on to the next one.  When reaches the bottom of the 'wall', it sorts the whole row, and prints the smallest value. That value is the maximum load you can place on the wall. That way the performance is highly superior over the previous version of the Maximum Load app (```O(2^n)```).

For a "wall" input of 10 rows the cProfile returns:

         688 function calls (680 primitive calls) in 0.003 seconds

    Ordered by: internal time

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       22    0.001    0.000    0.001    0.000 {method 'split' of 're.Pattern' objects}
        1    0.001    0.001    0.001    0.001 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.003    0.003 application.py:52(create_wall)
        2    0.000    0.000    0.000    0.000 sre_parse.py:475(_parse)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.003    0.003 application.py:111(main)
       23    0.000    0.000    0.000    0.000 re.py:271(_compile)



For a "wall" input of 20 rows the cProfile returns:

         1348 function calls (1340 primitive calls) in 0.007 seconds

    Ordered by: internal time

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       42    0.005    0.000    0.005    0.000 {method 'split' of 're.Pattern' objects}
        1    0.001    0.001    0.001    0.001 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.007    0.007 application.py:52(create_wall)
      171    0.000    0.000    0.000    0.000 application.py:83(choose_weaker_path)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
        1    0.000    0.000    0.000    0.000 application.py:70(create_pyramid)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        2    0.000    0.000    0.000    0.000 sre_parse.py:475(_parse)
       18    0.000    0.000    0.000    0.000 application.py:99(row_calculations)
       43    0.000    0.000    0.000    0.000 re.py:271(_compile)
       

For a "wall" input of 100 rows the cProfile returns:
       
          21028 function calls (21020 primitive calls) in 0.161 seconds

    Ordered by: internal time

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      202    0.138    0.001    0.138    0.001 {method 'split' of 're.Pattern' objects}
        1    0.008    0.008    0.151    0.151 application.py:52(create_wall)
     4851    0.004    0.000    0.006    0.000 application.py:83(choose_weaker_path)
        1    0.003    0.003    0.003    0.003 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.002    0.002    0.002    0.002 application.py:70(create_pyramid)
        1    0.001    0.001    0.001    0.001 {method 'split' of 'str' objects}
       98    0.001    0.000    0.007    0.000 application.py:99(row_calculations)
        1    0.001    0.001    0.001    0.001 application.py:63(divide_bricks)
     9781    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.001    0.001    0.001    0.001 {built-in method _codecs.utf_8_decode}
     4852    0.001    0.000    0.001    0.000 {method 'sort' of 'list' objects}
      203    0.000    0.000    0.001    0.000 re.py:271(_compile)


## #TODO

Possible improvements:
- Increase readability
- OO approach


Bugs:
- None :+1:


 
