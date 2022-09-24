import instaloader
from itertools import takewhile, dropwhile
import os

def get_instagram_posts(user_login, password, username : list, startdate, enddate, initial_path, save_folder='data'):
   # Create an instaloader object with parameters
   L = instaloader.Instaloader(download_pictures = False, download_videos = False, download_comments= False, compress_json = False)
   
   # Log in with the instaloader object
   L.login(user_login , password)
   # Search the instagram profile
   profile = instaloader.Profile.from_username(L.context, username)
   # Scrape the posts
   posts = profile.get_posts()
   os.chdir(os.path.join(initial_path, save_folder))
   for post in takewhile(lambda p: p.date > startdate, dropwhile(      lambda p : p.date > enddate, posts)): 
    print(post.date)
    L.download_post(post, target = profile.username)
   os.chdir(initial_path)