# Biofourmis

Repo to automate basic sanity flow in BioFourmis

This automation framework is build on pytest.



---
## Requriments:
* Chrome    - 92
* Python    - 3.9


## Application under test
* Web: BioFourmis
* API: https://deckofcardsapi.com/

---
## Installation
1. Clone the repo
```sh
  $ git clone https://github.com/sureshpathipati/Biofourmis.git
```
2. Install virtualenv
```sh
  $ pip3 install virtualenv
```
3. Create virtual env
 ```sh
  $ virtualenv <env_name>
    ex: virtualenv biofourmis
```
4. Open the virtual env(For winodows omit source)
```sh
  $ source <folder_name>/bin/activate
    ex: source biofourmis/bin/activate
```
5. Install dependencies using requirements file
```sh
  $ pip3 install -r requirements.txt
```
6. To Deactivate the virtual env use "deactivate" command
```sh
  $ deactivate
```
---

# Steps to uninstall virtualEnvironment
1. Remove packages
```sh
  $ pip uninstall -r requirements.txt -y
```
2. Come out off virtual env
```sh
  $ deactivate
```
3. Remove the environment folder
```sh   
  $ rm -r biofourmis/
```


## How to run a test suite file
1.use the following command
```sh
  $ pytest <file_name> --html=report.html
    ex: pytest bio_fourmis_test.py --html=report.html
```

## Folder Structure
  
  -api
     --end_points.py (Constants contains List of Endpoints)
     --open_api_test.py (Contains Actual test Cases)
  -biofourmis (Virtual Env)
  -config (Any configuration related files exits here)
     --browser_setup.py (Initialize chrome browser as if now)
  -pages
     --bio_fourmis_page.py (Contains all page objects as functions)
     --base_page.py (Contains common functions across all pages and act as parent class for all the plaform specific pages)
     --<platfrom_specific>_page.py
  -bio_fourmis_test.py (Contains actual UI Test Cases)
  -conftest.py (File specific to pytest, which gets loaded initially used for tearUp and tearDown)
  -requirements.txt (Contains project specific dependencies)
  -reports.html (Generated via inbuilt script after the execution)
  
