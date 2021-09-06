import requests

def main():
    print(requests.get("https://raw.githubusercontent.com/Xiaoyu-Ben-Wang/404-lab-1/main/requests_lab.py").text)

if __name__=='__main__':
    main()