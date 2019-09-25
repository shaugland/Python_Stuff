from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import requests
import time

driver = webdriver.Firefox()
driver.get("http://beta.freerice.com")

input("Are you ready? Press enter when ready")

times = 0
while times < 500:
    try:
        time.sleep(4)
        title = driver.find_element_by_class_name("card-title")
        options = driver.find_elements_by_class_name("card-button")

        # I have free version anyways of oxfords api
        # but you don't get any of my keys sorry :(
        app_id = ''
        app_key = ''

        language = 'en'
        word_id = ""

        new_title = title.text
        for i in range(len(new_title)):
            if new_title[i] != " ":
                word_id += new_title[i]
            else:
                break


        # print(word_id + '\n')


        # will receive our data from oxiford dictionaries api to get synonyms from it
        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower() + '/synonyms;antonyms'

        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
        if r.status_code == 200:
            data = r.json()


            # Gets every synonym to the word that the website wants to know what its word is similar to (hence synonym)
            synonyms = []
            for i in data['results'][0]['lexicalEntries']:
                entries = i['entries']
                for j in entries:
                    senses = j['senses']
                    for s in senses:
                        almost = s['synonyms']
                        for ii in almost:
                            last = ii['text']
                            # print(last)
                            synonyms.append(last)

            # print('\n')

            # Sees if there is a button on the page that has a word that is the same as the synonym
            found = False
            for text in synonyms:
                for option in options:
                    if text == option.text:
                        print("found")
                        found = True
                        option.click()
                        break
                if found == True:
                    break

            if found != True:
                # Since sometimes it doesn't line up with anything in the dictionary, we just click on the first element and hope for the best
                options[0].click()

            # print('\n')
            print(times)
            times += 1
        else:
            print("Word not found")
            options[0].click()
            continue

    except:
        time.sleep(1)
