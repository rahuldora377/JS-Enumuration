import sys
import threading
import requests

#script.py file_name thread_no
def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(url)
    except:
        pass

def main():
    file_name = sys.argv[1]
    num_threads = int(sys.argv[2])

    with open(file_name) as f:
        urls = [url.strip() for url in f.readlines()]

    threads = [threading.Thread(target=check_url, args=(url,)) for url in urls]
    
    for i in range(0, len(threads), num_threads):
        for j in range(i, min(i + num_threads, len(threads))):
            threads[j].start()
        
        for j in range(i, min(i + num_threads, len(threads))):
            threads[j].join()

if __name__ == '__main__':
    main()
