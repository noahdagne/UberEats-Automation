# UberEats-Automation
Skip to content
 noahdagne / igbot
Code  Issues 0  Pull requests 0  Projects 0  Wiki  Security  Pulse  Community
igbot
/
README.md
 


2
​
3
### Installation
4
* Selenium
5
  ```
6
  pip install selenium
7
  ```
8
* [Gecodriver](https://github.com/mozilla/geckodriver/releases)
9
* [Selenium Installation](https://selenium-python-readthedocs.io/insntallation.html#downloading-python-bindings-for-selenium)
10
  ```
11
  sudo mv geckodriver /usr/local/bin
12
  ```
13
14
  ```
15
  python first.py
16
  ```
17
### Code Workflow
18
* `igBot.new_phone(self)`
19
  * Generates a non-VOIP number to verify codes in the future
20
  * Handles 2FA confirmation
21
  * Enter received SMS code to console
22
* `igBot.sign_up(self)`
23
  * Generates random name to be used & inputs into corresponded boxes
24

​
@noahdagne
Commit changes
Commit summary 
Update README.md
Optional extended description
Add an optional extended description…
  Commit directly to the master branch.
  Create a new branch for this commit and start a pull request. Learn more about pull requests.
 
© 2019 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
