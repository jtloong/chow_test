# chow-test
Python module to calculate Chow break statistics. 

The Chow test was developed by econometrician Gregory Chow in 1960 to test whether one regression or two or more regressions best fit the time series data. It actually tests whether there is a structureal "break" in the dataset. More information can be found [on Wikipedia](https://en.wikipedia.org/wiki/Chow_test) and this [Statisitcis How To post](http://www.statisticshowto.com/chow-test/). 

Current version only supports simple linear models with a single x-variable, that have a time-axis in years as integers, and when finding breaks where k = 2. 

## Installation
Clone this repository, move into the directory, and install with pip:
```
git clone https://github.com/jtloong/chow-test.git
cd chow-test
pip install .
```
In your Python code you can import it as:
```
import chow_test
```

## Usage
The function has five parameters:
```
chow_test.calculate(Year, data, timeColumn, x_column, y_column)
```
Here are the requirements for these paramters:

| Parameter | Requirement                              |
|-----------|------------------------------------------|
| Year      | A valid year as an int                   |
| data      | A pandas dataframe of your data          |
| timeColumn| A string of the name of your time column |
| x_column  | A string of x-variable column name       |
| y_column  | A string of y-variable column name       |

## Future Ideas

* Build in functionality for complex linear models
* Enhance time comparison ability
* Ability to find more breaks in the data
