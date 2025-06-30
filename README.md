# Loan-Default-Predictions-for-American-Small-Businesses

The data used consists of nearly 50 years of loan data for American small businesses. The data was provided by Small Business Administration, a US government agency committed to helping small businesses propsper by connecting lenders with borrowers and assisting borrowers in successfully paying off their loans. 

In a high level, the project consists of the following steps:<br>
1. Initial data cleaning, such as removing nonsensical values and converting the data to the proper format for analysis.<br>
2. Exploratory data analysis (EDA), which consists of understanding statistical trends and patterns.<br>
3. Various machine learning models were developed and tested, with the goal of predicting loan defaults for the various loans in the dataset. The best performing model will be selected.<br>
4. The best performing model will be dissected to interpret what the model is doing and which factors are significant in predicting loan defaults.

# Setup
The "Loan Default Predictions.ipynb" file was initially run in Python 3.8.8. However, Python 3.8 is already obsolete when I checked on April 9, 2025. So we will use Python 3.10. setup.sh downloads the necessary Python packages, gets a virtual environment set up, gets the csv file necessary for this project, and runs the jupyter notebook. requirements.txt consists all the Python packages that are needed in this project. The instructions are provided below.

1. Use a linux Ubuntu environment <br>
2. Run
```bash
chmod +x setup.sh
./setup.sh
```
3. In the terminal, click on the link provided. You will see the Jupyter notebook UI in port 8888. <br>

You should now be able to run the jupyter notebook
