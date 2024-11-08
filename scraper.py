import praw
import pandas as pd
 
reddit_read_only = praw.Reddit(client_id="client id",       
                               client_secret="secret key",     
                               user_agent="SubScraper")      
 
 
subreddit = reddit_read_only.subreddit("redditdev")
 
print("Display Name:", subreddit.display_name)
 
print("Title:", subreddit.title)
 
print("Description:", subreddit.description)