{% load static %}
const CACHE_NAME = 'vphs-cache-v1';
const OFFLINE_URL = '/offline/';

const ASSETS_TO_CACHE = [
  '/',
  OFFLINE_URL,
  '{% static "homepage/assets/css/main.css" %}',
  '{% static "homepage/assets/vendor/bootstrap/css/bootstrap.min.css" %}',
  '{% static "homepage/assets/vendor/bootstrap-icons/bootstrap-icons.css" %}',
  '{% static "homepage/assets/vendor/aos/aos.css" %}',
  '{% static "homepage/assets/vendor/glightbox/css/glightbox.min.css" %}',
  '{% static "homepage/assets/vendor/swiper/swiper-bundle.min.css" %}',
  '{% static "homepage/assets/img/lo.png" %}',
  '{% static "homepage/assets/img/front.jpg" %}'
];

// Install service worker and cache assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[Service Worker] Caching core assets');
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
  self.skipWaiting();
});

// Activate service worker and clean up old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log('[Service Worker] Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// Fetch events: Network first, fallback to Cache, then Offline page
self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;

  event.respondWith(
    fetch(event.request)
      .then((response) => {
        if (response && response.status === 200 && response.type === 'basic') {
          const responseToCache = response.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseToCache);
          });
        }
        return response;
      })
      .catch(() => {
        return caches.match(event.request).then((cachedResponse) => {
          if (cachedResponse) {
            return cachedResponse;
          }
          if (event.request.mode === 'navigate') {
            return caches.match(OFFLINE_URL);
          }
        });
      })
  );
});
