import requests
import csv


# ---------------------------------------
# Function 1: Fetch and print post titles
# ---------------------------------------
def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print status code
    print(f"Status Code: {response.status_code}")

    # If successful, parse and print titles
    if response.status_code == 200:
        posts = response.json()

        # Print titles of all posts
        for post in posts:
            print(post["title"])
    else:
        print("Failed to fetch posts.")


# -------------------------------------------------
# Function 2: Fetch posts and save them into a CSV
# -------------------------------------------------
def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Prepare structured list of dictionaries
        structured_posts = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in posts
        ]

        # Write to CSV using DictWriter
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_posts)

        print("posts.csv has been created successfully.")
    else:
        print("Failed to fetch posts.")
