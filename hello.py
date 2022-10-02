from fyers_api import fyersModel
from fyers_api import accessToken
import pandas as pd
import time
import xlwings as xw




redirect_uri= "https://deepak.fyers.in/"  ## redircet_uri you entered while creating APP.
client_id = "NVGZ7GTG72-100"                                          ## Client_id here refers to APP_ID of the created app
secret_key = "9HWJDPM8UT"                                           ## app_secret key which you got after creating the app 
grant_type = "authorization_code"                  ## The grant_type always has to be "authorization_code"
response_type = "code"                             ## The response_type always has to be "code"
state = "sample"                                   ##  The state field here acts as a session manager. you will be sent with the state field after successfull generation of auth_code 



 
appSession = accessToken.SessionModel(client_id = client_id, redirect_uri = redirect_uri,response_type=response_type,state=state,secret_key=secret_key,grant_type=grant_type)

### Make  a request to generate_authcode object this will return a login url which you need to open in your browser from where you can get the generated auth_code 
generateTokenUrl = appSession.generate_authcode()
generateTokenUrl


auth_code = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2NjQ2ODE1NjUsImV4cCI6MTY2NDcxMTU2NSwibmJmIjoxNjY0NjgwOTY1LCJhdWQiOiJbXCJkOjJcIiwgXCJkOjJcIiwgXCJkOjJcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYRDA3MTAwIiwibm9uY2UiOiIiLCJhcHBfaWQiOiJOVkdaN0dURzcyIiwidXVpZCI6IjA5MWI1MjMxM2E5MjQ5ZTFhOWJkMDYyM2FhNTJhNGQ3IiwiaXBBZGRyIjoiMC4wLjAuMCIsInNjb3BlIjoiIn0.DtjHkHlQ_z2Kod3QEMYvv_Y5eE6r5e5fJogb0SZIxLI"



appSession.set_token(auth_code)
response = appSession.generate_token()

response
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NjQ2ODE2MjcsImV4cCI6MTY2NTk2NjY0NywibmJmIjoxNjY0NjgxNjI3LCJhdWQiOlsiZDoyIiwiZDoyIiwiZDoyIl0sInN1YiI6InJlZnJlc2hfdG9rZW4iLCJhdF9oYXNoIjoiZ0FBQUFBQmpPUWFib3pGVllXd1JJa3gteXJ6OURVRXNKbHljTHN2VnlDNWowZ1lDaDQ3LTRPRmZud3hnWkVjUGFzYUhnN29fTW92alR6R1NzRlBEVmpWNklSRkZmUGY2QldYRWRhNmFuZHc1V2ZSZzM3aUtMbXc9IiwiZGlzcGxheV9uYW1lIjoiREVFUEFLIEJIQVRUIiwiZnlfaWQiOiJYRDA3MTAwIiwiYXBwVHlwZSI6MTAwLCJwb2FfZmxhZyI6Ik4ifQ.HaXZRH937Mvuu5bXfwYiNzY4pK38En5T0G-j9c_O7iU"
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token)
print(fyers)
while (True):
 data = {"symbol":"NSE:RELIANCE-EQ","resolution":"1","date_format":"0","range_from":"1664508915","range_to":"1664534115","cont_flag":"1"}
 ss=fyers.history(data)['candles']
 ss

 df = pd.DataFrame(data=ss,columns=['Date', 'Open','High','Close','Low','Volume'])
 df['Date'] =[ time.strftime("%Y-%m-%d, %H:%M:%S",time.localtime(float(x))) for x in df['Date']]

 df
 wb = xw.Book("loopdata.xlsx")
 st = wb.sheets("rel")
 st.range("A1").value =df
 time.sleep(1)









