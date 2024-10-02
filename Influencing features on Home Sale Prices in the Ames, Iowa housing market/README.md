# Influencing features on Home Sale Prices in the Ames, Iowa housing market

The purpose of this project is to identify features that have a strong correlation to house sale prices on the Ames, Iowa dataset. With an intended application being for an audience of home owners or future home owners on how to improve their homes sale value, or get a good deal on a home.

# Data Dictionary

All data used is taken from [De Cock D. 2011. Ames, Iowa: Alternative to the Boston Housing Data as an End of Semester Regression Project. Journal of Statistics Education; 19(3)](https://jse.amstat.org/v19n3/decock.pdf)

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**Train**|*csv file*|De Cock|A subset of Alternative to the Boston Housing Data for analysis|
|**Test**|*csv file*|De Cock|A subset of Alternative to the Boston Housing Data for model testing|

Click below to see details of columns and categorical value meanings
<details>
  <summary>Data Column Details</summary>
	SalePrice - the property's sale price in dollars.
	
	MSSubClass: The building class
	
	MSZoning: The general zoning classification
	
	LotFrontage: Linear feet of street connected to property
	
	LotArea: Lot size in square feet
	
	Street: Type of road access
	
	Alley: Type of alley access
	
	LotShape: General shape of property
	
	LandContour: Flatness of the property
	
	Utilities: Type of utilities available
	
	LotConfig: Lot configuration
	
	LandSlope: Slope of property
	
	Neighborhood: Physical locations within Ames city limits
	
	Condition1: Proximity to main road or railroad
	
	Condition2: Proximity to main road or railroad (if a second is present)
	
	BldgType: Type of dwelling
	
	HouseStyle: Style of dwelling
	
	OverallQual: Overall material and finish quality
	
	OverallCond: Overall condition rating
	
	YearBuilt: Original construction date
	
	YearRemodAdd: Remodel date
	
	RoofStyle: Type of roof
	
	RoofMatl: Roof material
	
	Exterior1st: Exterior covering on house
	
	Exterior2nd: Exterior covering on house (if more than one material)
	
	MasVnrType: Masonry veneer type
	
	MasVnrArea: Masonry veneer area in square feet
	
	ExterQual: Exterior material quality
	
	ExterCond: Present condition of the material on the exterior
	
	Foundation: Type of foundation
	
	BsmtQual: Height of the basement
	
	BsmtCond: General condition of the basement
	
	BsmtExposure: Walkout or garden level basement walls
	
	BsmtFinType1: Quality of basement finished area
	
	BsmtFinSF1: Type 1 finished square feet
	
	BsmtFinType2: Quality of second finished area (if present)
	
	BsmtFinSF2: Type 2 finished square feet
	
	BsmtUnfSF: Unfinished square feet of basement area
	
	TotalBsmtSF: Total square feet of basement area
	
	Heating: Type of heating
	
	HeatingQC: Heating quality and condition
	
	CentralAir: Central air conditioning
	
	Electrical: Electrical system
	
	1stFlrSF: First Floor square feet
	
	2ndFlrSF: Second floor square feet
	
	LowQualFinSF: Low quality finished square feet (all floors)
	
	GrLivArea: Above grade (ground) living area square feet
	
	BsmtFullBath: Basement full bathrooms
	
	BsmtHalfBath: Basement half bathrooms
	
	FullBath: Full bathrooms above grade
	
	HalfBath: Half baths above grade
	
	Bedroom: Number of bedrooms above basement level
	
	Kitchen: Number of kitchens
	
	KitchenQual: Kitchen quality
	
	TotRmsAbvGrd: Total rooms above grade (does not include bathrooms)
	
	Functional: Home functionality rating
	
	Fireplaces: Number of fireplaces
	
	FireplaceQu: Fireplace quality
	
	GarageType: Garage location
	
	GarageYrBlt: Year garage was built
	
	GarageFinish: Interior finish of the garage
	
	GarageCars: Size of garage in car capacity
	
	GarageArea: Size of garage in square feet
	
	GarageQual: Garage quality
	
	GarageCond: Garage condition
	
	PavedDrive: Paved driveway
	
	WoodDeckSF: Wood deck area in square feet
	
	OpenPorchSF: Open porch area in square feet
	
	EnclosedPorch: Enclosed porch area in square feet
	
	3SsnPorch: Three season porch area in square feet
	
	ScreenPorch: Screen porch area in square feet
	
	PoolArea: Pool area in square feet
	
	PoolQC: Pool quality
	
	Fence: Fence quality
	
	MiscFeature: Miscellaneous feature not covered in other categories
	
	MiscVal: $Value of miscellaneous feature
	
	MoSold: Month Sold
	
	YrSold: Year Sold
	
	SaleType: Type of sale
	
	SaleCondition: Condition of sale
  
		MSSubClass: Identifies the type of dwelling involved in the sale.	

			20	1-STORY 1946 & NEWER ALL STYLES
			30	1-STORY 1945 & OLDER
			40	1-STORY W/FINISHED ATTIC ALL AGES
			45	1-1/2 STORY - UNFINISHED ALL AGES
			50	1-1/2 STORY FINISHED ALL AGES
			60	2-STORY 1946 & NEWER
			70	2-STORY 1945 & OLDER
			75	2-1/2 STORY ALL AGES
			80	SPLIT OR MULTI-LEVEL
			85	SPLIT FOYER
			90	DUPLEX - ALL STYLES AND AGES
		       120	1-STORY PUD (Planned Unit Development) - 1946 & NEWER
		       150	1-1/2 STORY PUD - ALL AGES
		       160	2-STORY PUD - 1946 & NEWER
		       180	PUD - MULTILEVEL - INCL SPLIT LEV/FOYER
		       190	2 FAMILY CONVERSION - ALL STYLES AND AGES

		MSZoning: Identifies the general zoning classification of the sale.

		       A	Agriculture
		       C	Commercial
		       FV	Floating Village Residential
		       I	Industrial
		       RH	Residential High Density
		       RL	Residential Low Density
		       RP	Residential Low Density Park 
		       RM	Residential Medium Density

		LotFrontage: Linear feet of street connected to property

		LotArea: Lot size in square feet

		Street: Type of road access to property

		       Grvl	Gravel	
		       Pave	Paved

		Alley: Type of alley access to property

		       Grvl	Gravel
		       Pave	Paved
		       NA 	No alley access

		LotShape: General shape of property

		       Reg	Regular	
		       IR1	Slightly irregular
		       IR2	Moderately Irregular
		       IR3	Irregular

		LandContour: Flatness of the property

		       Lvl	Near Flat/Level	
		       Bnk	Banked - Quick and significant rise from street grade to building
		       HLS	Hillside - Significant slope from side to side
		       Low	Depression

		Utilities: Type of utilities available

		       AllPub	All public Utilities (E,G,W,& S)	
		       NoSewr	Electricity, Gas, and Water (Septic Tank)
		       NoSeWa	Electricity and Gas Only
		       ELO	Electricity only	

		LotConfig: Lot configuration

		       Inside	Inside lot
		       Corner	Corner lot
		       CulDSac	Cul-de-sac
		       FR2	Frontage on 2 sides of property
		       FR3	Frontage on 3 sides of property

		LandSlope: Slope of property

		       Gtl	Gentle slope
		       Mod	Moderate Slope	
		       Sev	Severe Slope

		Neighborhood: Physical locations within Ames city limits

		       Blmngtn	Bloomington Heights
		       Blueste	Bluestem
		       BrDale	Briardale
		       BrkSide	Brookside
		       ClearCr	Clear Creek
		       CollgCr	College Creek
		       Crawfor	Crawford
		       Edwards	Edwards
		       Gilbert	Gilbert
		       IDOTRR	Iowa DOT and Rail Road
		       MeadowV	Meadow Village
		       Mitchel	Mitchell
		       Names	North Ames
		       NoRidge	Northridge
		       NPkVill	Northpark Villa
		       NridgHt	Northridge Heights
		       NWAmes	Northwest Ames
		       OldTown	Old Town
		       SWISU	South & West of Iowa State University
		       Sawyer	Sawyer
		       SawyerW	Sawyer West
		       Somerst	Somerset
		       StoneBr	Stone Brook
		       Timber	Timberland
		       Veenker	Veenker

		Condition1: Proximity to various conditions

		       Artery	Adjacent to arterial street
		       Feedr	Adjacent to feeder street	
		       Norm	Normal	
		       RRNn	Within 200' of North-South Railroad
		       RRAn	Adjacent to North-South Railroad
		       PosN	Near positive off-site feature--park, greenbelt, etc.
		       PosA	Adjacent to postive off-site feature
		       RRNe	Within 200' of East-West Railroad
		       RRAe	Adjacent to East-West Railroad

		Condition2: Proximity to various conditions (if more than one is present)

		       Artery	Adjacent to arterial street
		       Feedr	Adjacent to feeder street	
		       Norm	Normal	
		       RRNn	Within 200' of North-South Railroad
		       RRAn	Adjacent to North-South Railroad
		       PosN	Near positive off-site feature--park, greenbelt, etc.
		       PosA	Adjacent to postive off-site feature
		       RRNe	Within 200' of East-West Railroad
		       RRAe	Adjacent to East-West Railroad

		BldgType: Type of dwelling

		       1Fam	Single-family Detached	
		       2FmCon	Two-family Conversion; originally built as one-family dwelling
		       Duplx	Duplex
		       TwnhsE	Townhouse End Unit
		       TwnhsI	Townhouse Inside Unit

		HouseStyle: Style of dwelling

		       1Story	One story
		       1.5Fin	One and one-half story: 2nd level finished
		       1.5Unf	One and one-half story: 2nd level unfinished
		       2Story	Two story
		       2.5Fin	Two and one-half story: 2nd level finished
		       2.5Unf	Two and one-half story: 2nd level unfinished
		       SFoyer	Split Foyer
		       SLvl	Split Level

		OverallQual: Rates the overall material and finish of the house

		       10	Very Excellent
		       9	Excellent
		       8	Very Good
		       7	Good
		       6	Above Average
		       5	Average
		       4	Below Average
		       3	Fair
		       2	Poor
		       1	Very Poor

		OverallCond: Rates the overall condition of the house

		       10	Very Excellent
		       9	Excellent
		       8	Very Good
		       7	Good
		       6	Above Average	
		       5	Average
		       4	Below Average	
		       3	Fair
		       2	Poor
		       1	Very Poor

		YearBuilt: Original construction date

		YearRemodAdd: Remodel date (same as construction date if no remodeling or additions)

		RoofStyle: Type of roof

		       Flat	Flat
		       Gable	Gable
		       Gambrel	Gabrel (Barn)
		       Hip	Hip
		       Mansard	Mansard
		       Shed	Shed

		RoofMatl: Roof material

		       ClyTile	Clay or Tile
		       CompShg	Standard (Composite) Shingle
		       Membran	Membrane
		       Metal	Metal
		       Roll	Roll
		       Tar&Grv	Gravel & Tar
		       WdShake	Wood Shakes
		       WdShngl	Wood Shingles

		Exterior1st: Exterior covering on house

		       AsbShng	Asbestos Shingles
		       AsphShn	Asphalt Shingles
		       BrkComm	Brick Common
		       BrkFace	Brick Face
		       CBlock	Cinder Block
		       CemntBd	Cement Board
		       HdBoard	Hard Board
		       ImStucc	Imitation Stucco
		       MetalSd	Metal Siding
		       Other	Other
		       Plywood	Plywood
		       PreCast	PreCast	
		       Stone	Stone
		       Stucco	Stucco
		       VinylSd	Vinyl Siding
		       Wd Sdng	Wood Siding
		       WdShing	Wood Shingles

		Exterior2nd: Exterior covering on house (if more than one material)

		       AsbShng	Asbestos Shingles
		       AsphShn	Asphalt Shingles
		       BrkComm	Brick Common
		       BrkFace	Brick Face
		       CBlock	Cinder Block
		       CemntBd	Cement Board
		       HdBoard	Hard Board
		       ImStucc	Imitation Stucco
		       MetalSd	Metal Siding
		       Other	Other
		       Plywood	Plywood
		       PreCast	PreCast
		       Stone	Stone
		       Stucco	Stucco
		       VinylSd	Vinyl Siding
		       Wd Sdng	Wood Siding
		       WdShing	Wood Shingles

		MasVnrType: Masonry veneer type

		       BrkCmn	Brick Common
		       BrkFace	Brick Face
		       CBlock	Cinder Block
		       None	None
		       Stone	Stone

		MasVnrArea: Masonry veneer area in square feet

		ExterQual: Evaluates the quality of the material on the exterior 

		       Ex	Excellent
		       Gd	Good
		       TA	Average/Typical
		       Fa	Fair
		       Po	Poor

		ExterCond: Evaluates the present condition of the material on the exterior

		       Ex	Excellent
		       Gd	Good
		       TA	Average/Typical
		       Fa	Fair
		       Po	Poor

		Foundation: Type of foundation

		       BrkTil	Brick & Tile
		       CBlock	Cinder Block
		       PConc	Poured Contrete	
		       Slab	Slab
		       Stone	Stone
		       Wood	Wood

		BsmtQual: Evaluates the height of the basement

		       Ex	Excellent (100+ inches)	
		       Gd	Good (90-99 inches)
		       TA	Typical (80-89 inches)
		       Fa	Fair (70-79 inches)
		       Po	Poor (<70 inches
		       NA	No Basement

		BsmtCond: Evaluates the general condition of the basement

		       Ex	Excellent
		       Gd	Good
		       TA	Typical - slight dampness allowed
		       Fa	Fair - dampness or some cracking or settling
		       Po	Poor - Severe cracking, settling, or wetness
		       NA	No Basement

		BsmtExposure: Refers to walkout or garden level walls

		       Gd	Good Exposure
		       Av	Average Exposure (split levels or foyers typically score average or above)	
		       Mn	Mimimum Exposure
		       No	No Exposure
		       NA	No Basement

		BsmtFinType1: Rating of basement finished area

		       GLQ	Good Living Quarters
		       ALQ	Average Living Quarters
		       BLQ	Below Average Living Quarters	
		       Rec	Average Rec Room
		       LwQ	Low Quality
		       Unf	Unfinshed
		       NA	No Basement

		BsmtFinSF1: Type 1 finished square feet

		BsmtFinType2: Rating of basement finished area (if multiple types)

		       GLQ	Good Living Quarters
		       ALQ	Average Living Quarters
		       BLQ	Below Average Living Quarters	
		       Rec	Average Rec Room
		       LwQ	Low Quality
		       Unf	Unfinshed
		       NA	No Basement

		BsmtFinSF2: Type 2 finished square feet

		BsmtUnfSF: Unfinished square feet of basement area

		TotalBsmtSF: Total square feet of basement area

		Heating: Type of heating

		       Floor	Floor Furnace
		       GasA	Gas forced warm air furnace
		       GasW	Gas hot water or steam heat
		       Grav	Gravity furnace	
		       OthW	Hot water or steam heat other than gas
		       Wall	Wall furnace

		HeatingQC: Heating quality and condition

		       Ex	Excellent
		       Gd	Good
		       TA	Average/Typical
		       Fa	Fair
		       Po	Poor

		CentralAir: Central air conditioning

		       N	No
		       Y	Yes

		Electrical: Electrical system

		       SBrkr	Standard Circuit Breakers & Romex
		       FuseA	Fuse Box over 60 AMP and all Romex wiring (Average)	
		       FuseF	60 AMP Fuse Box and mostly Romex wiring (Fair)
		       FuseP	60 AMP Fuse Box and mostly knob & tube wiring (poor)
		       Mix	Mixed

		1stFlrSF: First Floor square feet

		2ndFlrSF: Second floor square feet

		LowQualFinSF: Low quality finished square feet (all floors)

		GrLivArea: Above grade (ground) living area square feet

		BsmtFullBath: Basement full bathrooms

		BsmtHalfBath: Basement half bathrooms

		FullBath: Full bathrooms above grade

		HalfBath: Half baths above grade

		Bedroom: Bedrooms above grade (does NOT include basement bedrooms)

		Kitchen: Kitchens above grade

		KitchenQual: Kitchen quality

		       Ex	Excellent
		       Gd	Good
		       TA	Typical/Average
		       Fa	Fair
		       Po	Poor

data details extracted from [Kaggle](https://www.kaggle.com/competitions/home-data-for-ml-course/data) 
					  
</details>
  

# Executive Summary

### The objective:
Use the Ames, iowa dataset to identify highly correlated features (using ttest pvalues less than 0.05), and their impact on Sale Price; the application being for home owners and potential buyers to make informed decisions to improve financial outcomes when considering buying or selling.

There are two notebooks in this repo, where all coding took place, the first titled Housing_Data_cleaning_and_modeling.ipynb has all of the data cleaning analysis, model building and notes on the work described below, in a clean easy to follow order. The second notebook, Further_analysis.ipynb, features additional analysis performed on the top features collected from the first notebook, and was used as a scratchpad to generate visuals for use in presentation and furter analysis and other exploratory notes, however one must scroll down to get to the exciting parts, and note that due to late changes to the model, the code in this second notebook may run with bugs, and is included purely as a relic, for anyone curious about the code that created the images and content seen in the slides, and should be viewed solely as such.
	
### EDA and Data Cleaning

1. Outliers were identified (using stats summaries, and boxplots) and dropped; cut off points for outliers were fine tuned informed by model performance across multiple models (Statsmodel, LinearRegression, Ridge, and Lasso)
	
2. Columns were divided into two groups (Nominal/ordinal/categorical, to be assigned for One Hot Encoding, and then quantitative values (note some qualitative values remained with the the quantitatives, as little improvement was found when sorting differently for modeling to justify added engineering). 
The seperation of the two groups was essential for differentiated handling of preprocesing and streamlining the handling of null values.

3. Missing values in the categorical group were replaced with the string "none" to generate its own column to represent the missing values and hold their meaning during One Hot Encoding, while streamlining handling each column. Further analysis could be performed in the future to consider multiple reasons for missing values and wether or not their absence may have multiple/different implications against different features that would recommend use of more than one value for replacing.
	
4. Values in the quantitative group were assessed on a case by case basis, looking at mean, median, mode, as well as scatterplots, and other data on the individual homes in question, to deterine appropriate values for imputation. During this process we discovered a garage from the future (the year 2207). Further study is indicated to assess other evidence of possible time travelers in our midst, but due to project constraints the value was replaced with what seemed a reasonable guess of the original inputters intention (2007). Determining how to replace the missing values for garage proved challenging, as using the year the home was built might add to overestimates on SalePrice, but using too small a value could potentially unfairly punish those values the same, 1950 proved to be a good year to work with based on the models performance, though ultimately dropping this column also had little impact on the models accuracy. 0's were used for where a feature was missing a value likley becuase the feature itself was mising based on other data for those rows.
	
### Feature Engineering
1. The data provided some opportunities to create additional columns of data, for example there was no total bathrooms, or total sq column prior to feature engineering, both which are influential on home value and a more common point of interest to home listings and persons intersted in buying or selling, so this felt like an essnetial set of columns to create.
2. There were also a number of columns that appeared less linear against sale price, and a good opportunity to experiemnt with some polynomial feature engineering without massively slowing the models run time. Very small improvement was noted with the addition of the squared feature columns, but did no negative harm to the model to justify removing.
	
### Model selection and coefficient extraction for answering projects question

1. Statsmodel was used to collect features whose p-value were under 0.05, and the coefficients to assess the likely impact on the SalePrice in dollars per unit. Running Lasso, Ridge and Linear Regression models retuned similar "top feautres", supporting the value of these features in their impact of Sale Price.

2. The most accurate model proved to be the LassoCV model.
	
### Analysis of findings

1. The highly correlated impactful features can be divided into 5 groups, House type, neighborhood, on property features, property adjacent features (i.e. railroad tracks,parks etc.) and Sale type.

2. The findings indicate that for the home buyer looking for a good deal on a nice home should consider:
	1. Buying a property in a less desirable neighborhood. 
	2. Properties in poorer condition or of lower quality, (fixer uppers). 
	3. Split properties (split foyer, multilevel, etc.).
	4. Properties near busy, loud, and/or polluted areas. 
	5. Sale type might also provide additional savings if the buyer can find such opportunity.
	
3. For the home owner looking to imrpove their property "value" with regard to future sale price, should consider:
	1. Adding an additional bathroom or fireplace.
	2. Maintiain or improve the quality of their home. 
	3. Roof types and material also had a strong impact on sale price, and homeowners should consider upgrading to a wood shingle roof.
	4. Finishing their basement.
	5. Petitioning local government for improved neighborhood features, such as parks and natural areas.
