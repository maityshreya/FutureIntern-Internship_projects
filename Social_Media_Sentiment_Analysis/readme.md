# Description
The Social Media Sentiments Analysis Dataset captures a vibrant tapestry of emotions, trends, and interactions across various social media platforms. This dataset provides a snapshot of user-generated content, encompassing text, timestamps, hashtags, countries, likes, and retweets. Each entry unveils unique stories—moments of surprise, excitement, admiration, thrill, contentment, and more—shared by individuals worldwide.

# DataSet
Columns :

Text: Text content of the post.
Sentiment: Sentiment of the post (positive, negative, or neutral).
Timestamp: Date and time of the post.
User: Username of the poster.
Platform: Social media platform where the post was made (Twitter, Instagram, Facebook).
Hashtags: Hashtags used in the post.
Retweets: Number of retweets for the post.
Likes: Number of likes for the post.
Country: Country of origin for the poster.
Year: Year in which the post was made.
Month: Month in which the post was made.
Day: Day of the month on which the post was made.
Hour: Hour of the day at which the post was made.

# Project Structure
The project is structured as follows:

- `app.py`: Flask web application for serving predictions.
- `model/`: Directory containing trained model and preprocessing objects.
- `dataset/`: Directory containing the dataset used for training.

# Technologies Used
- Python
- Flask
- Pandas
- Numpy
- matplotlib
- scikit-learn
