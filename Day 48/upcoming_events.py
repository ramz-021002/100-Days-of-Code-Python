from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")

# names = driver.find_elements(By.CLASS_NAME, value='event-widget')

# events = [name.text.split('\n') for name in names][0][2:]

# #print(events) #['2026-04-14', 'PyCon DE & PyData 2026', '2026-04-15', 'DjangoCon Europe 2026', '2026-04-17', 'PyTexas 2026', '2026-04-19', 'PyCon Austria 2026', '2026-04-22', 'The Carpentries - Plotting and Programming in Python']

# dates = events[::2] # filters dates which are in even index's
# event_names = events[1::2] # filters events names which are in odd index's

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

dates = [time.text for time in event_times]
event_names = [name.text for name in event_names]
final_dict = {}

for i in range(0, len(dates)):
    final_dict[i] = {"time": dates[i], "name": event_names[i]}

print(final_dict)


driver.quit()
