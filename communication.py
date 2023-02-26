from executeServices import execute_service


class Communication(object):
    def __init__(self, client_id):
        self.id = client_id

    @staticmethod
    def send_request(data):
        separated = data.split(",")

        response = execute_service(separated)

        return str(response)
