import requests

class Model:
    """
    Model in the MVC paradigm.
    """

    def __init__(self
                 ) -> None:
        pass

    def print_res(self):
        BASE_URL = "http://ergast.com/api/f1"
        ALL_JSON = "/current/driverStandings.json"

        request_url = f"{BASE_URL}{ALL_JSON}"
        response = requests.get(request_url)

        if response.status_code == 200:
            data = response.json()['MRData']
        else:
            print("Error")

        standing = data['StandingsTable']['StandingsLists'][0]['DriverStandings']

        result = {}
        for i in range(len(standing)):
            classement = {standing[i]['Driver']['familyName']}
            points = {standing[i]['points']}
            result[i+1] = (classement, points)

        print(result)