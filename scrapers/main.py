import time
import os
from FirestoreHelper import FirestoreHelper
from RealtimeDbHelper import RealtimeDbHelper
from crawlers.runner import run as scrapy_run

firestore_helper = FirestoreHelper()
realtimedb_helper = RealtimeDbHelper()

def main():
  start_time = time.time()
  
  # Get stores in radius around Orillia
  lat = 44.58857
  lng = -79.415588
  radius = 75
  
  stores = firestore_helper.get_local_stores(lat, lng, radius)
  num_stores = len(stores)
  print(f'\nFound {num_stores} stores within {radius}km of {lat}, {lng}.\n')
  
  scrapy_run(stores)
  
  print(f'\nAll stores complete. Total time: {time.time() - start_time} seconds.')

  
if __name__ == '__main__':
  main()