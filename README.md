# CourseProject

Please fork this repository and paste the github link of your fork on Microsoft CMT. Detailed instructions are on Coursera under Week 1: Course Project Overview/Week 9 Activities.

T20 Cricket World Cup Tweet Analysis Project
In this project, we set out to mine a large number of tweets and answer the high level question of are the predictions that are made on twitter about a sporting even accurate and is their a coorelation with who wins?

We have built a notebook that you can walk through to see what we did for our analysis and be able to test out some of the code on your own.

This notebook can be used as a starting point and altered to do further analysis to answer other questions.

In order to run the analysis notebook follow the instructions below:

Instructions:
1. Clone the rep
2. Create the python env needed to run the program by running the following 
   - conda env create --file tweet_env.yml
3. Activate the env
   - conda activate tweet_env 
4. Navigate to the bsi_sentiment folder to install this custom package
   - cd dependencies/bsi-sentiment/ 
5. Install the custom version of bsi_sentiment
   - python setup.py install 
6. Navigate back to the root folder
   - Cd ../.. 
7. Add New Env to Jupyter Notebook Kernal
   - python -m ipykernel install --user --name=tweet_env 
8. Open the Jupyter Notebook 
   - jupyter notebook
11. Navigate to project/tweet_analysis_example.ipynb
12. Open notebook 
13. Change kernel to tweet_env 
14. Follow instructions on notebook 
