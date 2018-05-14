import plotly.plotly as py
import plotly.graph_objs as go
from pymongo import MongoClient
import sys
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
from networkx.algorithms import approximation as approx
from nxpd import draw
from networkx.drawing.nx_agraph import graphviz_layout
client = MongoClient()
client = MongoClient('mongodb://m49dy:admin12345@ds251799.mlab.com:51799/sna_project')
db = client['sna_project']
userCollection = db['users']
groupCollection = db['groups']
postCollection=db['posts']
array_users = list(userCollection.find())
array_groups = list(groupCollection.find())
print(array_users[0])
names=[]
no_of_friends=[]
no_of_posts=[]
group_names=[]
users_groups=[]
posts=[]
use=[]
males=0
females=0
group_posts=[]
print(list(postCollection.find())[0]["group"])
for user in array_users:
    names.append(user["name"])
    no_of_friends.append(len(user["friends"]))
    no_of_posts.append(len(user["posts"]))
    if 'gender'  in user:
        if(user["gender"]==1):
            males=males+1
        else:
            females=females+1
for group in array_groups:
    group_names.append(group["name"])
    users_groups.append(len(group["users"]))
for group in array_groups:
    no=0
    for post in list(postCollection.find()):
        if 'group' in post:
            if post["group"]==group["_id"]:
                no=no+1
    group_posts.append(no)
   
# Replace the username, and API key with your credentials.
py.sign_in('diaa56', 'QaMy3cKad5uFqnLP8oaL')

trace = go.Bar(x=names, y= no_of_friends)
data = [trace]
 
layout=go.Layout(title = 'no of friends for each user', width = 800, height = 640,xaxis= dict(
        title='users',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis = dict(
        title='no of friends',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=data, layout=layout)

py.image.save_as(fig, filename='assets/a-simple-plot.png')
trace = go.Bar(x=names, y=no_of_posts)
data = [trace]

layout = go.Layout(title='no of posts for each user', width=800, height=640, xaxis=dict(
    title='users',
    titlefont=dict(
        family='Courier New, monospace',
        size=18,
        color='#7f7f7f'
    )
),
    yaxis=dict(
        title='no of posts',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
)
)
fig = go.Figure(data=data, layout=layout)

py.image.save_as(fig, filename='assets/posts.png')

trace = go.Bar(x=group_names, y=users_groups)
data = [trace]

layout = go.Layout(title='no of users for each group', width=800, height=640, xaxis=dict(
    title='groups',
    titlefont=dict(
        family='Courier New, monospace',
        size=18,
        color='#7f7f7f'
    )
),
    yaxis=dict(
        title='no of users',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
)
)
fig = go.Figure(data=data, layout=layout)

py.image.save_as(fig, filename='assets/groups.png')
trace = go.Bar(x=group_names, y=group_posts)
data = [trace]

layout = go.Layout(title='no of posts for each group', width=800, height=640, xaxis=dict(
    title='groups',
    titlefont=dict(
        family='Courier New, monospace',
        size=18,
        color='#7f7f7f'
    )
),
    yaxis=dict(
        title='no of posts',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
)
)
fig = go.Figure(data=data, layout=layout)

py.image.save_as(fig, filename='assets/groups_posts.png')


if len(sys.argv) > 1:
    target=sys.argv[1]
    print(sys.argv[1]) 
    gp = groupCollection.find_one( {"name":target})
    print(gp)
    G = nx.Graph()
    for user in gp["users"]:
        G.add_node(userCollection.find_one({"_id": user})["name"])
    for user in gp["users"]:
        data = userCollection.find_one({"_id": user})
        if 'friends' in data:
            for one in data["friends"]:
                if one in gp["users"]:
                    G.add_edge(data["name"], userCollection.find_one({"_id": one})["name"], color='grey')
    edges = G.edges()
    colors = [G[u][v]['color'] for u, v in edges]

    pos = nx.nx_pydot.graphviz_layout(G)


    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='red',font_size=18, node_size=0, edge_color=colors, width=5)

    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(20, 15)
    plt.savefig("assets/connect.png")
    if gp:
        print("lol")
        if 'users' in gp:
            for user in gp["users"]:
                no = 0
                us = userCollection.find_one({"_id": user})
                use.append(us["name"])
                for post in us["posts"]:
                    ps = postCollection.find_one({"_id": post})
                    if ps:
                        if 'group' in ps:
                            if(ps["group"] == gp["_id"]):
                                no = no + 1
                posts.append(no)
    trace = go.Bar(x=use, y=posts)
    data = [trace]

    layout = go.Layout(title='no of posts for each user in group '+target, width=800, height=640, xaxis=dict(
        title='users',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
        yaxis=dict(
            title='no of posts',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
    )
    )
    fig = go.Figure(data=data, layout=layout)

    py.image.save_as(fig, filename='assets/habd.png')

 


