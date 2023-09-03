import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_extras.app_logo import add_logo
from streamlit_lottie import st_lottie
import requests

st.set_page_config(
  page_title = "Litter Locator",
  page_icon = "🌲",
  layout = "wide"
) 

add_logo("https://cdn.discordapp.com/attachments/534885876585725985/1147776610834071572/logo-removebg-preview.png")

def local_css(file_name):
  with open(file_name) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def load_lottieurl(url:str):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()

local_css("style.css")

lottie_garbage = load_lottieurl('https://lottie.host/d88a2a4f-05f7-49d2-8c26-a0218f1c68ac/JYZz4sGoye.json')

image1 = Image.open('introduction text.png')

with st.container():
  left, right = st.columns([1,1])
  with left:
    st.image(image1)
  with right:
    st_lottie(
      lottie_garbage,
      speed = 0.5,
      reverse = False,
      quality = 'medium',
      height=None,
      width=None,
      key=None
    )

st.title("About Litter Locator")
image2 = Image.open('climateaction.jpg')
st.write("Did you know that in the United States alone, an astonishing 51 billion pieces of litter are left on the ground every year? This shocking statistic highlights a pervasive issue that not only harms the environment but also degrades the way our communities are presented. After all, no one likes seeing a litter-ridden city. In response to this alarming problem, Litter Locator has emerged as a beacon of hope in the battle against litter.  Litter Locator is not just a website; it's a powerful tool for change. By harnessing the collective efforts of concerned citizens, it presents a novel approach to reducing litter. Anyone can use the platform to self-report large quantities of litter in their communities, pinpointing trouble spots that need urgent attention. What sets Litter Locator apart is its ingenious system of mobilizing teams of dedicated cleaners who access the reported locations on the website, swiftly locating and cleaning these litter-ridden areas.  This dynamic synergy between technology and community engagement not only helps to keep our surroundings clean but also fosters a sense of shared responsibility. Litter Locator isn't just cleaning up our streets; it's cleaning up our collective conscience. Join the movement and be a part of the solution. Together, we can make a world with less litter and more beauty.")

st.divider()

with st.container():
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("Our Mission")
    st.write("At Litter Locator, our overarching goal is to create cleaner, more beautiful, and environmentally responsible communities. We envision a world where litter is no longer a blight on our neighborhoods, parks, and public spaces, and where the idea of a cleaner environment is championed by individuals and communities alike. To achieve this goal, there are two ways in which Litter Locator helps. 1: People are able to report highly littered areas, and 2: people are able to find these areas.")
  with right_column:
    st.image(image2)
st.divider()

with st.container():
  left, right = st.columns([1,1])
  with left:
    with st.expander("How can I report high litter areas?"):
      st.write("In the reporting section of Litter Locator, we've made it incredibly easy for you to be the catalyst for change in your community. When you come across a littered area that needs attention, simply navigate to our user-friendly reporting interface. Here, you can upload the exact location using GPS coordinates. However, there's more to it. We know that a picture is worth a thousand words, which is why we encourage you to snap a photo of the littered area. These images provide crucial context, helping us understand the extent of the issue and allowing volunteers to prepare accordingly. With your location and photographic evidence, you're not just reporting a problem; you're providing a clear and actionable insight that empowers our community to come together and make a real impact.")

  with right:
    with st.expander("How can I find high litter areas near me?"):
      st.write("We believe that change requires a collective effort. After a littered area has been reported on our Litter Locator website, the process of finding and addressing the litter becomes a community-driven effort. Once a report is submitted, it is immediately added to our interactive map, pinpointing the exact location for all users to see. Community members, volunteers, and concerned citizens can then take action by referring to the map, selecting a reported area that resonates with them, and organizing clean-up efforts. Our platform serves as a vital communication hub, connecting those who care with the specific areas in need of attention, ensuring that the response to litter reports is swift and effective. Together, we turn reports into action, making a lasting impact on the cleanliness and beauty of our communities.")
