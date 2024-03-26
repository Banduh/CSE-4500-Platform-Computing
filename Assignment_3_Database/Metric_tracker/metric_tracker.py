import time
from selenium import webdriver
import collections
import pymysql

# Initialize browser
driver = webdriver.Chrome()

# Navigate to your website 
driver.get("http://localhost:3000/")

# Initialize variables
metrics = []
SAMPLE_SIZE = 2
count = 0
start_time = time.time()
while count < SAMPLE_SIZE:
    # Track presence time 
    current_time = time.time()
    presence_time = current_time - start_time
    print(f"Presence time: {presence_time} seconds")
    # metrics ["Presence time {Seconds}"].append(presence_time)
    
    # Track scrolling
    scroll_height = driver.execute_script("return document.body.scrollHeight")  
    current_scroll = driver.execute_script("return window.pageYOffset")
    print(f"Scrolled {current_scroll}/{scroll_height} pixels")
    # metrics ["Presence time {Seconds}"].append(presence_time)
    metrics.append({"TIMESTAMP (HH:MM:SS)": time.strftime("%H:%M:%S", time.localtime()),
                    "Presence time (seconds)" : presence_time, 
                    "Scrolling (Pixels)" : current_scroll/scroll_height } )

    count += 1
    time.sleep(2) 
      
driver.quit()
print(metrics)

conn = pymysql.connect(
    host = "127.0.0.1",
    user = "root",
    password = "BTPandas1591!",
    db = "metrics"
    charset = 'utf8mb4'
    cursorclass=pymysql.cursors.Dictcursor
)

try:
    with conn.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `metrics` (`time`, `Scrolling`) VALUES ('presence_time', 'current_scroll/scroll_height')"

    # Commit changes
    conn.commit()

    print("Record inserted successfully")
finally:
    conn.close()