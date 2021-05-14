import os
import sentry_sdk

version = os.environ.get('GITHUB_SHA', '14.0.0')

sentry_sdk.init(dsn='https://39529b924487415380f43acf9a7d2335@o49697.ingest.sentry.io/5765882', release=version)

def try_oncemore(text):
  # not a thing
  total = os.environ
  version = os.environ.get('$GITHUB_SHA')
  text.enlarge()
  

try: 
   try_oncemore('meep')
except Exception as err:
   sentry_sdk.capture_exception(err)