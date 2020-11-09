# Alberta COVID-19 Tracking Repository

 A small personal project currently undergoing active development. The focus of this project is to scrape data from Alberta Health Srvices, apply different visualization/analysis techniques to what data is obtained, and attempt to deploy it using ReactJS.

 Required Packages:
 - python packages in `requirements.txt`
 - requires [chromedriver](https://chromedriver.chromium.org/) to be in PATH or in directory for web scraping

----
## Table of Contents
1. Web Scraping with Python
2. Visualization and Prediction with Jupyter
3. Deployment with ReactJS

I am currently working on step 2.

----
## Web Scraping with Python
A simple python scraping script was built with the selenium package and chromedriver. Running `scrape.py` will automatically acces the [AHS website](https://www.alberta.ca/stats/covid-19-alberta-statistics.htm) and download the latest csv file to the local `info/` directory.

----
## Visualization
**Mean**:
Taking the daily mean using a step size of (1/n). This is the same calculated result as (sum of cases)/(# of days), with a very minor improvement in efficiency as you do not need to recalculate the sum for each new day.

**Weighted Average**:
Taking the weighted average using a constant step size. More "recent" days in calculation are weighed more heavily depending on the exact step size.

----
## Sources
Reinforcement Learning Algorithms:

Sutton, R. S., Bach, F., &amp; Barto, A. G. (2018). Reinforcement Learning: An Introduction. Massachusetts: MIT Press.

<br>

Monte Carlo Simulations:

Xie, G. A novel Monte Carlo simulation procedure for modelling COVID-19 spread over time. Sci Rep 10, 13120 (2020). https://doi.org/10.1038/s41598-020-70091-1