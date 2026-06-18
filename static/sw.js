const CACHE_NAME = 'lms-v1';
const PRECACHE_URLS = [
	'/',
	'/offline.html',
	'/static/css/output.css',
	'/static/js/alpine.global.prod.js',
	'/manifest.json'
];

self.addEventListener('install', (event) => {
	event.waitUntil(
		caches.open(CACHE_NAME).then((cache) => cache.addAll(PRECACHE_URLS)).then(() => self.skipWaiting())
	);
});

self.addEventListener('activate', (event) => {
	event.waitUntil(
		caches.keys().then((keys) => Promise.all(keys.map((key) => {
			if (key !== CACHE_NAME) return caches.delete(key);
		}))).then(() => self.clients.claim())
	);
});

self.addEventListener('fetch', (event) => {
	const request = event.request;
	// For navigation requests, try network first, then fallback to cache, then offline page
	if (request.mode === 'navigate') {
		event.respondWith(
			fetch(request).then((response) => {
				return response;
			}).catch(() => caches.match('/offline.html'))
		);
		return;
	}

	// For other requests, respond with cache-first, then network
	event.respondWith(
		caches.match(request).then((cached) => cached || fetch(request).then((resp) => {
			// Cache fetched responses for future
			if (request.url.startsWith(self.location.origin)) {
				caches.open(CACHE_NAME).then((cache) => cache.put(request, resp.clone()));
			}
			return resp;
		}).catch(() => cached))
	);
});