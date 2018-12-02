import requests


#We make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print( " \n Status: ", r.status_code )
#We store the response from the API in a variable 
response_dict = r.json()

#We now process the results 
print( response_dict.keys() )
print(" \n Total Python repositories on GitHub are:", response_dict['total_count'] )

#We then explore information about the repositories
repo_dicts = response_dict['items']
print( "\n Returned ", len(repo_dicts) ," Python repositories" )

#Examine the first repository
#repo_dict = repo_dicts[0]
#print(" \nKeys:", len(repo_dict))
#for key in sorted(repo_dict.keys()):
#    print(key)

#We then print selected information about each repostiory
print("\nSelected information about first repository:")
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
 
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])



# A Simple call like this should return a complete set of results, so it’s pretty safe to ignore
# the value associated with 'incomplete_results'. Assuming we were making complex 
# API calls, this program would check this value.


