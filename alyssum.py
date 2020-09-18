import pandas as pd
from googletrans import Translator
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from sqlalchemy import create_engine


def scraping(url):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options = options)
    driver.implicitly_wait(15)
    driver.get(url)
    data = []
    df = pd.DataFrame(columns = (['Indicator Name', 'Weights', 'Grading', 'Scoring Result']))

    columns = len(driver.find_elements_by_xpath('//*[@id="combineStagePrepare"]/div[1]/div[1]/div/div[2]/div/div/div/span/div/table/thead/tr/th'))
    rows = len(driver.find_elements_by_xpath('//*[@id="combineStagePrepare"]/div[1]/div[1]/div/div[2]/div/div/div/span/div/table/tbody/tr'))

    for i in range(1, rows+1):
        data.clear()
        for j in range(1, columns+1):
            xpath = f'//*[@id="combineStagePrepare"]/div[1]/div[1]/div/div[2]/div/div/div/span/div/table/tbody/tr[{i}]/td[{j}]'
            table_data = driver.find_element_by_xpath(xpath)
            data.append(table_data.text)
        df.loc[len(df)] = data

    return translate_(df)

def translate_(df):
    translator = Translator()
    translated_df = df
    translated_df['Indicator Name'] = df['Indicator Name'].map(lambda x: translator.translate(x).text)
    #return translated_df
    return export_to_sql(translated_df)

def export_to_sql(df):
    engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/Alyssum')
    df.to_sql(name = 'alyssum', con = engine, if_exists = 'replace', index = False)
    pd.read_sql('alyssum', engine)


if __name__ == '__main__':
    url = 'https://www.cpppc.org:8082/inforpublic/homepage.html#/projectDetail/91fe736c280a47b183e2727b40cc8dc4'
    print(scraping(url))
