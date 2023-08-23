#Oppsition finder
# Maxwell Wippich
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask, request
import json

comp = []
def scrape(URL):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-crash-reporter")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-in-process-stack-traces")


    driver = webdriver.Chrome(options=chrome_options)
    print('https://www.'+ URL + '/')
    driver.get('https://www.'+ URL + '/')
    print("it passed this line")
    wait = WebDriverWait(driver, 30) #wait for page to load

    html = driver.page_source #get the html

    search_strings = ["LHInsights", "wp-content", "woocommerce", "foxentry", "smartlook", "crazyegg", "luigisbox", "bloomreach", "content=\"UPgates\"", "ecmtr", "Ecomail", "bsshop", "yottly", "boldem", "eshop-rychle", "presta", "presta", "mage/", "sites/default/files", "mailkit", "mailerlite", "myshoptet.com", "targito", "dg.incomaker"]
    search_tools = ["Leadhub", "Wordpress", "Woocommerce", "Foxentry", "Smartlook", "CrazyEgg", "Luigi’s Box", "Bloomreach/Exponea",  "Upgates", "Ecomail", "Ecomail", "BSShop", "Samba.ai", "Boldem", "Eshop-rychle", "Prestashop", "Magento", "Drupal", "Mailkit", "MailerLite", "Shoptet", "Targito", "Incomaker"]
    count = 0
    index = []
    for search_string in search_strings:
        if search_string in html:
            index.append(count)
        count += 1
    for tool in index:
        comp.append(search_tools[tool])

    driver.close()
    driver.quit()

def DNS(URL):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-crash-reporter")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-in-process-stack-traces")


    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://www.nslookup.io/domains/'+ URL + '/dns-records/txt/')
    #wait = WebDriverWait(driver, 100) #wait for page to load

    #element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#app > div.flex-grow.bg-neutral-100 > main > div.bg-white.shadow.p-6.pb-10.rounded-t > pre:nth-child(8)")))
    element = driver.find_element(By.CSS_SELECTOR, "#app > div.flex-grow.bg-neutral-100 > main > div.bg-white.shadow.p-6.pb-10.rounded-t > pre:nth-child(8)")
    # Get the fully loaded HTML content
    search_strings = ["spf.smartemailing.cz", "spfe.targito.com", "spf.mandrillapp.com", "spf.mailkit.eu", "incosrv.com"]
    search_tools = ["SmartEmailing", "Targito", "Mailchimp", "Mailkit", "Incomaker"]

    count = 0
    index = []
    text_content = element.text
    for search_string in search_strings:
        if search_string in text_content:
            index.append(count)
        count += 1
    for tool in index:
        comp.append(search_tools[tool])

    driver.close()
    driver.quit()


path_name = ''
service_name = 'default'
app = Flask(__name__)
@app.route("/")
def runner():
    url = request.args.get("url")
    if url:
        URL = url
    DNS(URL)
    scrape(URL)

    # Specify the file path where you want to save the .json file
    file_path = "opposition.json"

    # Use 'with' to ensure the file is properly closed after writing
    with open(file_path, "w") as json_file:
        json.dump(comp, json_file, indent=0)
    return 'finished'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
