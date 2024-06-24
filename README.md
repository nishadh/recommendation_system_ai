# Sentiment-based product recommendation system

> Sentiment-based product recommendation system by Nishadh Shrestha

## Heroku App

Deployed to: https://reco-app-4e9028a3ad63.herokuapp.com/

## Table of Contents

- [General Info](#general-information)
- [Models trained](#models-trained)
- [Technologies Used](#technologies-used)
- [Conclusions](#conclusions)
- [Acknowledgements](#acknowledgements)

<!-- You can include any other section that is pertinent to your problem -->

## General Information

The aim of this project is to build a model that will improve the recommendations given to the users given their past reviews and ratings.

**Directories:**

- The notebook folder includes the dataset, Jupyter notebook, and all generated pickle assets.
- The flask folder contains the Flask application for the final recommendation system, which was also deployed to Heroku.

<!-- You don't have to answer all the questions - just the ones relevant to your project. -->

## Models trained

|               Model | Accuracy |  ROC AUC |   Recall | Precision | F1 Score |
| ------------------: | -------: | -------: | -------: | --------: | -------: |
| Logistic Regression | 0.882556 | 0.900992 | 0.908751 |  0.957503 | 0.932490 |
|              LGBM 2 | 0.898889 | 0.898878 | 0.938006 |  0.948157 | 0.943054 |
|                LGBM | 0.902111 | 0.896776 | 0.942736 |  0.947336 | 0.945030 |
|       Random Forest | 0.895667 | 0.869070 | 0.944355 |  0.939094 | 0.941717 |
|             XGBoost | 0.853778 | 0.588613 | 0.950703 |  0.892486 | 0.920675 |

## Technologies Used

- numpy 1.25.2
- pandas 2.1.4
- pycaret 3.3.2
- seaborn 0.12.2
- nltk 3.8.1
- spacy 3.7.4

and more...

<!-- As the libraries versions keep on changing, it is recommended to mention the version of library used in this project -->

## Conclusions

We trained several models and chose Logistic Regression for sentiment analysis due to its superior performance. We opted for user-based collaborative filtering for the recommendation system because of its lower error rate. The project was packaged as a Flask application and deployed on Heroku.

## Acknowledgements

- Theory - Sentiment Based Product Recommendation System course

## Contact

Created by [@nishadh] - feel free to contact me!
