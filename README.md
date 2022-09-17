# Insurance_Premium
AIM: To give people an estimate of how much they need based on their individual health situation. After that, customers can work with any health insurance carrier and its plans and perks while keeping the projected cost from our study in mind. This can assist a person in concentrating on the health side of an insurance policy rather than the ineffective part.
------------------

Dataset description

    Age: Person's age in years
    Sex: Gender of the person or insurance holder(Female or Male)
    BMI: Body mass index. The ideal range according to height and weight is 18.5 to 24.9
    Children: Number of dependents
    Smoker: Whether the insurance holder smokes or not
    Region: Residential area of the person
    Expenses: Individual medical costs billed by health insurance
------------------

APPROACH:
Loading the dataset using Pandas and performed basic checks like the size of the data, data type of each column and having any missing values. Also checked the uniq values of categorical columns.

Performed Exploratory data analysis:

To get even more better insights visualized independent feature with the target feature
    the distribution of the target feature, expenses which was in Normal distribution with a very little right skewness.

Data Transformation:

To standardise numerical columns i use standard scaler technique and to create dummy variables for categorical columns used onehotencoding.

Experimenting with various ML algorithms

Like LinearRegression, DecissionTreeRegressor, GradienBoostingRegressor and RandomForestRegressor ,performed hyper parameter tuning using the GridSearchCV and found the best hyperparameters for each model. Then, picked the top most features as per the feature importance by an each model. Models, evaluated on both the training and testing data and recorded the performance metrics. Based on the performance metrics of both the linear and the tree based models, random forest regressor performed the best among all.

Deployment: Deployed the best trained model using Flask, which works in the backend part while for the frontend used HTML5.

------------------

Software and account Requirement.

Github Account
[Heroku Account](https://dashboard.heroku.com/login)
VS Code IDE
GIT cli
GIT Documentation
Docker

------------------

Deployed app link
Heroku app link:  https://insuranceprem.herokuapp.com
