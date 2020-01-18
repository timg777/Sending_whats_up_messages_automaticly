from selenium import webdriver
import os

driver = webdriver.Chrome('./chromedriver')
driver.get('https://web.whatsapp.com/')

print('Choose and download chromedriver via chrome to current directory --> https://chromedriver.chromium.org/downloads')

print('Before you write your dataa, please do not scan QR code')
print('Scan it after third step of authorization\n')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_3u328')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
