import pytest
from selenium import webdriver
from pageObjects.loginPage import loginPage
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen



class Test_001_Login:
    baseURL =ReadConfig.getApplicationURL
    username=ReadConfig.getUseremail
    password =ReadConfig.getPassword
    logger= LogGen.loggen()


    @pytest.mark.regression
    def test_login_title(self,setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started login page title test ****")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title= self.driver.title
        self.driver.close()
        if act_title=="Your store. Login":
            self.driver.close()
            self.logger.info("**** login page title test passed ****")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login_title.png")
            self.driver.close()
            self.logger.info("**** login page title test failed ****")
            assert False


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("****Started Login Test****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=loginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("****Login test passed ****")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("****Login test failed ****")
            assert False
