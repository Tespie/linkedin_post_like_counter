from flask import Flask, render_template
import requests
import json
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_linkedin_post_likes(post_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(post_url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        page_title = soup.find('h1')

        like_count_element = soup.find('span', {'data-test-id' :'social-actions__reaction-count'})

        if(page_title.text.__contains__("Post")):
            # Find the element containing the like count
            if like_count_element:
                like_count = like_count_element.text
                print(f"Like Count: {like_count}")
            else:
                like_count = "0"

        else:
            like_count = "Maybe Private Account ⚠️ OR\n Post Deleted 🥸"

        # WORKING
        return like_count

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    
def get_linkedin_post_comments(post_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(post_url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        page_title = soup.find('h1')

        comment_count_element = soup.find('a', {'data-test-id' :'social-actions__comments'})

        if(page_title.text.__contains__("Post")):
            # Find the element containing the like count
            if comment_count_element:
                comment_count = comment_count_element.text
                print(f"Comment Count: {comment_count}")
            else:
                comment_count = "0 Comment"

        else:
            comment_count = "Maybe Private Account ⚠️ OR\n Post Deleted 🥸"

        # WORKING
        return comment_count

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


@app.route('/')
def index():
    file_path = "assets\\staticData\\post_data.json"
    with open(file_path, 'r', encoding='utf-8') as json_file:
        post_data = json.load(json_file)

    like_counts = [get_linkedin_post_likes(data["postUrl"]) for data in post_data]
    comment_counts = [get_linkedin_post_comments(data["postUrl"]) for data in post_data]
    return render_template('index.html', post_data=post_data, like_counts=like_counts,comment_counts=comment_counts,zip = zip)

if __name__ == '__main__':
    app.run(debug=True)