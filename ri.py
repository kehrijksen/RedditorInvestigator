#!/bin/python3

import praw
import re
import argparse
import os

from dotenv import load_dotenv 
from collections import OrderedDict
from operator import itemgetter

def parse_args():
    parser = argparse.ArgumentParser(description="Get insights in posts made by a redditor")
    parser.add_argument(
        '-u', '--username',
        help='username of the redditor'
    )
    parser.add_argument(
        '-o', '--output-file',
        help='write the results into a text file'
    )
    return parser.parse_args()

# Go to https://www.reddit.com/prefs/apps
# Fill in a random name and http://127.0.0.1:1337
# Paste vars into .env
load_dotenv()
reddit = praw.Reddit(
    client_id=os.environ.get("CLIENT_ID"),
    client_secret=os.environ.get("CLIENT_SECRET"),
    user_agent="RedditorInspector"
)

# TODO 
DELIMITER_REGEX = ''

def get_posts(username: str):
  words = {}
  for submission in reddit.redditor(username).submissions.new(limit=None):
    # Search title
    for word in submission.title.lower().split():
      words[word] = words.get(word, 0) + 1
	# Search body
    for word in submission.selftext.lower().split():
      words[word] = words.get(word, 0) + 1
  return words
	
def get_comments(username: str):
  words = {}
  for comment in reddit.redditor(username).comments.new(limit=None):
    for word in comment.body.lower().split():
      words[word] = words.get(word, 0) + 1
  return words

def lookup_redditor(username: str):
  print('Looking up user:', username)
  
  # Get all words from submissions and comments
  words = get_posts(username=username)
  words.update(get_comments(username=username))
  sorted_words = OrderedDict(sorted(words.items(), key=itemgetter(1), reverse=True))
  return sorted_words


def write_to_file(filename: str, text: str):
  with open(filename, "w", encoding="utf-8") as file:
    file.write(text)
    print("Wrote to file!")


def main():
  args = parse_args()
  if not args.username:
    parser.error('No username given')
  
  result = lookup_redditor(username=args.username)
  if args.output_file:
    write_to_file(filename=args.output_file, text=str(result))
  else:
    print(result)


if __name__ == '__main__':
  main()
	
