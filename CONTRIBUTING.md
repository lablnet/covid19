
## CONTRIBUTING  
Contributions are welcome, and they are greatly appreciated! Every little bit helps! You can contribute in many ways.  
## Types of Contributions - Reporting a bug  
- Discussing the current state of the code  
- Submitting a fix  
- Adding scrapper for your Country  
- Becoming a maintainer  
  
Please make sure open `issue` before creating `PR`  
  
## How to add my country scrapper?
  Well, this is pretty simple, but you have to consider few things in your mind.
  1. Create Directory inside `Countries` like we have `Pakistan` your all scrapping files, generating csv and JavaScript JSON file should be their.
  2. Add source in `Source.md` file with your country name.
  3. Write GitHub workflow to automate your files you can see sample form `pk.yaml`
  
  
###  Database structure
Actually, there is no database structure that you need to follow, but when you generate CSV, and JSON file the structure should be follow as below:
`cases.csv`
id, datetime, type, description


### Configuration file
You can see configuration file in root of this project, that actually defines database schema, you should copy that inside your folder modify your schema as needed
for the database you should its better to use class that can be found inside `src/_sqlite,py` there are few messy code exists, but you can ignore that. if you want to create mode function, you should inherit that class inside your own.
you can load files from `src` as below
```py
import sys  
sys.path.append('./')  
   
from src._sqlite import _sqlite  
from src.__config import get_config
```
you can define folder variable which points to root of the project so you can easily access the other directory.
```py
from pathlib import Path  
  
folder = str(Path("").parent.absolute()).replace("Countries\coubtry_name_goes_here", "") + "/"```
 ```

**NOTE: Currently our frontend do not support multiple country, but we're willing to as we got new country be added. 
Thanks**
## License  
  
By contributing, you agree that your contributions will be licensed under GNU GPL-3 License.