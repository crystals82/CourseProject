# CourseProject

Please fork this repository and paste the github link of your fork on Microsoft CMT. Detailed instructions are on Coursera under Week 1: Course Project Overview/Week 9 Activities.



Instructions to run the example notebook.
1. Clone the repo\
2. Create the python env needed to run the program by running the following \
   - conda env create --file tweet_env.yml\
3. Activate the env
   - conda activate tweet_env \
4. Navigate to the bsi_sentiment folder to install this custom package
   - cd dependencies/bsi-sentiment/ \
5. Install the custom version of bsi_sentiment
   - python setup.py install \
6. Navigate back to the root folder
   - Cd ../.. \
7. Add New Env to Jupyter Notebook Kernal
   - python -m ipykernel install --user --name=tweet_env \
8. Open the Jupyter Notebook \
   - jupyter notebook
11. Navigate to project/tweet_analysis_example.ipynb \
12. Open notebook \
13. Change kernel to tweet_env \
14. Follow instructions on notebook \
