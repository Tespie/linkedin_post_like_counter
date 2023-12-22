from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_linkedin_post_likes(post_url):
    # print('post_url =',post_url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(post_url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        # print("soup =",soup)
        # like_element = soup.find('button', {'aria-label': 'Like'})
        # like_element = soup.find('button', {'class': 'social-details-social-counts__social-proof-fallback-number'})

        # gives count
        # like_element = soup.find('span', {'class' :'social-details-social-counts__social-proof-fallback-number'}) 

        # gives span having count vala span
        # like_element = soup.find('span', {'class' :'social-details-social-counts__social-proof-container'}) 


# SAMPLE
#  <span class="font-normal ml-0.5" data-test-id="social-actions__reaction-count"> 118 </span>


        # soup.find('p', attrs={"aria-hidden": "true"})
        # soup.find('p', attrs={"class": "class_name", "id": "id_name"})


        # print("like_elementt =",like_element)
        # like_count = like_element.find('span', {'class': 'v-align-middle'}).text

        # return like_count.strip()
        # return '5000'


        # return like_element
        # return soup

        # gives count from the parser - WORKING
        like_count = soup.find('span', {'class' :'font-normal ml-0.5'}).text 

        # WORKING
        return like_count

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

@app.route('/')
def index():
    post_data = [
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
    return render_template('index.html', post_data=post_data, like_counts=like_counts,zip = zip)
    

if __name__ == '__main__':
    app.run(debug=True)




    # "https://www.linkedin.com/posts/your_username_your_post_id1",
        # "https://www.linkedin.com/posts/your_username_your_post_id2",
        # "https://www.linkedin.com/posts/nikunj-patel-68b292150_jignecttechnologies-lifeatjignect-jignectadventure-activity-7140740425388118016-JYt2?utm_source=share&utm_medium=member_desktop"
        # Add more post URLs as needed
