
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

	return fname
