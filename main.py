import requests
from bs4 import BeautifulSoup

URL = "https://www.kumarijob.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="job-list")
# print(results.prettify())
job_elements = results.find_all("li")

for job_element in job_elements:
  title_element = job_element.find("h5")
  company_element = job_element.find("div", class_="text-wrap").find("a")
  
  print(title_element.text)
  print(company_element.text)
  print("-----------------")
