import time
from selenium import webdriver

def findKeyword(driver, keyword)->bool:
    print(driver.page_source)
    return keyword.lower() in driver.page_source

def main():
    # Initialize browser
    driver = webdriver.Chrome()

    # Navigate to your website
    driver.get("http://localhost:3000/")

    reward_time = 10
    total_reward_time = 0
    keyword = "student"
    if findKeyword(driver, keyword):
        total_reward_time += reward_time
        
    driver.quit()
    print("Presence Time:", total_reward_time)

if __name__ == "__main__":
    main()