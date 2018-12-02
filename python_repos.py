import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

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


names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#We now make the visualization 
my_style = LS('#333366', base_style=LCS)
#Making custom configurations 
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar( style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "Most-Starred Python Projects on Git-Hub"
chart.x_labels = names

chart.add('',stars)
chart.render_to_file("python_repos_GitHub.svg")




#Examine the first repository
#repo_dict = repo_dicts[0]
#print(" \nKeys:", len(repo_dict))
#for key in sorted(repo_dict.keys()):
#    print(key)

#We then print selected information about each repostiory
print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
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


