from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
links = {
    'Neck':'https://exrx.net/Lists/ExList/NeckWt',
    'Chest':'https://exrx.net/Lists/ExList/ChestWt',
    'Shoulder':'https://exrx.net/Lists/ExList/ShouldWt',
    'Waist':'https://exrx.net/Lists/ExList/WaistWt',
    'Arms':'https://exrx.net/Lists/ExList/ArmWt',
    'Hips':'https://exrx.net/Lists/ExList/HipsWt',
    'ForeArms':'https://exrx.net/Lists/ExList/ForeArmWt',
    'Thighs':'https://exrx.net/Lists/ExList/ThighWt',
    'Calves':'https://exrx.net/Lists/ExList/CalfWt',
    'Back':'https://exrx.net/Lists/ExList/BackWt'}

for key in links:
    driver = webdriver.Chrome()
    
    driver.get(links[key])

    time.sleep(10)
    # print(driver.page_source) # for debugging

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    links_to_save = []

    for a_tag in soup.find_all('a'):
        href = a_tag.get('href', '')
        
        if href.startswith('../../WeightExercises'):
            full_link = href.replace('../..', 'https://exrx.net')
            print(full_link)
            links_to_save.append(full_link)

    with open(f"./exercise_links/{key}_exercises.txt", "w") as f:
        for link in links_to_save:
            f.write(link + '\n')

    driver.quit()
