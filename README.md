# minex-bonus-collector
Collects bonuses on minex using selenium webdriver

An issue I have discovered:
 - sometimes the chromedriver.exe will have a longer time to get to the login page. This will cause the enter key to be sent even before the login process; the resulting scenario is the program trying to access the bonuses but without being logged in yet.
   - this can be fixed by increasing the sleep time to the suited duration. 
   - you could also add more sleep functions between loading screens to give way to the website buffer due to internet connection
