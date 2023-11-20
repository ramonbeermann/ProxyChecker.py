HTTP Proxy Checker

This Python script tests a list of HTTP proxies against a specified URL, identifying proxies that return a status code of 200. It utilizes threading to enhance efficiency in testing multiple proxies simultaneously.
How to Use

    Requirements: Ensure you have Python installed.
    Install Dependencies: You may need to install the requests library by running pip install requests.
    Adjust Settings: Modify the test_url variable to the URL you want to test and adjust the input proxy file (list.txt) to contain your list of proxies.
    Run the Script: Execute the script by running python proxy_checker.py.
    Output: Successful proxies (status code 200) will be saved in res_list.txt.

Code Overview

The code reads a list of proxies from a file (list.txt), then uses threading to perform HTTP GET requests using each proxy. Proxies that return a 200 status code are saved into res_list.txt. Adjust the max_threads variable to control the number of simultaneous requests.

Feel free to tailor the script to your specific requirements and make sure to handle proxies ethically and within legal boundaries.

For any queries or improvements, please feel free to contribute or raise issues in the repository. Enjoy testing your proxies!
Disclaimer

This script is for educational purposes only. Use it responsibly and comply with the terms of service of the URLs you test and any applicable laws. The developer holds no responsibility for any misuse of this script.
# ProxyCheckerv1
