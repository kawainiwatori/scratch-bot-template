import scratchattach as sa
import time
import random
from collections import deque

# Replace username and password with your credentials
try:
    session = sa.login("username", "password")
except Exception as e:
    print(f"Error logging in: {e}")
    exit()

# Replace studioid with your studio ID
try:
    studio = session.connect_studio("studioid")
except Exception as e:
    print(f"Error connecting to studio: {e}")
    exit()

comment_queue = deque()
replied_comments = set()
last_reply_time = 0

# Define your commands here
commands = {
    "/example1": lambda: f"this is an example command (RNTAS: {random.randint(1000, 9999)})",
}

while True:
    try:
        newest_comment_as_list = studio.comments(limit=1, offset=0)
        newest_comment = newest_comment_as_list[0]
        comment = studio.comment_by_id(newest_comment.id)
    except Exception as e:
        print(f"Error retrieving comments: {e}")
        time.sleep(1)
        continue
    
    if comment.content in commands and comment.id not in replied_comments:
        comment_queue.append((comment, commands[comment.content]()))
        replied_comments.add(comment.id)
    
    current_time = time.time()
    if (current_time - last_reply_time) >= 30 and comment_queue:
        try:
            comment_to_reply, response = comment_queue.popleft()
            comment_to_reply.reply(response)
        except Exception as e:
            print(f"Error replying to comment: {e}")
        
        last_reply_time = current_time
    
    time.sleep(1)
