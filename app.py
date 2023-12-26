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
    post_data = [
        {
         "name" : "jignect-technologies",
         "postUrl" : "https://www.linkedin.com/posts/jignect-technologies_jignecttechnologies-lifeatjignect-jignectadventure-activity-7140621156784549888-FtPm?utm_source=share&utm_medium=member_desktop"
        },
        {
         "name" : "nikunj-patel",
         "postUrl" : "https://www.linkedin.com/posts/nikunj-patel-68b292150_jignecttechnologies-lifeatjignect-jignectadventure-activity-7140740425388118016-JYt2?utm_source=share&utm_medium=member_desktop"
        },
        {
         "name" : "ravi-lalwani",
         "postUrl" : "https://www.linkedin.com/posts/ravi-lalwani-4907991a4_jawai-rajasthan-leopard-activity-7141250234470367232-Lw9e?utm_source=share&utm_medium=member_android"
        },
        {
         "name" : "rajan-patel",
         "postUrl" : "https://www.linkedin.com/posts/rajan-patel-361b4a117_hey-connection-like-repost-share-like-activity-7143477583454654464-xqD6?utm_source=share&utm_medium=member_desktop"
        },
        {
         "name" : "nehal-lunagariya",
         "postUrl" : "https://www.linkedin.com/posts/nehal-lunagariya-229683179_jignecttechnologies-lifeatjignect-jignectadventure-activity-7141449662976237568-Rmsx?utm_source=share&utm_medium=member_desktop"
        },
        {
         "name" : "raj-lunagariya",
         "postUrl" : "https://www.linkedin.com/posts/raj-lunagariya-67631b284_im-happy-to-share-that-i-am-starting-a-new-activity-7115165744950108160--Nlx?utm_source=share&utm_medium=member_desktop"
        },
        {
         "name" : "hely-patel",
         "postUrl" : "https://www.linkedin.com/posts/hely-patel-634528228_jawaileopardsafari-natureunleashed-leopardencounter-activity-7141119418192887809-IRYm?utm_source=share&utm_medium=member_desktop"
        },
        {
         "name" : "raj-vivek",
         "postUrl" : "https://www.linkedin.com/posts/raj-vivek-878395246_lifeatjignect-jignectadventure-rajasthanwonders-activity-7141432688577601537-4dKK?utm_source=share&utm_medium=member_android"
        }
        
        # "https://www.linkedin.com/posts/nikunj-patel-68b292150_jignecttechnologies-lifeatjignect-jignectadventure-activity-7140740425388118016-JYt2?utm_source=share&utm_medium=member_desktop",
        # "https://www.linkedin.com/posts/rajan-patel-361b4a117_hey-connection-like-repost-share-like-activity-7143477583454654464-xqD6?utm_source=share&utm_medium=member_desktop",
        # "https://www.linkedin.com/posts/drashti-mehta-199093209_ketalystcertification-continuouslearning-activity-7140619174761906176-Z974?utm_source=share&utm_medium=member_desktop"
        # "https://www.linkedin.com/posts/activity-7141449662976237568-Qpdv?utm_source=share&utm_medium=member_desktop",
    ]

    # OLD
    # like_counts = [get_linkedin_post_likes(url) for url in post_urls]
    # return render_template('index.html', post_urls=post_urls, like_counts=like_counts,zip = zip)


    like_counts = [get_linkedin_post_likes(data["postUrl"]) for data in post_data]
    comment_counts = [get_linkedin_post_comments(data["postUrl"]) for data in post_data]
    return render_template('index.html', post_data=post_data, like_counts=like_counts,comment_counts=comment_counts,zip = zip)

if __name__ == '__main__':
    app.run(debug=True)




    # "https://www.linkedin.com/posts/your_username_your_post_id1",
        # "https://www.linkedin.com/posts/your_username_your_post_id2",
        # "https://www.linkedin.com/posts/nikunj-patel-68b292150_jignecttechnologies-lifeatjignect-jignectadventure-activity-7140740425388118016-JYt2?utm_source=share&utm_medium=member_desktop"
        # Add more post URLs as needed
