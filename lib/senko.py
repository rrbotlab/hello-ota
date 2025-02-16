import urequests
import uhashlib


def _check_hash(x, y):
    x_hash = uhashlib.sha1(x.encode())
    y_hash = uhashlib.sha1(y.encode())

    x = x_hash.digest()
    y = y_hash.digest()

    if str(x) == str(y):
        return True
    else:
        return False


class Senko:
    raw = "https://raw.githubusercontent.com"
    github = "https://github.com"

    def __init__(self, user, repo, branch="master", working_dir=None, files=["boot.py", "main.py"], url=None, headers={}):
        """Senko OTA agent class.

        Args:
            user (str): GitHub user.
            repo (str): GitHub repo to fetch.
            branch (str): GitHub repo branch. (master)
            working_dir (str): Directory inside GitHub repo where the micropython app is.
            url (str): URL to root directory.
            files (list): Files included in OTA update.
            headers (list, optional): Headers for urequests.
        """
        self.base_url = "{}/{}/{}/{}".format(self.raw, user, repo, branch) # if user else url.replace(self.github, self.raw)
        if working_dir is not None:
            self.url = url if url is not None else "{}/{}".format(self.base_url, working_dir)
        else:
            self.url = url if url is not None else self.base_url
        self.headers = headers
        self.files = files

    def _get_file(self, url):
        try:
            payload = urequests.get(url, headers=self.headers)
            code = payload.status_code

            if code == 200:
                return payload.text
            else:
                raise ValueError('(1) Github return code: ' + str(code))

        except NotImplementedError:
            raise #ValueError('(2) Github error')

    def _check_all(self):
        changes = []

        for file in self.files:
            latest_version = self._get_file(self.url + "/" + file)
            if latest_version is None:
                continue

            try:
                with open(file, "r") as local_file:
                    local_version = local_file.read()
            except:
                local_version = ""

            if not _check_hash(latest_version, local_version):
                changes.append(file)

        return changes

    def fetch(self):
        """Check if newer version is available.

        Returns:
            True - if is, False - if not.
        """
        if not self._check_all():
            return False
        else:
            return True

    def update(self):
        """Replace all changed files with newer one.

        Returns:
            True - if changes were made, False - if not.
        """
        changes = self._check_all()

        for file in changes:
            with open(file, "w") as local_file:
                local_file.write(self._get_file(self.url + "/" + file))

        if changes:
            return True
        else:
            return False
