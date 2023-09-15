import requests
from bs4 import BeautifulSoup

cat_url = "https://pixabay.com/images/search/cat/"

def scrape_cat_images(cat_url):


    response = requests.get(cat_url)
    soup = BeautifulSoup(response.content, "html.parser")

    image_urls = []
    for img in soup.find_all("img"):
        image_urls.append(img["src"])

    return image_urls

if __name__ == "__main__":
    image_urls = scrape_cat_images(cat_url)

    for image_url in image_urls:
        image_response = requests.get(image_url)
        with open(f"cat_{image_urls.index(image_url)}.jpg", "wb") as f:
            f.write(image_response.content)

