# A Simple call like this should return a complete set of results, so it’s pretty safe to ignore
# the value associated with 'incomplete_results'. Assuming we were making complex 
# API calls, this program would check this value.




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
#print( response_dict.keys() )
print(" \n Total Python repositories on GitHub are:", response_dict['total_count'] )

#We then explore information about the repositories
repo_dicts = response_dict['items']
print( "\n Returned ", len(repo_dicts) ," Python repositories" )


#Automatically generating a description of all the python projects returned from the API call 
names, plot_dicts, = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    #Get a project description if one is available 
    description =  repo_dict['description']
    if not description:
        description = "No description about repo provided"

    plot_dict = {
        #Number of stars on the repo
        'value' : repo_dict['stargazers_count'],
        #Description of the repository
        'label' : description,
        #clickable link that will be added on the bar
        'xlink' : repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

#We now make the visualization 
my_style = LS('#646464', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

#Making custom configurations 
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar( my_config, style=my_style)
chart.title = "Most-Starred Python Projects on Git-Hub"
chart.x_labels = names


chart.add('',plot_dicts)
chart.render_to_file("python_repos_GitHub.svg")
# chart.render_to_file("python_repositories_GitHub.svg")
