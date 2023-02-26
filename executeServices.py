import requests

from ServiceRequirements import services
from services import find_station_id_by_name


def execute_service(separated):
    try:
        service = services.keys()
        services_array = [item.strip() for item in service]
        service_string = ""
        for item in services_array:
            service_string += item + "\n"

        if str(separated[0]) not in service:
            return "No such service. Check your spelling.\navailable services :\n{}".format(service_string)
        else:
            url = services[str(separated[0])]["url"]
            method = services[str(separated[0])]["method"]
            parameters = services[str(separated[0])]["parameters"]
            arguments = [*separated[1:]]
            get_keys = parameters.keys()
            keys = [*get_keys]

            if len(keys) == len(parameters) == len(arguments):
                if len(keys) != 0:
                    sid = find_station_id_by_name(separated[1])
                    if sid == "NF":
                        return "tbs name not found Check your name and spelling"
                    else:
                        values = [sid, *separated[2:]]
                        for i in range(len(keys)):
                            parameters[keys[i]] = values[i]
                        try:
                            req = None
                            if method == "post":
                                req = requests.post(url, data=parameters)
                            if method == "get":
                                try:
                                    req = requests.get(url.format(*values))
                                except:
                                    req = requests.get(url)
                            if req is not None:
                                return req.text
                        except Exception as e:
                            pass
            else:
                return "Invalid Values, Please fill all the parameters correctly"
    except:
        return "Oops! Something went wrong.Please try again later"
