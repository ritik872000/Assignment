import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=24&Tx_State=UP&Tx_District=1&Tx_Market=0&DateFrom=01-Jan-2020&DateTo=31-Dec-2021&Fr_Date=01-Jan-2020&To_Date=31-Dec-2021&Tx_Trend=0&Tx_CommodityHead=Potato&Tx_StateHead=Uttar+Pradesh&Tx_DistrictHead=Agra&Tx_MarketHead=--Select--'

# request to fetch the raw html content
html_content = requests.get(url).text

# parsing html content
soup = BeautifulSoup(html_content, "lxml")

agri_table = soup.find("table", attrs={"class": "tableagmark_new"})

agri_table_data = agri_table.find_all("tr")  

headings = []
for td in agri_table_data[0].find_all("th"):
    # remove any newlines and extra spaces from left and right
    headings.append(td.b.text.replace('\n', ' ').strip())

rows = []
for child in soup.find('table', attrs={"class": "tableagmark_new"}).children:
    row = []
    for td in child:
        try:
            row.append(td.text.replace('\n', '').strip())
            
        except:
            continue
    if len(row) > 0:
        rows.append(row)

df = pd.DataFrame(rows[1:], columns=rows[0])

df.to_csv(r'C:\Users\ritik\Desktop\agri.csv')