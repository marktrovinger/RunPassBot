# Run-Pass Bot
Run-Pass Bot is a twitter bot that is designed to make predictions if a team is more likely to call a running play or a passing play. The model is trained on the play-by-play data from the 2009-2015 seasons. The twitter bot will use a (near) real-time data source to tweet predictions.

## The Data
The data from this project comes directly from the NFL, through the use of the [nflscrapR package](https://github.com/maksimhorowitz/nflscrapR). Data was pulled from the 2009-2015 regular seasons. 

## Machine Learning
Given that this is a Python project, it uses [sci-kit learn](http://scikit-learn.org/stable/) for its machine learning library.

## Twitter App
The purpose of the app, similarly to [New York Times 4th Down Bot](http://nyt4thdownbot.com/), is is predict the outcome of a given play in the NFL. Currently, while the Twitter app is implemented, the lack of an affordable real-time data source has limited its usefulness.