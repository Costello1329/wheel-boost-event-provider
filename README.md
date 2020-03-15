# WheelBoostEventProvider
An event provider for WheelBoostBackend module, that parses .csv files and sends request to add event to backend’s database.

### How to use:
Run this command `python3 provider.py __path__ __host__ __api_url__`, where `__path__` is the path to your .xlsx file with data, and `__host__` is the WheelBoostBackend API instance, `__api_url__`,if path to api service 
### Example
python provider.py test.xlsx localhost:8000 /add_events 
test.xlsx - .xlsx file with data 
localhost:8000 - is the WheelBoostBackend API instance 
/add_events - path to api service 
test xlsx 
https://docs.google.com/spreadsheets/d/1TYtZiLMBaWD6kPOSND_QFoaylEJhQQUbfJL-QSeIwBQ/edit?usp=sharing 
