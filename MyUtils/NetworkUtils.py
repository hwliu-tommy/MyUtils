
import requests

# Functions
def get_html(uri, **kwargs):
        resp = requests.get(uri, kwargs)

        if not resp.ok:
                raise RuntimeError('Fail to get HTML from uri={}\nError code = {}\nResp text = {}'.format(
                        uri, resp.status_code, resp.text))

        return resp.text

def get_bin(fname, uri, dry_run=False, **kwargs):
        if dry_run:
                print("Download binary file: uri={}, fname={}, kwargs={}".format(uri, fname, kwargs))
        else:
                r = requests.get(uri, kwargs, stream=True)

                if r.status_code == 200:
                        with open(fname, 'wb') as f:
                                for chunk in r.iter_content(1024):
                                        f.write(chunk)
        return fname


# Class
class NetworkClient:
        def __init__(self, **ikwargs) -> None:
                self.env_kwargs = ikwargs

        # Static
        def get_html(self, uri, **ikwargs) -> str:
                kwargs = {**self.env_kwargs, **ikwargs}
                return get_html(uri, kwargs)

        def get_bin(self, fname, uri, dry_run=False, **ikwargs):
                kwargs = {**self.env_kwargs, **ikwargs}
                return get_bin(fname, uri, dry_run, kwargs)

        def setenv(self, **ikwargs):
                self.env_kwargs = {**self.env_kwargs, **ikwargs}

        def unsetenv(self, *iargs):
                for key in iargs:
                        try:
                                del self.env_kwargs[key]
                        except NameError:
                                pass

        def getenv(self, name):
                try:
                        return self.env_kwargs[name]
                except KeyError:
                        return None

        def getenvs(self, args):
                if args:
                        return dict((x, self.getenv(x)) for x in args)
                else:
                        return self.env_kwargs
