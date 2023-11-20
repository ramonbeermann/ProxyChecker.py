import requests
import threading

# Funktion zum Lesen der Proxyliste aus der Datei
def read_proxy_list(file_name):
    with open(file_name, 'r') as file:
        proxies = [line.strip() for line in file.readlines() if line.strip()]
    return proxies

# Funktion für Anfragen mit Proxies
def make_request_with_proxy(proxy):
    global proxies_with_200_response
    try:
        response = requests.get(test_url, proxies={"http": proxy, "https": proxy}, timeout=10)
        if response.status_code == 200:
            proxies_with_200_response.append(proxy)
    except requests.RequestException as e:
        print(f"Fehler beim Testen des Proxys {proxy}: {e}")

# Basis-URL für den Test (Anpassen an deine Bedürfnisse)
test_url = 'https://example.com'  # Hier die Test-URL einfügen

# Dateinamen für die Proxy-Listen
input_proxy_file = 'list.txt'
output_proxy_file = 'res_list.txt'

# Proxies aus der Datei lesen
proxy_list = read_proxy_list(input_proxy_file)

# Liste für Proxies mit Statuscode 200
proxies_with_200_response = []

# Maximal zulässige Threads
max_threads = 10

# Anfragen in Threads senden
threads = []
for proxy in proxy_list:
    if len(threads) >= max_threads:
        for thread in threads:
            thread.join()
        threads = []

    thread = threading.Thread(target=make_request_with_proxy, args=(proxy,))
    thread.start()
    threads.append(thread)

# Auf die Beendigung aller Threads warten
for thread in threads:
    thread.join()

# Proxy-Adressen mit Statuscode 200 in eine Datei speichern
with open(output_proxy_file, 'w') as output_file:
    for proxy in proxies_with_200_response:
        output_file.write(f"{proxy}\n")

print(f"Proxies mit Statuscode 200 wurden in '{output_proxy_file}' gespeichert.")
