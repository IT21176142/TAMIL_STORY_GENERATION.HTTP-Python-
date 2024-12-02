# import streamlit as st
# import json
# import requests

# st.title("Tamil Story Generator")


# story_title = st.text_input("Enter a Tamil Story Title")


# if story_title.strip() != "":
#     inputs = {
#         "user": 290,
#         "text": story_title
#     }


# if st.button("Generate Story"):
#     try:

#         response = requests.post(
#             url="http://localhost:8000/generate/story/tamil",
#             data=json.dumps(inputs),
#             headers={"Content-Type": "application/json"}
#         )

 
#         if response.status_code == 200:
#             response_data = response.json()
#             if response_data["result"]:
#                 story_heading = response_data["result"]["heading"]
#                 story_content = response_data["result"]["story"]
#                 st.subheader(f"Story: {story_heading}")
#                 st.write(story_content)
#             else:
#                 st.error("Story generation failed. Try again.")
#         else:
#             st.error(f"Request failed with status: {response.status_code}")

#     except Exception as e:
#         st.error(f"An error occurred: {e}")

# else:
#     st.write("Enter a story title and click 'Generate Story' to proceed.")


import streamlit as st
import json
import requests

st.title("Tamil Story Generator")

# Input for user story title
story_title = st.text_input("Enter a Tamil Story Title")

# Initialize a placeholder for the button to control its state
button_placeholder = st.empty()

# Initialize a variable to control the button state
button_disabled = False

# Function to make the API call and display result
def generate_story():
    global button_disabled
    button_disabled = True  # Disable button during API call
    if story_title.strip() != "":
        # Show spinner to indicate processing
        with st.spinner("Generating story..."):
            inputs = {
                "user": 290,
                "text": story_title
            }
            try:
                response = requests.post(
                    url="http://localhost:8000/generate/story/tamil",
                    data=json.dumps(inputs),
                    headers={"Content-Type": "application/json"}
                )

                if response.status_code == 200:
                    response_data = response.json()
                    if response_data["result"]:
                        story_heading = response_data["result"]["heading"]
                        story_content = response_data["result"]["story"]
                        st.subheader(f"Story: {story_heading}")
                        st.write(story_content)
                    else:
                        st.error("Story generation failed. Try again.")
                else:
                    st.error(f"Request failed with status: {response.status_code}")

            except Exception as e:
                st.error(f"An error occurred: {e}")
            finally:
                button_disabled = False  # Re-enable button after API call

# Render button and control its click behavior
if button_placeholder.button("Generate Story", disabled=button_disabled):
    generate_story()