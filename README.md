This repository contains business analytics scripts of a real estate portfolio, but the business problem and the company are ficticial. <br>

# HOUSE ROCKET COMPANY

<img src="https://github.com/RPerottoni/House_Rocket_Insights/blob/main/img/house.png" width=100% height=40%/>

## About House Rocket

House Rocket is a company that is specialist in buying and resell properties using technology. The business model is act as online platform and they realiase that they should use Data Science to help them to find the best business opportunities. <br>

The goal of this project is delivery insights for the company in order to find the best business opportunities, seeking to be more attractive for the customers, increasing the company's profit.

The strategy to achieve this goal is to buy good houses in great locations at low price and resell them for a hight price.
However, the properties have many attributes that make them more or less attractive to buyers and sellers, furthermore the location and time of year can also influence prices.

### Business Questions

Seeking to achieve the goal, there are two mainly questions thats directs the project:

1. Which properties the company should buy and how much they should pay for each property?

2. Once purchased, when the company should resell and what should be the price?

### About the datas

The dataset contains information about the properties that was sold between May 2014 and may 2015 and is possible to download the dataset following the link https://www.kaggle.com/harlfoxem/housesalesprediction

The description about the variables can be checked bellow:

Variable | Definition
------------ | -------------
|id | Identification number of each property|
|date | The date when the property was available|
|price | The price of each property considered as the purchase price |
|bedrooms | Number of bedrooms|
|bathrooms | The number of bathrooms, the value .5 indicates a room with a toilet but no shower. The value .75 or 3/4 bathroom represents a bathroom that contains one sink, one toilet, and either a shower or a bath.|
|sqft_living | Square feet of the houses interior space|
|sqft_lot | Square feet of the houses land space |
|floors | Number of floors|
|waterfront | A dummy variable for whether the house was overlooking the waterfront or not, ‘1’ if the property has a waterfront, ‘0’ if not|
|view | An index from 0 to 4 of how good the view of the property was|
|condition | An index from 1 to 5 on the condition of the houses, 1 indicates worn-out property and 5 excellent|
|grade | An overall grade is given to the housing unit based on the King County grading system. The index from 1 to 13, where 1-3 falls short of building construction and design, 7 has an average level of construction and design, and 11-13 has a high-quality level of construction and design|
|sqft_above | The square feet of the interior housing space that is above ground level|
|sqft_basement | The square feet of the interior housing space that is below ground level|
|yr_built | Built year of the property |
|yr_renovated | Represents the year when the property was renovated. It considers the number ‘0’ to describe the properties never renovated.|
|zipcode | A five-digit code to indicate the area where the property is in|
|lat | Latitude|
|long | Longitude|
|sqft_living15 | The square feet average size of interior housing living space for the closest 15 houses|
|sqft_lot15 | The square feet average size of land lots for the closest 15 houses|
<br>

### Solution Strategy 

Step 01 - Define and understanding the business problem; <br>

Step 02 - Select and inspect the datas; <br>

Step 03 - Data cleaning and transforming; <br>

Step 04 - Exploratory Data Analysis; <br>

Step 05 - Business Hypothesis definition and validation; <br>

Step 06 - Business questions answering; <br>

Step 07 - App creation; <br>

Step 08 - Conclusion and Understanting the Business results; <br>

### Business Assumptions <br>

There are the considerations that was made: <br>
**Duplicated ID's**: were removed. <br>
**Outliers**: was replaced by the median value for that variable. <br>
**Good properties to buy:** Are the properties were the price is lower than the median price by region (zipcode) and the house condition is good (higher than 3). <br>
**Price to buy:** The price to buy needs to be lower than the region median price. <br>
**The best time to sell:** According to the date, was created and defined a new feature: season. And the datas was classified by season. The best time to sell is the season where the profit is higer.<br>
**Price to sell:** The price to sell was defined according the following criteria: If the median price by season is higher than the property price, the selling price will be 30% over the price to buy and if the median price by season is lower than the property price, the selling price will be 10% over the price to buy.<br>

### Main Insights <br>

**1. Properties that is water front are 20% more expensive.**
 Hypothesis is true. Properties that are waterfront costs 68 % more than the properties are not water front. <br>

**2. Properties that was built before 1955 are 50% cheaper.**
 Hypothesis is true. Properties builted before 1955 are 0.78 % more cheaper. But the difference is insignificant.<br>

**3. Properties without basement are 40% bigger that the others.**
 Hypothesis is true. Properties without basement are 18.41 % bigger than properties with basement.<br>

**4. YoY ( Year over Year ) property price growth is 10%.**
Hypothesis is true. The price grew up 0.52 %.<br>

**5. Month over Month price growth is 15% for properties with 3 bathrooms.**
Hypothesis is false, the price does not show growth.<br>

**6. Properties in bad conditions but is water front are more expensive thant properties in good condition but is not water front.**
Hypothesis is true. Water front properties in bad conditions are more expensive than properties in good condition but are not water front.

**7. Properties that are not waterfront are smaller than the properties that are water front.**
Hypothesis is true. Properties that are water front are bigger than properties that are not water front. <br>

**8. Properties renovated are 20% more expensive than the properties that are not renovated.**
Hypothesis is false. Properties not renovated are 30.25 % more expensive than the properties that was renovated.<br>

**9. Houses with more than 3 bedrooms cost 40% more than properties that have less bedrooms.**
Hypothesis is true. Properties with more than 3 bedrooms costs 29.71 % more than the properties with less than 3 bedrooms. <br>

**10. At the winter there are 35% more properties to sell than the summer.**
Hypothesis is true. At the winter there are 45 % more properties to sell than the summer.<br>

### Results

According to the analysis, there are 3863 properties available that fit in the predefined conditions. And, if the CEO decide to buy all those houses and resell them, the profit will be $1.124.865.171,00.

### Conclusions

Although simple, the insights projects is based on a exploratory data analysis allows achive good result faster and it is a good point to start.
Through this analysis was possible to answers the main business questions and find some intersting insights that can help the company make better decisions.
As a result of this project, there is dashboard, where could be accessed by the link https://houserocketri-analytics.herokuapp.com/. <br>
There is possible to see the answers about the business questions, and the insights obtained.

### Next Steps
As the next steps is possible to improve these analysis, by doing feature engineering and consider the ML Algorithm implemention.

----
**References:**
Youtube Channel [Seja um Data Scientist](https://www.youtube.com/c/SejaUmDataScientist)

