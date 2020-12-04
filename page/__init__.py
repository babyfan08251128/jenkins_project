"""页面元素信息"""

from selenium.webdriver.common.by import By
#新建联系人
new_contacts = By.ID,"com.android.contacts:id/floating_action_button"

#姓名输入
name_input = By.XPATH,"//*[@text ='姓名']"

#电话号输入
num_input = By.XPATH,"//*[@text ='电话']"