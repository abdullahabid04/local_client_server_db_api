services = {
    "set_demand": {
        "url": "https://care.iub.edu.pk/sngpl/api/demand",
        "method": "post",
        "parameters": {
            "sid": None,
            "value": None
        }
    },
    "get_demand": {
        "url": "https://care.iub.edu.pk/sngpl/api/demand?sid={}",
        "method": "get",
        "parameters": {
            "sid": None
        }
    },
    "get_flag": {
        "url": "https://care.iub.edu.pk/sngpl/api/demandflag?sid={}",
        "method": "get",
        "parameters": {
            "sid": None
        }
    },
    "set_pressure": {
        "url": "https://care.iub.edu.pk/sngpl/api/pressure",
        "method": "post",
        "parameters": {
            "sid": None,
            "flag": None,
            "value": None
        }
    },
    "get_pressure": {
        "url": "https://care.iub.edu.pk/sngpl/api/pressure?sid={}&flag={}",
        "method": "get",
        "parameters": {
            "sid": None,
            "flag": None
        }
    },
    "get_all_pressures": {
        "url": "https://care.iub.edu.pk/sngpl/api/allpressures",
        "method": "post",
        "parameters": {
            "sid": None,
            "start": None,
            "end": None
        }
    },
    "set_station": {
        "url": "https://care.iub.edu.pk/sngpl/api/stations",
        "method": "post",
        "parameters": {
            "name": None,
            "regulator": None
        }
    },
    "get_station": {
        "url": "https://care.iub.edu.pk/sngpl/api/stations?sid={}",
        "method": "get",
        "parameters": {
            "sid": None
        }
    },
    "get_all_stations": {
        "url": "https://care.iub.edu.pk/sngpl/api/stations",
        "method": "get",
        "parameters": {
        }
    },
    "set_site": {
        "url": "https://care.iub.edu.pk/sngpl/api/sitedata",
        "method": "post",
        "parameters": {
            "sid": None,
            "name": None,
            "value": None
        }
    },
    "get_site": {
        "url": "https://care.iub.edu.pk/sngpl/api/sitedata?sid={}",
        "method": "get",
        "parameters": {
            "sid": None
        }
    }
}
