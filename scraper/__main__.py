import os
import sys
import argparse
import pandas as pd
from twitter_scraper import Twitter_Scraper

try:
    from dotenv import load_dotenv

    print("Loading .env file")
    load_dotenv()
    print("Loaded .env file\n")
except Exception as e:
    print(f"Error loading .env file: {e}")
    sys.exit(1)

def main():
    try:
        parser = argparse.ArgumentParser(
            add_help=True,
            usage="python scraper [option] ... [arg] ...",
            description="Twitter Scraper is a tool that allows you to scrape tweets from twitter without using Twitter's API.",
        )

        print("Parser complete")

        try:
            parser.add_argument(
                '--user',
                type=str,
                default=os.getenv("TWITTER_USERNAME")
            )

            parser.add_argument(
                '--password',
                type=str,
                default=os.getenv("TWITTER_PASSWORD")
            )
            
            parser.add_argument(
                '--scrolls',
                type=int,
                default=os.getenv("SCROLL_AMOUNT")
            )

            parser.add_argument(
                '--url',
                type=str,
                default=os.getenv("URL")
            )

            parser.add_argument(
                '--headless',
                type=str,
                default=os.getenv("HEADLESS")
            )

            print("Environment variables checked")

        except Exception as e:
            print(e)
            sys.exit(1)

    except Exception as e:
        print(e)
        sys.exit(1)
    
    args = parser.parse_args()
    tweet_args = []

    if args.user is not None:
        tweet_args.append(args.user)
    if args.password is not None:
        tweet_args.append(args.password)
    if args.scrolls is not None:
        tweet_args.append(args.scrolls)
    if args.url is not None:
        tweet_args.append(args.url)
    if args.headless is not None:
        tweet_args.append(args.headless)
    
    print("args added")

    scraper = Twitter_Scraper(password=args.password, username=args.user, tweet_url=args.url, headlessState=args.headless, mail=None)
    scraper.login()
    print("login complete")
    replies = scraper.scrape_replies_to_tweet(tweet_url=args.url, scrolls=10)
    for reply in replies:
        print(reply)
    
    saveToCSV(replies)

    scraper.driver.quit()

def saveToCSV(data):
    print("saving data to csv file...")

    dataframe = pd.DataFrame(data)
    dataframe.to_csv('replies.csv', index=False)
    print("data saved.")

if __name__ == "__main__":
    main()