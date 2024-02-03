import praw

reddit =praw.Reddit(
    client_id ='je2YPZNc5P9C-ha4GnYF8g',
    client_secret = 'quejvpgbawWuI5TunnVR1E6Ehg37WA',
    user_agent ='Personal by u/Few-Yogurtcloset4571',
    # username="Few-Yogurtcloset4571",
    # password="Gold@Hunt",
)

subreddit = reddit.subreddit("dataengineeringjobs")

top_posts = subreddit.top(limit=10)

new_posts = subreddit.new(limit=10)

for post in top_posts:
    print("Title -", post.title)
    print("ID -", post.id)
    print("Author - ", post.author)
    print("URL -", post.url)
    print("Comment Count", post.num_comments)
    print("\n")


post = reddit.submission(id="i8au2i")

comments = post.comments

for comment in comments[:5]:
    print("Printing comment...")
    print("comment.body- ",comment.body)
    print("Author - ",comment.author)
    print('\n')