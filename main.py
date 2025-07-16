

from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import re
import numpy as np

import re

def extraire_nombres(chaine):
    return ''.join(c for c in chaine if c.isdigit())
objet_json ={}
 
def replace(str,id,cursser):
    pattern = r"aweme_id=\d+"
    pattern2 = r"cursor=\d+"
    search_result = re.findall(pattern, str) , re.findall(pattern2,str)
    return str.replace(search_result[0][0],f"aweme_id={id}").replace(search_result[1][0],f"cursor={cursser}")

def req(stred,url,cursser):
    POST_ID = extraire_nombres(url.split('/')[-1])
    driver = webdriver.Chrome()
    stred = replace(stred,POST_ID,cursser)
    try:
        driver.get(stred)
        texte = None
        try:
            body_content = driver.find_element(By.TAG_NAME, "pre").get_attribute('innerHTML')
            texte = str(body_content)
        except Exception as e:
            pass
        
        if texte != None:
            objet_json = json.loads(texte)
            return objet_json

    finally:
         driver.quit()
         
        


def parser(data):
    comment = np.array([])
    if data:
        coment = data['comments']
        for cm in coment:
            comment = np.append(comment,cm['text'])
            print(comment)
            print('#' * 100)
            #comment = np.append(comment,cm['reply_comment'])
        return data,comment


#GET_Comments(Network API, Video URL)

#To Get Network API : 
# 1 Inspect

# 2 Go to the Network tab

# 3 Filter by: /api/comment

# 4 From the Headers tab, copy the Request URL
def GET_Comments(stre,url):
    comment = np.array([])
    cursser=0
    while True:
      
      data = req(stre,url,cursser)
     
      if data: 
           same_data, comment = parser(data)[0],np.append(comment,parser(data)[1])
           cursser = same_data['cursor']
           if same_data['has_more']==1:
               print(data['has_more'])
               print(cursser)
           else:
               break
      else:
       break
    return comment


#Example

GET_Comments('https://www.tiktok.com/api/comment/list/?WebIdLastTime=1752700768&aid=1988&app_language=ja-JP&app_name=tiktok_web&aweme_id=7525947256504208662&browser_language=fr&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F138.0.0.0%20Safari%2F537.36%20Edg%2F138.0.0.0&channel=tiktok_web&cookie_enabled=true&count=20&current_region=JP&cursor=0&data_collection_enabled=false&device_id=7527792443455817221&device_platform=web_pc&enter_from=tiktok_web&focus_state=true&fromWeb=1&from_page=video&history_len=3&is_fullscreen=false&is_non_personalized=false&is_page_visible=true&odinId=7527792334449886213&os=windows&priority_region=&referer=https%3A%2F%2Fwww.bing.com%2F&region=DZ&root_referer=https%3A%2F%2Fwww.bing.com%2F&screen_height=768&screen_width=1366&tz_name=Europe%2FParis&user_is_login=false&verifyFp=verify_md6g1em1_UhGJ5MD5_GNlb_4EuG_8IVI_P0uGXw18WP6R&webcast_language=fr&msToken=dPHWGxDkCxAFkzuBfzHHJMa8oXDQD2jzyXt1rsm8HNNWFtzN3vDsGk4lqUGw68KxYFVq2z2ICWvwU6RO-GsX6__wgGRP4ykI9H9LJRZBHNvxqu-h2kWs2Sda2YUm7gExAGqK4pcP--KqHqPdE3pK8BWS&X-Bogus=DFSzswVu0giANGChCSrWWuhPmk3n&X-Gnarly=MHC5ZqUBBWtEFtL00yhbHaXkzpT-UVLv8IKsBAU3y5wdN698xGSGkMIsxFoVSq18NUA1lnQ-5GhJcIBzWqVqk-m4uxy7VKC9gZ3cOaa3pceWBeU1T8kWtKKOjLGNaMae7f4eWLj1PMR2ckTJAsi2Vx8kUWvKh0f/CBRbzVCN5AuRED/MK8nzbelg5gv9pvVICUrS9s/B0BkjdN/eK/eGwtQ09rDBNSZcSCntOy5FTzfPm-uyeKSMa3CxOKo7IvQPKZIsYykMRLgX4OH8NJDp-d9t0Cq8N93vZf/Sc0yBtsmw','https://www.tiktok.com/@caf_online/video/7524732448144461064')
