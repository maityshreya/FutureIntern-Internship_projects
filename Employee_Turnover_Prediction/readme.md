 # Objective: -
Employee turnover refers to the total number of workers who leave a company over a certain time period. It includes those who exit voluntarily as well as employees who are fired or laid off — that is, involuntary turnover.

Resigning means you’re voluntarily leaving your job. When you resign, you give up all of the responsibilities associated with your job and also lose your benefits, including your salary.

The goal of this challenge is to build a machine learning model that predicts the chances of an employee turnover.
 
 # Dataset
 This database is from a large US company (no name given for privacy reasons). The management department is worried about the relatively high turnover. They want to find ways to reduce the number of employees leaving the company and to better understand the situation, which employees are more likely to leave, and why.

 The data¶
The HR department has assembled data on almost 10,000 employees who left the company between 2016-2020. They used information from exit interviews, performance reviews, and employee records.

department - the department the employee belongs to.

promoted - 1 if the employee was promoted in the previous 24 months, 0 otherwise.
review - the composite score the employee received in their last evaluation.
projects - how many projects the employee is involved in.
salary - for confidentiality reasons, salary comes in three tiers: low, medium, high.
tenure - how many years the employee has been at the company.
satisfaction - a measure of employee satisfaction from surveys.
bonus - 1 if the employee received a bonus in the previous 24 months, 0 otherwise.
avg_hrs_month - the average hours the employee worked in a month.
left - "yes" if the employee ended up leaving, "no" otherwise.

# Features
-Import libraries<br>
-loading data<br>
-apply EDA<br>
-Modelling<br>
-Randomdorest<br>

# Project Structure
The project is structured as follows:

- app.py: Flask web application for serving predictions.
- model/: Directory containing trained model and preprocessing objects.
- dataset/: Directory containing the dataset used for training.

# Technologies Used
-Python<br>
-Flask<br>
-pandas<br>
-numpy<br>
-scikit-learn<br>
