import requests
import time

class Client:
	def __init__(self, protocol="https", domain="", cookies={}, args={}, headers={}, cache=None, ratelimit={}):
		self.domain = domain
		self.protocol = protocol
		self.cookies = cookies
		self.args = args
		self.headers = headers

		self.cooldown = cache
		self.ratelimit = {"reqs":1,"reset":0, **ratelimit}

		self._cache = {}
		self._cachetimes = {}

		self._rl = []

	def url(self, **kwargs):
		arguments = {**self.args, **kwargs}
		path = kwargs.get("path", "")

		url = self.protocol + '://' + self.domain + path
		if arguments != {}:
			url += '?' + '&'.join(f'{i}={arguments[i]}' for i in arguments)
		
		return url

	def dict_path(dct, path):
		path = path.split('/')
		elem = dct
		for i in path:
			if not i == path[-1]:
				elem = elem.get(i, {})
				if not type(elem) == dict:
					elem = {}
			else:
				return elem.get(i, None)

	def get(self, path, *args, **kwargs):
		if len(args) > 0:
			settings = kwargs
			kwargs = args[0]
		else:
			settings = {}
		ctime = time.time()
		if self.cooldown != None:
			if path in self._cache:
				lasttime = self._cachetimes[path]
				if (ctime - lasttime) > self.cooldown:
					resp = self._get(path, settings, kwargs)
					self._cache[path] = resp
					self._cachetimes[path] = ctime
					return resp
				else:
					return self._cache[path]
			else:
				resp = self._get(path, settings, kwargs)
				self._cache[path] = resp
				self._cachetimes[path] = time.time()
				return resp
		else:
			return self._get(path, settings, kwargs)
	
	def _get(self, path, settings, kwargs):
		ctime = time.time()
		cd, limit = self.ratelimit['reset'], self.ratelimit['reqs']
		self._rl = [i for i in self._rl if (ctime - i) < cd]
		
		if len(self._rl) >= limit:
			return "You got rate limited!"
		return self.__get(path, settings, kwargs)
		
	def __get(self, path, settings, kwargs):
		if self.ratelimit != None:
			self._rl.append(time.time())

		url = self.url(path=path, **kwargs)
		cookies = {**self.cookies, **kwargs.get("cookies", {})}

		response = requests.get(url, cookies=cookies, headers=self.headers)
		response.find = lambda path: Client.dict_path(response.json(), path)
		return response