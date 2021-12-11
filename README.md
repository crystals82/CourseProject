# CourseProject

## T20 Cricket World Cup Tweet Analysis Project


Watch our presentation and demo of this project here: https://mediaspace.illinois.edu/media/t/1_1lswv7yg


### Overview of the project goal
In this project, we set out to mine a large number of tweets and answer the high level question of is there a coorelation between the polarity/confidence of what the prediction made in the tweet and the accuracy of the predicted outcomes. For example, if there is a tweet that says "I think Pakistan is going to dominate India today" we want to verify if this prediction is right and then check to see if there is a coolerlation between the success of the prediction and the polarity of the language used in the prediction.

### What you can use this code for
We have built a notebook that you can walk through to see what we did for our analysis and be able to test out some of the code on your own.
This notebook can be used as a starting point and altered to do further analysis to answer other questions.

### Documentation of the usage of the software 

In order to run the analysis notebook follow the instructions below:

Instructions:
1. Clone the rep
2. Create the python env needed to run the program by running the following command in your terminal 
   - conda env create --file tweet_env.yml python=3.7
3. Activate the env by running the following command in your terminal 
   - conda activate tweet_env 
4. Navigate to the bsi_sentiment folder to install this custom package by running the following command in your terminal
   - cd dependencies/bsi-sentiment/ 
5. Pip install a few other packages by running the following commands in your terminal:
   - pip install pandas
   - pip install selenium
   - pip install webdriver_manager
   - pip install sklearn
   - pip install matplotlib
   - pip install jupyter notebook
7. Install the custom version of bsi_sentiment by running the following command in your terminal
   - python setup.py install 
8. Navigate back to the root folder  by running the following command in your terminal
   - Cd ../.. 
9. Add New Env to Jupyter Notebook Kernal by running the following command in your terminal
   - python -m ipykernel install --user --name=tweet_env 
10. Open the Jupyter Notebook by running the following command in your terminal
   - jupyter notebook
11. Navigate to project/tweet_analysis_example.ipynb with in the Jupyter Notebook Portal
12. Open the analysis notebook by clicking on the file of 'tweet_analysis_example.ipynb'
13. Change kernel to tweet_env within the jupyter notebook
14. Follow the instructions on notebook 




### Team Member Contributions:

Adam Ruther:

Discovered how to pull historical tweets without using Tweepy
Wrote the code to pull the tweets
Wrote the code to build the schedule scraper
Wrote the code to filter the tweets down to only tweets that pertained to the matches 
Coded the Feature logic to extract features for the Logistic Regression Classification Model
Trained the model using the test data
Used the model for the predictions
created the plots
modularized the code
created final documentation
created final jupyter notebook

Prasanna Kumar:
1. Coordinated the tweepy API access for initial proof of concepts
2. Coordinated Project progress report & overview to list down different tasks involved in the application design & build
3. Built & tested code for sentiment analysis using text blob and retrieved subjectivity, polarity scores for various tweets
4. Data collection for prediction terms (BoW), Sentiment analysis
5. Extensive testing of the application for training the model and recording the prediction outcomes
6. Final project documentation and presentation

Surabhi Choudhary:
Part of initial app design and task determination. Data collection via Tweepy and then research on sentiment analysis using TextBlob. Later identified limitations of using Tweepy/Twitter API which would have severely limited the dataset for this project. Researched on ways to work around the issue. Discovered the worldcup tweets dataset on Kaggle which was nightly updated and had all tweets we needed.Pulled that in python and cleaned it up to ready it for keyword filtering. Researched on the data itself to help build the classifier however due to time constraints I could not assist with the classifier itself. Assisted in development of test/training set of the classifier.
