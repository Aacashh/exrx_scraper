from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import os
import requests

txt_files = {
    # 'Neck':'./exercise_links/Neck_exercises.txt',
    # 'Chest':'./exercise_links/Chest_exercises.txt',
    'Shoulder':'./exercise_links/Shoulder_exercises.txt',
    'Waist':'./exercise_links/Waist_exercises.txt',
    'Arms':'./exercise_links/Arms_exercises.txt',
    'Hips':'./exercise_links/Hips_exercises.txt',
    'ForeArms':'./exercise_links/ForeArms_exercises.txt',
    'Thighs':'./exercise_links/Thighs_exercises.txt',
    'Calves':'./exercise_links/Calves_exercises.txt',
    'Back':'./exercise_links/Back_exercises.txt'}

for key in txt_files:
    
    driver = webdriver.Chrome()

    if not os.path.exists(f'./exercise_gifs/{key}_gifs'):
        os.makedirs(f'./exercise_gifs/{key}_gifs')

    with open(f'./exercise_dataset/{key}_exercises.csv', 'w', newline='') as csvfile:
        fieldnames = ['Exercise Name', 'Link', 'Instructions', 'Comments', 'Target Muscles', 'Thumbnail GIF'] # 'Synergists', 'Stabilisers', 'Antagonist Stabilisers'
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        with open(txt_files[key], 'r') as txtfile:
            for link in txtfile:
                link = link.strip()
                
                driver.get(link)
        
                time.sleep(5)
                soup = BeautifulSoup(driver.page_source, 'html.parser')

                exercise_data = {}
                
                exercise_data['Exercise Name'] = soup.find('h1', {'class': 'page-title'}).text.strip()
                exercise_data['Link'] = link
                
                # for i, col_sm_6 in enumerate(soup.find_all('div', {'class': 'col-sm-6'})):
                #     if i == 0:  # First 'col-sm-6'
                exercise_data['Instructions'] = soup.find('strong', text='Preparation').find_next('p').text
                exercise_data['Instructions'] += ' ' + soup.find('strong', text='Execution').find_next('p').text
                    # elif i == 1:  # Second 'col-sm-6'
                exercise_data['Comments'] = soup.find('h2', text='Comments').find_next('p').text
                exercise_data['Target Muscles'] = [li.get_text(strip=True) for li in soup.find('strong', text='Target').find_next('ul').find_all('li')]
                # exercise_data['Synergists'] = [li.get_text(strip=True) for li in col_sm_6.find('strong', text='Synergists').find_next('ul').find_all('li')]
                # exercise_data['Stabilisers'] = [li.get_text(strip=True) for li in col_sm_6.find('strong', text='Stabilizers').find_next('ul').find_all('li')]
                # antagonist_stabilisers_tag = col_sm_6.find('strong', text='Antagonist Stabilizers')
                # exercise_data['Antagonist Stabilisers'] = [li.get_text(strip=True) for li in antagonist_stabilisers_tag.find_next('ul').find_all('li')] if antagonist_stabilisers_tag else 'None'

                file_url = soup.find('meta', {'name': 'thumbnail'})['content']
                exercise_data['Thumbnail'] = file_url

                # Fetch file data and its type
                response = requests.get(file_url)
                file_data = response.content
                file_type = response.headers['content-type'].split('/')[-1]

                # Determine the correct extension
                if file_type == 'gif':
                    extension = '.gif'
                elif file_type == 'png':
                    extension = '.png'
                elif file_type == 'jpg' or file_type == 'jpeg':
                    extension = '.jpg'
                else:
                    extension = '.unknown'

                # Save the file
                with open(f'./exercise_gifs/{key}_gifs/{exercise_data["Exercise Name"]}{extension}', 'wb') as file:
                    file.write(file_data)

                # Write the scraped data to the CSV file
                writer.writerow(exercise_data)
                print(f"Scraped data and downloaded thumbnail for {link}")

    driver.quit()
