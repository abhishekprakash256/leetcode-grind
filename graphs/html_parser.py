import requests
from bs4 import BeautifulSoup

# List of dummy URLs
allBaseURLs = ["https://example.com/page1", "https://example.com/page2"]

allFeaturesURLs = []

action_key_links = []

def find_div_by_partial_id(soup, keyword):
   
    for div in soup.find_all('div', id=True):
        
        if keyword.lower() in div['id'].lower():
            return div

    return None



def find_action_div(soup):

    return soup.find('div', id="action")


#first part 
# Go to each page and collect feature links
for url in allBaseURLs:

    url_data = requests.get(url)

    page_data = BeautifulSoup(url_data.text, 'html.parser')


    feature_div = find_div_by_partial_id(page_data, 'feature')

    if feature_div:

        all_feature_anchors = feature_div.find_all('a', href=True)

        for anchor in all_feature_anchors:

            allFeaturesURLs.append(anchor['href'])

# Print all collected feature URLs
for feature_url in allFeaturesURLs:
    print(feature_url)



#second part 

for link in allFeaturesURLs :

    link_data = requests.get(link)

    link_data_parse = BeautifulSoup(link_data.text, 'html.parser')

    action_div = find_action_div(link_data_parse)

    if action_div:
            
        # get the link 
        action_links = action_div.find_all('a', href=True)
        
        for action_key_link in action_links :

            if "action_KEY" in link["href"] :

                action_key_links.append(action_key_link)

                print(link)

                print(link['href'])
















    






