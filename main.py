import praw


client_id=""
client_secret=""
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent="Tutorial user agent",
)

subreddit='wallstreetbets'
for submission in reddit.subreddit(subreddit).hot(limit=10):
    print("Submission Title:", submission.title, "\nSubmission score:",submission.score,"\nSubmission url:",submission.url)
    print(submission.score)
    print(submission.url)
    print("----------")


for submission in reddit.subreddit(subreddit).top(time_filter="all",limit=10):
    print("Submission Title:", submission.title, "\nSubmission score:",submission.score,"\nSubmission url:",submission.url)
    print(submission.score)
    print(submission.url)
    print("----------")
