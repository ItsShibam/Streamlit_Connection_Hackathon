import streamlit as st
import requests
from streamlit.connections import ExperimentalBaseConnection


class GitConnection(ExperimentalBaseConnection[requests.Session]):

    def __init__(self, connection_name: str, **kwargs):
        super().__init__(connection_name, **kwargs)
        self._resource = self._connect()
    def _connect(self) -> requests.Session:
        return requests.Session()
    def cursor(self):
        return self._resource
    def query(self, _id, ttl: int = 3600):
        _base_url = "https://api.github.com/"
        # def image_card(user,follower,repos):

        def get_user_data(username):
            url = f"{_base_url}users/{username}"
            response = self._resource.get(url)
            # print(response.json())
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                # st.error("Failed to fetch data from the API")
                return None

        def get_user_repos(username):
            url = f"{_base_url}users/{username}/repos"
            response = self._resource.get(url)
            # print(response.json())
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                # st.error("Failed to fetch data from the API")
                return None

        def get_user_followers(username):
            url = f"{_base_url}users/{username}/followers"
            response = self._resource.get(url)
            # print(response.json())
            if response.status_code == 200:
                data = response.json()
                print(len(data))
                return data
            else:
                # st.error("Are you a fuck up guy")
                return None
        return get_user_data(_id), get_user_followers(_id), get_user_repos(_id)


def main():
    st.title('Custom connection Streamlit hackathon submission')
    st.markdown('Developed by Shibam Ku. Patra')
    name = st.text_input('Enter your github username')
    gitconnection = GitConnection('githubapi')
    if(st.button('Get Info')):
        if not name:
            return

        # Image and link URLs
        # image_url = "https://example.com/image.png"
        # link_url = "https://example.com/destination"
        
        user, follower, repos = gitconnection.query(name)
        if user is None or follower is None or repos is None:
            st.error("You forgot your username. Try again")
            return
        if user is not None:
            st.image(user['avatar_url'], width=300)  # Display the image with a width of 300 pixels
            st.header("Name")
            st.write(user['name'])
            st.header("Followers")
            st.write(len(follower))
                    
            st.header("Repositories ");
            for i in repos:
                st.write(i['name'])
        # Display the card


if __name__ == "__main__":
    main()

# def main():
    # st.title('Welcome to Streamlit')
    # name = st.text_input('Enter your name')
    # st.write(f'Hello, {name}!')

# if __name__ == '__main__':
#     main()


# def get_api_data():
#     url = "https://jsonplaceholder.typicode.com/users"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         return data
#     else:
#         st.error("Failed to fetch data from the API")
#         return None

# data = get_api_data()
# if data is not None:
#     st.table(data)




