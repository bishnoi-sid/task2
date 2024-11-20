import requests
import time

APPLICATION_URL = "http://application:5000/metrics"  # 'application' is the container name in Docker Compose

def scrape_metrics():
    while True:
        try:
            response = requests.get(APPLICATION_URL)
            if response.status_code == 200:
                metrics = response.json()
                print(f"CPU Usage: {metrics['cpu_percent']}%")
                print(f"Memory Usage: {metrics['memory_usage']}%")
            else:
                print(f"Failed to fetch metrics: {response.status_code}")
        except Exception as e:
            print(f"Error occurred: {str(e)}")
        
        time.sleep(5)  # Scrape every 5 seconds

if __name__ == '__main__':
    scrape_metrics()
