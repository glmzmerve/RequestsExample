import requests
import json
#get
#user_input=input("enter id:")
#url=f"https://jsonplaceholder.typicode.com/todos/{user_input}"
#get_response=requests.get(url)
#print(get_response.json())
#post
to_do_item={"userId" :2,"title" : "my to do" , "completed":False}
post_url="https://jsonplaceholder.typicode.com/todos"
#optional header
headers={"Content-Type":"application/json"}
post_response=requests.post(post_url, data=json.dumps(to_do_item),headers=headers)
print(post_response.json())
#print(json.dumps(to_do_item))