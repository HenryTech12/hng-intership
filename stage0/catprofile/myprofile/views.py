from django.shortcuts import render
import requests
from django.http import JsonResponse
from datetime import datetime, timezone
import logging

#CONFIGURATION
logging.basicConfig(level=logging.INFO)

# Create your views here.

def fetchMe(request):
  url = 'https://catfact.ninja/fact'
  response = None
  #verify if user is calling a GET request
  if request.method == "GET":
    try:
      #fetch fact from CAT FACT API
      response = requests.get(url, timeout=(3,10))
      logging.info("fetching data from cat facts api")
      response.raise_for_status()
      fact_data = response.json()
      logging.info(f"extracted data: {fact_data}")
      #check if request is successful
      if response.status_code == 200:
        #get timestamp for every request using ISO 8601 format
        utc_time = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
        print(utc_time)
        logging.info("updates timestamp for every request ")
        data = {
          "status":"success",
          "user": {
                  "email": "fakorodehenry@gmail.com",
                  "name": "Fakorode Odunayo Henry",
                  "stack": "Python/Django"
          },
          "timestamp": utc_time,
          "fact": fact_data.get("fact", "No Data Found")
        }
        return JsonResponse(data)
    #handles exceptions with corresponding status code
    except requests.Timeout:
      r_code = 500 if response is None else response.status_code
      error = {
        "message": "the request timed out",
        "status": r_code
      }
      logging.error(f"an error occurred: {error}")
      return JsonResponse(error)
    except requests.RequestException as e:
      fallback_fact = "Could not fetch cat fact at the moment. Please try again later."
      r_code = 500 if response is None else response.status_code
      error =  {
          "status": r_code,
          "error": fallback_fact,
      }
      logging.error(f"an error occurred: {fallback_fact}")
      print(e)
      return JsonResponse(error)
    except Exception as ex:
      print(ex)
      r_code = 500 if response is None else response.status_code
      error = {
        "status": r_code,
        "message": "an error occurred!!!",
        "error": str(ex)
      }
      logging.error(f"an error occurred: {str(ex)}")
      return JsonResponse(error)
  else:
    #returns invalid response for post requests
    error = {
      "message": "POST request not supported",
               "status": 500
    }
    logging.error(error.message)
    return JsonResponse(error)