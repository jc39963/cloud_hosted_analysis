# Cloud Hosted Notebook

## About the Project
The purpose of this project is to perform data manipulation tasks in a cloud hosted notebook. The analysis is done in Google Colab and the [dataset]("https://github.com/fivethirtyeight/data/tree/master/historical-ncaa-forecasts") is a dataset of NCAA tournament predictions along with whether the predicted games were won or not. In this analysis, we see what the actual win percentages are for games in various bins of win prediction probabilities. 


## Note on the repository and directions:
This repository also contains local files for CI/CD integration:
* requirements.txt detailing the requirements needed for this project
* Makefile to install requirements, lint, format, and test your code
* github actions 
* DockerFile and devcontainer for environment set up
* Jupyter notebook performing descriptive statistics and analysis + Cloud hosted notebook with badge
* main.py Python script for performing data manipulation and analysis
* test_main.py for Python testing scripts


## Description of Analysis
This analysis checks the actual win percentages of games grouped by what their projected win probabilities were. For example, were games that were predicted to have a 0.5 - 0.599 chance of winning actually won ~50 - 59% of the time? I display this data in a dataframe along with what their predicted win percentage bins are to see how accurate the predicted win percentages were. 


## Preparation
1. Open codespaces 
2. Load repo to code spaces
3. Wait for installation of all requirements in requirements.txt
4. Run main.py  

## Check format and test errors
1. Format code `make format`

2. Lint code `make lint`

3. Test code `make test`

(alternatively, do all with `make all`)




