import requests

def get_user_data(access_token):
    # Define the endpoint for retrieving user data
    endpoint = "https://graph.facebook.com/v13.0/me"

    # Set up parameters, including the access token
    params = {
        'fields': 'id,name,email',  # Customize fields as per your needs
        'access_token': access_token
    }

    # Make the API request
    response = requests.get(endpoint, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        user_data = response.json()
        print("User Data:")
        print(user_data)
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Replace 'YOUR_ACCESS_TOKEN' with the actual access token
access_token = 'EAAMfjIfBfWsBO4fJ5FQeYMk3R78PZAs5NgUn6nJDNIDX5x101ZBukCJdA60qyyggBnbUCITDVvZA3sXenGU5KRX3oQ5Ltmd7C9fq1KclqrJDqX44RzcauveYEw2aQ53L4nTI0EpeS7tvK6ZBmKLzYq1ZAiBkOjLwjoJ1aEX3OHmGkpIKHx4oWZBvfcCe4YtKAHcN94RTZAUF8JtwYYNCQZDZD'
get_user_data(access_token)
