import time
import hashlib
from urllib.request import urlopen, Request


class Website_Check:
    def __init__(self) -> None:
        self.currentHash = None
        self.newHash = None
        self.response = None
        self.changed = None
        # replace with the websites URL
        self.url = Request(
            "WEBSITEURL",
            headers={"User-Agent": "Mozilla/5.0"},
        )

    def get_response(self):
        # to perform a GET request and load the
        # content of the website and store it in a var
        self.response = urlopen(self.url).read()

    def hash(self):
        # creates initial hash
        self.currentHash = hashlib.sha224(self.response).hexdigest()
        # wait for x seconds
        time.sleep(5)

    def checkSite(self):
        while True:
            try:
                # perform the get request and store it in a var
                self.response = urlopen(self.url).read()

                # create a hash
                self.currentHash = hashlib.sha224(self.response).hexdigest()

                # wait for x seconds
                time.sleep(5)

                # perform the get request
                self.response = urlopen(self.url).read()

                # create a new hash
                self.newHash = hashlib.sha224(self.response).hexdigest()

                # check if new hash is same as the previous hash
                if self.newHash == self.currentHash:
                    self.changed = False
                    # change continue to return if you would like for it to check only once per iteration
                    continue

                # if something changed in the hashes
                else:
                    # notify in console
                    print("The website has changed")

                    # again read the website
                    self.response = urlopen(self.url).read()

                    # create a hash
                    self.currentHash = hashlib.sha224(
                        self.response).hexdigest()

                    # wait for x seconds
                    time.sleep(5)
                    self.changed = True
                    return
            # To handle exceptions
            except Exception as e:
                print("error")

    def checkWebsite(self):
        self.get_response()
        self.hash()
        self.checkSite()


if __name__ == "__main__":
    check = Website_Check()
    check.checkWebsite()
