from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()

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
    
def get_to(url):
    driver.get(url)

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

def like(post_url):
    get_to(post_url)
    like_btn = driver.find_element_by_id('u_0_s')
    like_btn.click()

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

def share(cap,post_url):
    get_to(post_url)
    share_btn = driver.find_element_by_css_selector('a[data-sigil="share-popup"]').click()

    write_post = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.ID, "share-with-message-button"))).click()

    post_msg = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'textarea#share_msg_input')))
    post_msg.send_keys(cap)

    post_btn = driver.find_element_by_css_selector('div#modalDialogHeaderButtons button#share_submit').click()


if __name__ == '__main__':
    main()