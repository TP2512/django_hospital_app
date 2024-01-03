import requests

def test_portal_up():
    url = "http://127.0.0.1:8000/admin"  # Replace with the URL of the portal you want to check

    try:
        response = requests.get(url)
        res = response.status_code
        print("poratl is up")
    except:
        res = 500

    assert res == 200, f"Portal is not up. Status code: {res}"

if __name__=="__main__":
    test_portal_up()