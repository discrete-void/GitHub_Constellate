import requests


#We make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print( "Status: ", r.status_code )

#We store the response from the API in a variable 
response_dict = r.json()

#We now process the results 
print( response_dict.keys() )

# A Simple call like this should return a complete set of results, so it’s pretty safe to ignore
# the value associated with 'incomplete_results'. Assuming we were making complex 
# API calls, this program would check this value.