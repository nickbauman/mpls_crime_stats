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

TODO. Ultimately the most interesting data structure I can come up with looks like the following dict:

```
year->month->neighborhood->crime->occurrences
```

Let's just call this the _Crime Stat Time Series_ (or *CSTS*) data format. Once we have all the data loaded into this
format, things can get a lot more interesting.

### First Glance

At first glance you can see crime is dropping city-wide. In some cases *a lot.* But that's all I can say for now.

### Goals

Be able to discern where our crime is headed for the city. NOTE: this is reported crime to the local police. Many crimes 
do not get reported for a variety of reasons, some of them very surprising.

### License

The code you see here is Copyright Nick Bauman and is EPL licensed. The data is public and available on the Minneapolis
city website. http://minneapolismn.gov/police/statistics/crime-statistics_codefor_statistics

