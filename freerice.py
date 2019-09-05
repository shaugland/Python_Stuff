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

        app_id = '645be0cd'
        app_key = '2b421453b19f1f23d97cb884c1bd2264'

        language = 'en'
        word_id = ""

        new_title = title.text
        for i in range(len(new_title)):
            if new_title[i] != " ":
                word_id += new_title[i]
            else:
                break


        # print(word_id + '\n')

        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower() + '/synonyms;antonyms'

        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
        if r.status_code == 200:
            data = r.json()


            synonyms = []
            for i in data['results'][0]['lexicalEntries']:
                something = i['entries']
                for j in something:
                    somethingElse = j['senses']
                    for s in somethingElse:
                        almost = s['synonyms']
                        for ii in almost:
                            last = ii['text']
                            # print(last)
                            synonyms.append(last)

            # print('\n')
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
