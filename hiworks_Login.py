# %%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


def hiworks_login(id, pw):

    try:
        # ▶ 기본 변수 할당

        status_code = "Fail"
        URL ="https://office.hiworks.com/powergen.ai/"
        
        for retry in range(3):
            
            if(status_code=="Success"): break
            
            option = webdriver.ChromeOptions()
            option.add_argument('start-maximized')

            driver = webdriver.Chrome(executable_path='chromedriver')
            driver.get(url=URL)

            driver.implicitly_wait(time_to_wait=5)

            # ▶ 로그인 시도
            id_input = driver.find_element_by_xpath('//*[@id="office_id"]')
            driver.implicitly_wait(time_to_wait=5)
            pw_input = driver.find_element_by_xpath('//*[@id="office_passwd"]')
            driver.implicitly_wait(time_to_wait=5)
            
            id_input.send_keys(id)
            pw_input.send_keys(pw)
            
            login_button = driver.find_element_by_xpath('//*[@id="contents"]//input[@type="submit"]').click()
            
            ## 로그인 확인 처리
            mail_button = driver.find_elements_by_xpath('//*[@id="contents"]//p[contains(text(), "메일")]')
            if len(mail_button) >= 1:
                status_code = 'Success'
            else:
                driver.close()
        
    except Exception as e:
        print(e)
    finally:
        print(status_code + ' // try : ' + str(retry))



# %%
