import praw
import pandas as pd
 
reddit_read_only = praw.Reddit(client_id="5Aw8MgAsTghDiquR2eqBqw",       
                               client_secret="LA6U3KB-kfeDJ1F8MExnzIn4PpJ-ZA",     
                               user_agent="SubScraper")      
 
 
subreddit = reddit_read_only.subreddit("redditdev")
 
print("Display Name:", subreddit.display_name)
 
print("Title:", subreddit.title)
 
print("Description:", subreddit.description)