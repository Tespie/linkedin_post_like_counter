from flask import Flask, render_template
import requests
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
        like_element = soup.find('button', {'aria-label': 'Like'})
        like_count = like_element.find('span', {'class': 'v-align-middle'}).text

        return like_count.strip()
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

@app.route('/')
def index():
    post_urls = [
        "https://www.linkedin.com/posts/your_username_your_post_id1",
        "https://www.linkedin.com/posts/your_username_your_post_id2",
        # Add more post URLs as needed
    ]

    like_counts = [get_linkedin_post_likes(url) for url in post_urls]

    return render_template('index.html', post_urls=post_urls, like_counts=like_counts)

if __name__ == '__main__':
    app.run(debug=True)
