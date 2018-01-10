# chow-test
Python module to calculate Chow break statistics.

The Chow test was developed by econometrician Gregory Chow in 1960 to test whether one regression or two or more regressions best fit the time series data. It actually tests whether there is a structural "break" in the dataset. More information can be found [on Wikipedia](https://en.wikipedia.org/wiki/Chow_test) and this [Statistics How To post](http://www.statisticshowto.com/chow-test/).

Here is the formula:
</br><img src='http://www.statisticshowto.com/wp-content/uploads/2016/10/chow-test-formula.png'>

Current version only supports simple linear models with a single x-variable, that have a time-axis in years as integers, and when finding breaks where k = 2.

You can find my blog post about this package [here](http://joshualoong.com/2018/01/05/Building-the-Python-chow-test-Package/).

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
The function has four parameters:
```
chow_test.f_value(breakpoint, index, y, x)
```
Here are the requirements for these parameters:

| Parameter | Requirement                              |
|-----------|------------------------------------------|
| breakpoint| A valid year as an int                   |
| index     | A numpy array of the time-axis in years  |
| y         | A numpy array of the y-variables         |
| x         | A numpy array of the x-variables         |

## Future Ideas

* Build in functionality for complex linear models
* Enhance time comparison ability
* Ability to find more breaks in the data
