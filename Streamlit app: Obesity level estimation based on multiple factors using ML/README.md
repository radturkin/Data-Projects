# Obesity level estimation based on multiple factors
## with additional resources to find sustainable options for improved weight management and overall health

Obesity is a major crisis in the US, that can negatively impact both the indiviudals health and that of the overall healthcare system. However despite the many challenges that come with obesity, many struggle to maintain or achieve a healthy weight.The aim of this project is to look at various features that can potentially impact a persons health and weight, and see which are most impactful, and provide insight and options to those that are currently struggling with weight or working with those that do, to make the most achievable and informed changes to diet and/or lifestyle, with a focus on the individuals preference.

# Data Dictionary

Data is originally from this study: 
"Dataset for estimation of obesity levels based on eating habits and physical condition in individuals from Colombia, Peru and Mexico"
[here](https://www.sciencedirect.com/science/article/pii/S2352340919306985)


|Feature|Type|Dataset|Description|
|---|---|---|---|
|**Gender**|*object*|gender|
|**Age**|*float64*|age|
|**Height**|*float64*|height in meters|
|**Weight**|*float64*|weight in kg|
|**family_history_with_overweight**|*object*|yes or no values for history of family member being overweight|
|**FAVC**|*object*|Frequent consumption of high caloric food, yes or no|
|**FCVC**|*float64*|Frequency of consumption of vegetables as values 1-3|
|**NCP**|*float64*|Number of main meals as values 1-4|
|**CAEC**|*object*|Consumption of food between meals as string value of frequency|
|**SMOKE**|*object*|does patient smoke yes or no|
|**CH2O**|*float64*|Consumption of water daily in liters as float value 1-3|
|**SCC**|*object*|Calories consumption monitoring, yes or no|
|**FAF**|*float64*|Physical activity frequency value between 0-3|
|**TUE**|*float64*|Time using technology devices in hours per day|
|**CALC**|*object*|Consumption of alcohol as string value of frequency|
|**MTRANS**|*object*|Transportation used as string value for transportation used|
|**NObeyesdad**|*object*|weight level category 7 different string values|

# Data Cleaning and Collection

Most of the data is synthetic the original 2111 rows were 77% synthetic to balance out the different obesity ("Nobeyesdad") values since most of the original were of "Normal Weight" it was then combined with additional synthetic data (20758 rows) built from the original data. Due to its primarily synthetic nature little cleaning was necessary, however for much of the analysis should be compared against the original data collected from the online survey against the synthetic data to look for any noticeable inconsistencies that may have been created during the synthetic generation of the rest of the data. One important thing to note is that the synthetic data took on float values that while they do not disrupt the data, do provide unusual interpretations for the anallysis of some columns and as such ocassionally rounding to integers will need to take place.

# EDA and Preliminary Analysis
## major issue with synthetic data after review of original data
## review of important features
using the xgboostclassifier model and reviewing the most important features after weight and height. Age, FAF, TUE, CH2O, FCVC, NCP were most important for the classification model, so we investigate why, sepcifically of most interest was age.

# Findings and Technical Report
The best classification models were able to all perform at over 90% accuracy, however, it is testing against its own synthetic data, so while the results seem good, there are lots of questions about how well the model would hold up against new non synthetic data. Testing out the streamlit app on different users, seems to show good accuracy as well in predicting the correct weight class. It would be good to store user inputs to generate additional data, though it would require a certain amount of trust in the accuracy of user input.

# Presentation 
The best model was used for the streamlit app, where users can input their own values and receive the output of their weight class. Initially I attempted to use Snowflakes Arctic to then offer recommendations to the user based on their preferences for weight class achievements. However, there is currently an issue with one of the imports necessary for snowflakes arctip llm to function inside of our streamlit app, which will require further investigation.

# Executive Summary

# Further Study
Gather more data from app, or other sources to test how well synthetic data holds up.
Merge the two severely obese classes into a single obesity class and regenerate new synthetic data with improved sampling for this particular weight class.
Resolve Snowflake Arcic LLM import issue to build a more functional and useful app.

