from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.follower = []
    def login(self):
        self.browser.get("https://github.com/login")

        time.sleep(2)
        self.browser.find_element(by="xpath", value="//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element(by="xpath", value="//*[@id='password']").send_keys(self.password)
        self.browser.find_element(by="xpath", value="//*[@id='login']/div[4]/form/div/input[11]").click()
        time.sleep(2)
    
    def loadFlowwers(self):
        z = 0
        follower = self.browser.find_elements(By.CSS_SELECTOR,".d-table.table-fixed")
        for i in follower:
            x = i.find_element(By.CSS_SELECTOR, ".Link--secondary").text
            self.follower.append(x)
            z += 1
        return z
  

    def followers(self):
        url = "https://github.com/"+self.username+"?tab=followers"
        self.browser.get(url)
        time.sleep(2)
        z = self.loadFlowwers()
        y = self.browser.find_element(By.XPATH,"/html/body/div[1]/div[6]/main/div[2]/div/div[1]/div/div[2]/div[3]/div[2]/div[3]/div/a[1]/span").text
        if (int(y) > 50):
            while True:
                if z == 50:
                    links = self.browser.find_element(By.XPATH,"//*[@id='user-profile-frame']/div/div[51]/div").find_elements(By.TAG_NAME, "a")

                    if (len(links) == 1):
                        if links[0].text == "Next":
                            links[0].click()
                            time.sleep(2)
                            z = self.loadFlowwers()
                        else:
                            break
                    else:
                        for lik in links:
                            if lik.text == "Next":
                                lik.click()
                                time.sleep(4)
                                self.loadFlowwers()
                            else:
                                continue
                        else:
                            break
                else:
                    break

username = input("username: ")
password = input("password: ")

git = Github(username, password)
git.login()
git.followers()
print(git.follower)