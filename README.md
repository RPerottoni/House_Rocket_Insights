This repository contains business analytics scripts of a real estate portfolio, but the business problem and the company are ficticial. <br>

# HOUSE ROCKET COMPANY - A INSIGHT PROJECT

<img src="https://github.com/RPerottoni/House_Rocket_Insights/blob/main/img/house.png" width=100% height=40%/>

## 1 About House Rocket

House Rocket is a company that is specialist in buying and resell properties. The business model is act as online platform and they realiase that they should use Data Science to help them to find the best business opportunities. <br>

The goal of this project is delivery insights for the company, helping them to find the best business opportunities, seeking to be more attractive for the customers, improving the company's profit.

The company strategy is based on buy good houses, and ressel them for a good price. The definition for what is a good house, good price to buy, to sell, are based on some criteria.

### 1.2 Context

The proprerties market is actually very competitive and if you are not updated, the tendency is reduce your profit and find potential customers will be much harder. Because of that, the House Rocket CEO thought to use DataScience seeking a profit improvement.

### 1.3 Bussiness Problem

There are two mainly reasons for this projetc:

a) The business team can't made good decisions without analyse the datas, due the number of the properties characteristics. And that makes the process very slow and the deals done are not profitable;

b) O portfólio é muito grande, o que levaria muito tempo para fazer o trabalho manualmente.

O objetivo desse projeto é fornecer uma seleção de imóveis, dadas as melhores condições, para que a empresa possa realizar suas operações de compra e venda. O planejamento é demonstrar através de visualizações, quais as melhores oportunidades e qual resultado (lucro) máximo que pode ser alcançado.

Em suma, o projeto visa responder às seguintes perguntas de negócio:

Quais são os imóveis que a House Rocket deveria comprar e por qual preço ?
Uma vez a casa comprada, qual o melhor momento para vendê-las e por qual preço ?


### 1.4 About the datas
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



### 1.5 Premissas




### 1.4 Business Assumptions


----
**References:**
* Python from Zero to DS lessons on Meigarom channel [Youtube](https://www.youtube.com/watch?v=1xXK_z9M6yk&list=PLZlkyCIi8bMprZgBsFopRQMG_Kj1IA1WG&ab_channel=SejaUmDataScientist)
* Blog [Seja um Data Scientist](https://sejaumdatascientist.com/os-5-projetos-de-data-science-que-fara-o-recrutador-olhar-para-voce/)
* Dataset from [Kaggle](https://www.kaggle.com/harlfoxem/housesalesprediction)
