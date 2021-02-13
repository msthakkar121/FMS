# File Monitoring

The system consists of two parts:

    1. Generator
    2. Search

`Generator:` It writes pseudo random strings of various lengths to two different files (picks file randomly) every 
few seconds. It has 50% probability of generating a specific keyword (‘CDS’ in current case). If the data file gets 
larger than ten megabytes, the data in the file gets archived under the `Archives` directory with a timestamp. 
Variables such as `string length`, `data length`, `execution interval`, `data file names`, `keyword` and so on 
can be configured in the `config.py` file.

`Search:` It picks up data files from the config file and starts searching for the occurrence of a specific keyword
(‘CDS’ in current case). Upon completion of search, the search code writes the count along with data file name to a 
separate logs file in `filename – count` format with timestamp. If the logs file gets larger than ten megabytes, the
data in the file gets archived under the `Archives` directory with a timestamp. Variables such as `keyword`, 
`search interval`, `logs file name`, and so on can be configured in the `config.py` file.
 

## Prerequisites 

Please make sure these are installed on your system:

    1. Python 3.6+

    2. schedule library
       https://schedule.readthedocs.io/en/stable/
       pip install schedule


## Configure the App

Visit `/CDS/config.py` to set any variables that the application might use such as file names, execution intervals, data length, and so on.


## Run the Generator

Open the terminal and run the following commands:

1. `cd CDS` - Changes the directory to the project folder

2. `python3 generator.py` - Runs the generator script using Python

To stop the execution, you can use the keyboard shortcut `Ctrl + C`


## Run the Search

Open the terminal and run the following commands:

1. `cd CDS` - Changes the directory to the project folder

2. `python3 search.py` - Runs the generator script using Python

To stop the execution, you can use the keyboard shortcut `Ctrl + C`

## Notes

* Both generator & search should be run separately in two separate console/terminals. They will execute in parallel 
to each other
   
* You can now periodically monitor the results file to make sure the system is functioning.

* You can also monitor the terminal, which you used to kickstart the scripts, to check for updates.

`Sit back & relax!`