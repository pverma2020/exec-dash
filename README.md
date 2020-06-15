# exec-dash

# Project Description: https://github.com/prof-rossetti/intro-to-python/tree/master/projects/exec-dash

# Step 1: Install
Clone/download project repository from https://github.com/pverma2020/exec-dash
It is helpful to choose a familiar location like your Desktop. After coloing, be sure to navigate to the download location via the command line
For example, if you chose to download to your desktop, enter:
cd ~/Desktop/shopping-cart

# Step 2: Environment Setup
1. Create and activate a new Anaconda virtual environment (if you haven't already) by typing the following into your command line:

    conda create -n dashboard-env python=3.7 (this command is only required first time)
    conda activate shopping-env

2. From within the virtual environment, install any packages you may require:

    pip install pandas
    pip install matplotlib 

# Step 3: Run the program
Use the following command to run the script:
python dashboard_generator.py

Make sure the monthly sales CSV files reside inside a "data" sub-directory of the project repo. If the csv file has not been added, you will not be able to view it.

You will need to input the following:
Enter the year of the sales info you would like to view in YYYY format.
Enter the year of the sales info you would like to view in MM format.

A graphical representation of the data will pop up in a new window. You may need to close the chart window in order to see the text output print in the command line.