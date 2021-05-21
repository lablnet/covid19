
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

### Adding frontend
Adding frontend now is too easy, there are few config file you need to manipulate, are as follow:
Inside `web/src/config` you will find configuration file.
1. `navbarConfig.js` Define navigation for your country site, all possible `{key: value}` in sample which is for  `Pakistan` is given.
2. `routeConfig.ts` Routes for your country.
3. `datafileConfig.js` defines country wise javascript data file that need's to be loaded, it can be with same name because it load once country match.
     
      **Note: the file `datafileConfig.js` can be found inside `web/public/` directory.

once you add configuration now the next step is to write `views` it can be tricky but you can just copy files from `Pakistan` folder inside `web/src/views` and paste into your country folder.
Once you refer to varialbe that is loaded from JavaScript file that is loaded via dynamically so you have to write above that
```js
// eslint-disable-next-line no-undef
```
it is because the `eslint` validates the file on running either on local or deployment.
you can 	`watch` the changes with following command:
```sh
npm run serve
```
**Note: currently the function `get_country` just returns  country code for `Pakistan` for testing you can change it to your country code.**


**Thanks**
## License  
  
By contributing, you agree that your contributions will be licensed under GNU GPL-3 License.
