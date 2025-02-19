import praw
import pandas as pd
from praw.models import MoreComments

reddit_read_only = praw.Reddit(client_id="client id",       
                               client_secret="secret key",     
                               user_agent="SubScraper")      
 
 
subreddit = reddit_read_only.subreddit("redditdev")
 
print("Display Name:", subreddit.display_name)
 
print("Title:", subreddit.title)
 
print("Description:", subreddit.description)

#printing top 5 posts in subreddit
subreddit = reddit_read_only.subreddit("Python")

for post in subreddit.hot(limit=5):
    print(post.title)
    print()

# scraping the top posts of the current month
posts = subreddit.top("month")
 
posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }
 
for post in posts:
    posts_dict["Title"].append(post.title)
    posts_dict["Post Text"].append(post.selftext)
    posts_dict["ID"].append(post.id)
    posts_dict["Score"].append(post.score)
    posts_dict["Total Comments"].append(post.num_comments)
    posts_dict["Post URL"].append(post.url)
 
top_posts = pd.DataFrame(posts_dict)
top_posts


#scrape data from posts
post_comments = []
 
for comment in submission.comments:
    if type(comment) == MoreComments:
        continue
 
    post_comments.append(comment.body)
 
# creating a dataframe
comments_df = pd.DataFrame(post_comments, columns=['comment'])
comments_df