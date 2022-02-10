This repository contains business analysis scripts of a real estate portfolio, but the business problem and the company are ficticial. <br>

# HOUSE ROCKET COMPANY - A INSIGHT PROJECT

<img src="https://github.com/RPerottoni/House_Rocket_Insights/blob/main/img/house.png" width=70% height=60%/>

## 1. About House Rocket

House Rocket is a company that is specilist in buying and resell properties. The business model is act as online platform and they are starting to use the technology to find the best business opportunities, seeking to improve their profit and be more competitive.<br>

---
## 2. Business Problem

The proprerties market is actually very competitive and if you are not updated, the tendency is reduce your profit and find potential customers will be much harder. Because of that, the House Rocket CEO thought to use DataScience seeking a profit improvement.

## 3. Business Results


## 4. Business Assumptions

* Available data are only from May 2014 to May 2015.
* There was a value where the number of bedrooms is vast compared to other houses, so this data was removed, assuming it was an input error.
* When the houses could be sold on different seasons, considered just one to analyze the most suitable season to sell it.
* Seasons of the year:<br>
   * Spring starts on March 1 st<br>
   * Summer starts on June 1 st<br>
   * Fall starts on September 1 st<br>
   * Winter starts on December 1 st<br>

<br>

* The variables on the original dataset are:<br>

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

## 5. Solution Strategy
My strategy to solve this challenge was:
1. Understanding the business model 
2. Understanding the business problem
3. Collecting the data
4. Data Description
5. Data Filtering
6. Feature Engineering
8. Exploratory Data Analysis
9. Insights Conclusion
10. Dashboard deploy on [Heroku](https://houserocketri-analytics.herokuapp.com/)


## 6. Top Data Insights

## 7. Conclusion

## 8. Next Steps



----
**References:**
* Python from Zero to DS lessons on Meigarom channel [Youtube](https://www.youtube.com/watch?v=1xXK_z9M6yk&list=PLZlkyCIi8bMprZgBsFopRQMG_Kj1IA1WG&ab_channel=SejaUmDataScientist)
* Blog [Seja um Data Scientist](https://sejaumdatascientist.com/os-5-projetos-de-data-science-que-fara-o-recrutador-olhar-para-voce/)
* Dataset from [Kaggle](https://www.kaggle.com/harlfoxem/housesalesprediction)
