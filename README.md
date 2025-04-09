# Loan-Default-Predictions-for-American-Small-Businesses

The data used can be collected from the following link below <br>
https://www.kaggle.com/mirbektoktogaraev/should-this-loan-be-approved-or-denied

If the dataset and/or link no longer exists, please contact me at nathanling9730@gmail.com and I will send it to you accordingly.

The data used consists of nearly 50 years of loan data for American small businesses. The data was provided by Small Business Administration, a US government agency committed to helping small businesses propsper by connecting lenders with borrowers and assisting borrowers in successfully paying off their loans. 

In a high level, the project consists of the following steps:<br>
1. Initial data cleaning, such as removing nonsensical values and converting the data to the proper format for analysis.<br>
2. Exploratory data analysis (EDA), which consists of understanding statistical trends and patterns.<br>
3. Various machine learning models were developed and tested, with the goal of predicting loan defaults for the various loans in the dataset. The best performing model will be selected.<br>
4. The best performing model will be dissected to interpret what the model is doing and which factors are significant in predicting loan defaults.

# Setup
The "Loan Default Predictions.ipynb" file was initially run in Python 3.8.8. However, Python 3.8 is already obsolete when I checked on April 9, 2025. So we will use Python 3.10. In this folder is a requirements.txt file, which contains all the libraries needed.
Run the following in your command line:
1. sudo apt-get update
3. sudo apt-get install python3.10 -y
4. sudo apt-get install pip -y
5. sudo apt install python3.10-venv
6. python3 -m venv venv
7. source venv/bin/activate
8. pip install -r requirements.txt
9. pip install notebook==7.4.0
10. jupyter notebook
11. Once you run "jupyter notebook", click on the link provided in the terminal. You will see the Jupyter notebook UI in port 8888.

You should now be able to run the jupyter notebook
