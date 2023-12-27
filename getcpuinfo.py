import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import selenium.common.exceptions

if len(sys.argv)<2:
    print("Usage: "+sys.argv[0]+" cpu_name")
    sys.exit()

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#get cpu name by concatenating all argvs from 1 to n
cpu=""
for arg in sys.argv[1:]:
    cpu+=arg+"+"

#strip last character    
cpu=cpu[:-1]

url="https://www.cpubenchmark.net/cpu.php?cpu="+cpu
print("Retrieving cpu mark from: "+url)
driver.get(url)

try:
    cpuname = driver.find_element(By.XPATH, '//*[@id="main_content"]/div[1]/h1')
    cpumark = driver.find_element(By.XPATH, '//*[@id="main_content"]/div[3]/div[2]/div[2]/div[1]/div/div[2]/span[1]')
except selenium.common.exceptions.NoSuchElementException:
    print("Error: unable to locate element")
    sys.exit()


print("CPU: "+ cpuname.get_attribute('innerHTML'))
print("CPUMark: "+ cpumark.get_attribute('innerHTML'))

driver.close() 
