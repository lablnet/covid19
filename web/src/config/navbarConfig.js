var navbarConfig = {
  "pk": {
    "1": {
      "name": "Home",
      "slug": "/",
      "type": "route",
      "hasdropdown": false,
    },
    "2": {
      "name": "Vaccine",
      "slug": "https://ncoc.gov.pk/covid-vaccination-en.php",
      "type": "url",
      "hasdropdown": false,
    },
    "3": {
      "name": "Deep Dive",
      "slug": "#",
      "type": "route",
      "hasdropdown": true,
      "dropdown": {
        "1": {
          "name": "Quarantine Facilities",
          "slug": "/quarantine",
          "type": "route",
          "hasdropdown": false,
        },
        "2": {
          "name": "Labs",
          "slug": "/labs",
          "type": "route",
          "hasdropdown": false,
        },
        "3": {
          "type": "divider",
        },
        "4": {
          "name": "Forecast",
          "slug": "/forecast",
          "type": "route",
          "hasdropdown": false,
        }
      }
    },
    "4": {
      "name": "Map",
      "slug": "/map",
      "type": "route",
      "hasdropdown": false,
    },
  },
  "tw": {

  }
}

export default navbarConfig
