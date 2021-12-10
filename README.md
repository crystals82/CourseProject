# CourseProject

Please fork this repository and paste the github link of your fork on Microsoft CMT. Detailed instructions are on Coursera under Week 1: Course Project Overview/Week 9 Activities.

Git clone ‘’
conda env create --file tweet_env.yml
conda activate tweet_env
cd dependencies/bsi-sentiment/
python setup.py install
Cd ../..
python -m ipykernel install --user --name=tweet_env
Jupyter notebook

Navigate to project/tweet_analysis_example.ipynb
Open notebook
Change kernel to tweet_env
Follow instruction on notebook