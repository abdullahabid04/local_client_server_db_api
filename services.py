import requests


def check_pressure_update_flag(tbs_id):
    sid = str(tbs_id)

    url = "https://care.iub.edu.pk/sngpl/api/demandflag?sid={}".format(sid)

    try:
        req = requests.get(url)

        if req.ok:
            if req.status_code == 200:
                res = req.json()
                flag = str(res)
                return flag
    except Exception as e:
        pass


def get_sensor_in_pressure(tbs_id):
    sid = str(tbs_id)

    url_in = "https://care.iub.edu.pk/sngpl/api/pressure?sid={}&flag=0".format(str(sid))

    try:
        req = requests.get(url_in)

        if req.ok:
            if req.status_code == 200:
                res = req.json()
                return res
    except Exception as e:
        pass


def get_sensor_out_pressure(tbs_id):
    sid = str(tbs_id)

    url_out = "https://care.iub.edu.pk/sngpl/api/pressure?sid={}&flag=1".format(str(sid))

    try:
        req = requests.get(url_out)

        if req.ok:
            if req.status_code == 200:
                res = req.json()
                return res
    except Exception as e:
        pass


def write_data(tbs, pres_val):
    sid = str(tbs)
    pressure = str(pres_val)

    url = "https://care.iub.edu.pk/sngpl/api/demand"
    obj = {"sid": sid, "value": pressure}

    try:
        req = requests.post(url, data=obj)

        if req.ok:
            if req.status_code == 200:
                res = req.json()
                return res
    except Exception as e:
        pass


def get_dated_pressure(tbs_id, start_date, end_date):
    sid = str(tbs_id)
    start = str(start_date)
    end = str(end_date)

    url = "https://care.iub.edu.pk/sngpl/api/allpressures"
    obj = {"sid": sid, "start": start, "end": end}

    try:
        req = requests.post(url, data=obj)

        if req.ok:
            if req.status_code == 200:
                res = req.json()
                return res
    except Exception as e:
        pass


def set_station_info(name, regulator):
    tbs_name = str(name)
    tbs_regultor = str(regulator)

    url = "https://care.iub.edu.pk/sngpl/api/stations"
    obj = {"name": tbs_name, "regulator": tbs_regultor}

    try:
        req = requests.post(url, data=obj)

        if req.ok:
            if req.status_code == 200:
                res = req.json()
                return res
    except Exception as e:
        pass


def get_specific_station_info(tbs_id):
    sid = str(tbs_id)

    url = "https://care.iub.edu.pk/sngpl/api/stations?sid={}".format(sid)

    try:
        req = requests.get(url)

        if req.ok:
            if req.status_code == 200:
                res = req.json()
                return res
    except Exception as e:
        pass


def get_all_stations_info():
    url = "https://care.iub.edu.pk/sngpl/api/stations"

    try:
        req = requests.get(url)

        if req.ok:
            if req.status_code == 200:
                res = req.json()
                return res
    except Exception as e:
        pass


def set_site_info(tbs_id, name, value):
    sid = str(tbs_id)
    para_name = str(name)
    para_value = str(value)

    url = "https://care.iub.edu.pk/sngpl/api/sitedata"
    obj = {"sid": sid, "name": para_name, "value": para_value}

    try:
        req = requests.post(url, data=obj)

        if req.ok:
            if req.status_code == 200:
                res = req.json()
                return res
    except Exception as e:
        pass


def get_site_info(tbs_id):
    sid = str(tbs_id)

    url = "https://care.iub.edu.pk/sngpl/api/sitedata?sid={}".format(sid)

    try:
        req = requests.get(url)

        if req.ok:
            if req.status_code == 200:
                res = req.json()
                return res
    except Exception as e:
        pass


def find_station_id_by_name(name):
    tbs_name = str(name)

    url = "https://care.iub.edu.pk/sngpl/api/stations"

    try:
        req = requests.get(url)

        if req.ok:
            if req.status_code == 200:
                res = req.json()

                for i in range(len(res)):
                    if res[i]["tbs_name"] == tbs_name:
                        return str(res[i]["id"])
                return "NF"
    except Exception as e:
        pass
