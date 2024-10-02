# An Exploration of the Decline of Life Expectancy in the US

In recent years the US has received a lot of attention for its decrease in life expectancy. In this analysis we explore the correlation between wealth inequality and life expectancy in the US; viewing the life expectancy and Gini Index across multiple countries we will attempt to explore and extrapolate quantitative evidence of the divergence in life expectancy in the US against similar countries.


# Data Dictionary

All data used is taken from [GapMinder](https://www.gapminder.org/)

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**Life Expectancy**|*integer*|GapMinder|Life Expectancy by country and year year|
|**Population**|*integer*|GapMinder|Population by country and year|
|**GNI**|*integer*|GapMinder|Gross National Income yb country and year|
|**Gini Index**|*integer*|GapMinder|Gini Index (measure of wealth inequality) by country and year|


# Executive Summary

This project will attempt to identify the key moments in US history that have led to the decrease in life expectancy by viewing data across other countries and identifying the moment of clear divergence as well as key indicators via the Gini Index.

The four main data sets were all accessed via GapMinder (linked above). The data was then cleaned, and analyzed looking specifically at data post 1950s. Based on initial analysis it was clear that the US problem of life expectancy began to take hold in the 1980s so a subset of data was collected from what will be referred to as "Select Countries". These select countries were chosen for their high GNI and populations (over 32,000 and 75 million, respectively) countries were also chosen if their GNI and population was high in 2019 (over 50,000, and 100 million, respectively). The data was then visualized as hisograms, and line graphs to view trends, signifigant moments, and other transformations over time.While some of these countries pose as anomalies and hav questionability in their datas accruacy overall. 

The data identifies unique highly correlated trends between Gini Index and Life Expectancy across these countries. The findings suggest that countries with very high life expectancy (over 80) all had Gini Index values between 24-34. Where as the US has had a growing Gini Index that continues to trend upwards, approaching 40 in the 80s and crossing into 40 in 1994 and continuind to increase, which correlates with the trending divergence of life expectancy in the US. There was a much stronger correlation between a healthy Gini Index and high life expectancy, than for countries with high Gini Index values. 

This evidence suggests that the massive and growing wealth inequality in the US is likely the leading cause of our decreasing life expectancy; if action is not taken to resolve we should expect life expectancy to continue to decrease and the majority of the American people to suffer. The best course of action would be to generate more agressive graduated income taxes, and income caps for the uber wealthy and large corporations, with stricter penalties for evasion. The excess should be used to provide services such as Universal Basic Income and Healthcare, with a target goal of reaching a Gini Index under 34.
