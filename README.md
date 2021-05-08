[![Update Records from Pak gov website](https://github.com/lablnet/covid19-parser/actions/workflows/pk.yaml/badge.svg)](https://github.com/lablnet/covid19-parser/actions/workflows/pk.yaml)
[![Who update](https://github.com/lablnet/covid19-parser/actions/workflows/who.yaml/badge.svg)](https://github.com/lablnet/covid19-parser/actions/workflows/who.yaml)
[![Web Build and Deploy](https://github.com/lablnet/covid19-parser/actions/workflows/web_build.yml/badge.svg)](https://github.com/lablnet/covid19-parser/actions/workflows/web_build.yml)

# covid19-parser

COVID-19 Dashboard and parser

  
  The sole purpose of this dashboard is to make the general public aware of the current situation about COVID-19 virus outbreak in Pakistan.

We have tried to sketch a clear picture for you in the simplest and the easiest manner so that you can explain everything to others in a convenient way, saving time and eliminating misconceptions about COVID-19.

If you have any idea/suggestion to improve this dashboard, please write to mumerfarooqlablnet01@gmail.com

## Purpose

1. Develop awareness among the public.
2. Visualized the data for everyone to understand.
3. Gather data for research/experiences.

## Features

1. Parse data from government websites automatically daily, automated using GitHub Action.
2. Parse data from WHO automatically on every Monday, automated using GitHub Actions
3. Dashboard to visualize data.
4. Publicly Data downloading.

## Contribution

You're welcome to contribute to this project.

You should follow contribution guideline [Contribution guideline](https://github.com/lablnet/covid19-parser/blob/master/CONTRIBUTING.md)
  
## File Structure
  ```sh covid19_pakistan.sqlite``` Core Database File
  
  ```sh today.py``` Gather Data from  https://covid.gov.pk/ last 24 hrs stat.
  
  ```sh covid19_pk_official.py``` Gather Data from  https://covid.gov.pk/
     
  ```sh who.py``` Gather Data from  https://covid19.who.int
  
  ```sh toCsv.py``` Export Date to CSV
    
  ```sh toJs.py``` Export Date to JavaScript  JSON
    
  ```sh config.json``` Config File for the project.
    
  ```sh src/__config.json``` Helper file for getting value from config.
        
  ```sh src/_sqlite.json``` SQLite helper class.
    
  ```sh /web``` Folder contain web Dashboard.
    
  ```sh server.py```Backend Server deprecated.
    

## License

GPL-3

## Support

If you like this project; Donate coffee?

Here is the bitcoin address.

[![Balance](https://img.balancebadge.io/btc/37x6PA4qtPu2fQnYdW5U7jztYhbchASpBV.svg)](https://img.balancebadge.io/btc/37x6PA4qtPu2fQnYdW5U7jztYhbchASpBV.svg)

```37x6PA4qtPu2fQnYdW5U7jztYhbchASpBV```

Thank you so much.

## Disclaimer

**I do not accept responsibility for any illegal usage**
