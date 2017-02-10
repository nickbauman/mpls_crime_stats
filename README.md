# Minneapolis Crime Trends

This is an attempt to show some trends in Minneapolis-wide trends in crime by looking at the data.

## Installation

I prefer to use virtualenv and install packages that way.

```
virtualenv -p /usr/bin/python3 env;
source env/bin/activate;
pip install -r ./requirements.txt
```

pandas uses numpy which is HUGE so this will take some time.

## How it works

### Cleaning the Data

Much of the data here is pretty clean already. Except for 2012, which appears to have the data only in the turd-format 
(for data-mining at least) that is PDF. Hopefully that will be changed soon.

### Loading the data

Ultimately the most interesting data structure I can come up with looks like the following dict:

```
year->month->neighborhood->crime->occurrences
```

Let's just call this the _Crime Stat Time Series_ (or *CSTS*) data format. 

To import all the data into RAM, from the root of the repo checked out, start an iPython session and do the following:

```
(env)$  mpls_crime_trends git:(master) ✗ ipython                      
WARNING: Attempting to work in a virtualenv. If you encounter problems, please install IPython inside the virtualenv.
Python 2.7.10 (default, Jul 14 2015, 19:46:27) 
Type "copyright", "credits" or "license" for more information.

IPython 1.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: from import_all import loadm

In [2]: g = loadm()
```

The variable `g` should contain the full CSTS formatted data in this example iPython session

### First Glance

At first glance you can see crime is dropping city-wide. In some cases *a lot.* But that's all I can say for now.

### Goals

Be able to discern where our crime is headed for the city. NOTE: this is reported crime to the local police. Many crimes 
do not get reported for a variety of reasons, some of them very surprising.

### License

The code you see here is Copyright Nick Bauman and is EPL licensed. The data is public and available on the Minneapolis
city website. http://minneapolismn.gov/police/statistics/crime-statistics_codefor_statistics

