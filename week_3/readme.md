# DSC-DSU | Python Bootcamp 2020 | Week 3 | Facebook Bot 

## Problem Statement
1. **TAKE AS USER INPUT A FACEBOOK POST LINK AND HAVE YOUR BOT LIKE THE POST AND SHARE IT ON YOUR TIMELINE**
    - You'll need to use m.facebook.com for ease
    - For submission, like and share this post: [Facebook Post](https://www.facebook.com/Developer.../posts/2838706263116774)
    - The shared post should have the following caption(also sent through Selenium bot):"This post was shared using a bot that I learnt to create from Python Bootcamp 2020 held by DSC@DSU. #DSCDSU #DeveloperStudentClubs #DSCPakistan #Python #Bot"
    The caption is not strict, but should contain the hashtags even if you modify your message according to your flavor.
    - You'll need to submit a video recording of you running the script and showing the bot performing the liking and sharing of above mentioned post.
2. **OPTIONAL, EXTRA MARKS: MAKE THE BOT CREATED ABOVE MAKE AT LEAST 50 COMMENTS IN SUCCESSION ON THE PAGE. THESE 50 COMMENTS SHOULD BE LINES SPLIT FROM A PARAGRAPH YOU MAY WRITE ON:**
    - Your aims and goals after this bootcamp?
    - How did you like the instructors and the management?
    - What did you learn from the bootcamp?
    - Would you be willing to carry the legacy forward for a free, open source driven tech bootcamp like this one?

## Output Video
![Bot Liking, Posting And Commenting on Post](./bot.gif)

## Solution:

### Code:
Libraries used are
```python
#Selenium Imports
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
```
First from this this line sellenium driver initiate the browser from global scope.
```python
driver = webdriver.Chrome()
```
Then main function is responsible of calling all the major function. first it call the get_to() function which open facebook login page then it the login() function whcih will login to your account then the like() function go to the post then like it. then comment function comment every '.' sepreated line one by one from my_review variable then finally it call the share() function which the share the post with caption from share_caption variable  
```python
def main():
    fb = 'https://m.facebook.com/'
    post_url = 'https://m.facebook.com/DeveloperStudentClubDHASuffaUniversity/photos/a.1451042185216529/2839108256409908/'
    my_review = 'CHALLENGE ACCEPTED. I name is shahab. I am doing BSCS currently in 1st semester. course was amazing. short and concise. i will explore data science and Ml after this bootcamp and try to excel my python knowledge. instructors were great especialy tarun they exlained everything simply and in a fun i enjoyed the and waiting for another one. Other than the cuuriculum i learn exception handling problem solving skills and many more. i try to learn more about open-source and try to contribute and maybe try GSOC(need tips in this) and. yes plz make some other bootcamp love to participate'
    share_caption = "This post was shared using a bot that I learnt to create from Python Bootcamp 2020 held by DSC@DSU. #DSCDSU #DeveloperStudentClubs #DSCPakistan #Python #Bot"

    get_to(fb)
    login()
    like(post_url)
    comment(post_url,my_review)
    share(share_caption,post_url)
```
main() function only execute when this condition is true only when the script is not being imported and run from somewhere else:
```python
if __name__ == '__main__':
    main()
```
The following function first redirect the page based on the argument url:
``` python 
def get_to(url):
    driver.get(url)
```
Following function log in to facebook account.
```python
def login():
    # Enter your email password here
    email = ''
    password = input('')

    email_frm = driver.find_element_by_id("m_login_email")
    pass_frm = driver.find_element_by_id("m_login_password")
    login_btn = driver.find_element_by_css_selector('#u_0_4 button')
    
    email_frm.send_keys(email)
    pass_frm.send_keys(password)
    login_btn.click()
    
    # Cencel save password window
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div._2pii div a"))).click()
```
Following Function Like the post:
```python
def like(post_url):
    get_to(post_url)
    like_btn = driver.find_element_by_id('u_0_s')
    like_btn.click()
```
Following function is responsible for commenting on the post
```python
def comment(post_url,review):
    get_to(post_url)
    paragraphs = review.split(".")

    for i in paragraphs:
        commt_area = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.mentions textarea#composerInput")))
        commt_area.send_keys(i)

        post_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[data-sigil="touchable composer-submit"]')))
        post_btn.click()
```
Finaly the final function share the post with caption :)
```python
def share(cap,post_url):
    get_to(post_url)
    share_btn = driver.find_element_by_css_selector('a[data-sigil="share-popup"]').click()

    write_post = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.ID, "share-with-message-button"))).click()

    post_msg = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'textarea#share_msg_input')))
    post_msg.send_keys(cap)

    post_btn = driver.find_element_by_css_selector('div#modalDialogHeaderButtons button#share_submit').click()
```

## Special Thanks to:
[***Trun Kumar - Instructor***](https://github.com/sinnytk)
[***Bhawal Baloch - instructor***](https://github.com/bahawal32)

## Credits
README.md is inspired by Bilal Naseem readme template:
[Bilal Naseem](https://github.com/Bilal-Naseem)