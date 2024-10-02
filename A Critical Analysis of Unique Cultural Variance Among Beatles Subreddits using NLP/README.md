# A Critical Analysis of Unique Cultural Variance Among Beatles Subreddits: 
## Rad finds a home for his memes 

Reddit currently has three Beatles themed subreddits for discussion of all matters related to famed 1960s rock quad. Lets explore.

# Data Dictionary

All data used is taken from Reddit using PRAW

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**created_utc**|*float*|created utc|
|**title**|*string*|title of reddit post|
|**self_text**|*string*|content of reddit post (not including title)|
|**subreddit**|*string*|name of subreddit post belongs to|
|**score**|*int*|score/popularity of post by upvotes|
|**author**|*string*|author of post by reddit username|
|**comments**|*praw comments forest*|object containing all comments on given post|
|**words**|*string*|title and post combined to one string object|
|**comments_total**|*int*|total number of comments for given post|
|**comments_list**|*string*|comments object as list for extraction|
|**comment_1,comment_0, ... , comment_10**|*string*|numbered ten comments from each post|
|**words_comments**|*string*|top ten comments concatenated to single string object|
|**all_words**|*string*|title, post, and top ten comments concatenated to single string object|


# Executive Summary

This project is intended to differentiate between the three Beatles subreddits, utilizing various regression and classifier models and as well as CountVectorizer, TF-IDF Vectorizer, and Lemmatization to analyse the texts contained with the posts and comments of each sub.
Do different groups discuss the Beatles differently? do some groups have more bullies? Do they favor different Beatles? and most importantly, which subreddit would make the most ideal home for Rads highly specialized Beatles themed memes, and can the data from the models be used to leverage high impact memes and reddit posts.

the analysis can be found in the beatlesredditdataanalysis.ipynb file, the original scraping and engineering of the data here: scrapingdatawithPRAW.ipynb and the models here: BeatlesRedditModels.ipynb
