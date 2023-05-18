from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import csv
from selenium.webdriver.common.keys import Keys
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

app = Dash()

job_options = [
    {'label': 'google', 'value': 'google'},
    {'label': 'apple', 'value': 'apple'},
    {'label': 'amazon', 'value': 'amazon'},
    {'label': 'oracle', 'value': 'oracle'},
    {'label': 'ibm', 'value': 'ibm'},
    {'label': 'sap', 'value': 'sap'},
    {'label': 'salesforce', 'value': 'salesforce'},
    {'label': 'accenture', 'value': 'accenture'},
    {'label': 'Adobe', 'value': 'adobe'},
    {'label': 'Intel', 'value': 'intel'},
    {'label': 'Cisco', 'value': 'cisco'},
    {'label': 'dell-technologies', 'value': 'dell-technologies'},
    {'label': 'Infosys', 'value': 'infosys'},
    {'label': 'VMware', 'value': 'VMware'},
    {'label': 'Tata-consultancies', 'value': 'Tata-consultancies'},

]

search = dcc.Dropdown(id="input-search-term", options=job_options, value="software-engineer")

app.layout = html.Div(
    children=[
        html.H1("Job Search"),
        html.Label("Select a job:"),
        search,
        html.Button("Search", id="btn-search", n_clicks=0),
        html.H2("Top 40 Job Links:"),
        html.Ul(id="articles"),
    ]
)

@app.callback(
    Output("articles", "children"),
    [Input("btn-search", "n_clicks")],
    [Input("input-search-term", "value")]
)

def perform_search(articles , options):
    options = Options()
    options.add_argument("--headless=new")
    driver1 = webdriver.Chrome(options=options)
    # driver1 = webdriver.Chrome('C:/Users/deepa/Downloads/chromedriver_win32/chromedriver.exe')
    driver1.get('https://www.naukri.com/')
    driver1.maximize_window()
    driver1.find_element(By.XPATH, '//*[@id="root"]/div[6]/div/span').click()
    box1 = driver1.find_element(By.XPATH, '//*[@id="root"]/div[6]/div/div[1]/div[1]/div/div/div/div[1]/div/input')
    query = {search}
    for i in query:
        box1.send_keys(i)
    driver1.find_element(By.XPATH, '//*[@id="root"]/div[6]/div/div/div[6]').click()
    time.sleep(5)
    #box2 = driver1.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/div/section[1]/div[2]/div[4]/div[2]/div[1]/label/i').click()
    articles = []
    url = driver1.find_elements(By.XPATH, '//*[@class="title ellipsis"]')
    while (True):
        try:
            time.sleep(2)
            elem = driver1.find_element(By.XPATH, "//a[@class='fright fs14 btn-secondary br2']")
            urls = driver1.find_elements(By.XPATH, '//*[@class="title ellipsis"]')
            for url in urls:
                href = articles.append(url.get_attribute("href"))
                print(len(articles))
                print(articles)
            if (len(articles) < 40):
                elem.click()
            else:
                break
        except(NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException,
               ElementClickInterceptedException) as ex:
            print("breaking as there is no next page")
            break
    return articles

if __name__ == "__main__":
    app.run_server(debug=True)