import streamlit as st
import pandas as pd
import numpy as np
from helper import list_of_selected_locations, locations_list

st.title("Bangalore House Price Prediction")

st.markdown(
    """
This app predicts the **Bangalore House Price**!
"""
)
st.sidebar.header("User Input Features")


# list_of_selected_features = ['Area',
#  'No. of Bedrooms',
#  'Resale',
#  'Gasconnection',
#  "Children'splayarea",
#  'LiftAvailable',
#  'Wardrobe',
#  'Price_per_sqft',
#  'Location_Anjanapura',
#  'Location_Attibele',
#  'Location_Avalahalli Off Sarjapur Road',
#  'Location_Banashankari',
#  'Location_Begur',
#  'Location_Bellandur',
#  'Location_Bommanahalli',
#  'Location_Bommasandra',
#  'Location_Budigere Cross',
#  'Location_Carmelaram',
#  'Location_Chandapura',
#  'Location_Devanahalli',
#  'Location_Electronic City Phase 1',
#  'Location_Electronic City Phase 2',
#  'Location_Gottigere',
#  'Location_Harlur',
#  'Location_Hebbal',
#  'Location_Hennur',
#  'Location_Horamavu',
#  'Location_Hosa Road',
#  'Location_ITPL',
#  'Location_JP Nagar Phase 1',
#  'Location_JP Nagar Phase 3',
#  'Location_JP Nagar Phase 4',
#  'Location_JP Nagar Phase 7',
#  'Location_JP Nagar Phase 8',
#  'Location_Jakkur',
#  'Location_Jalahalli',
#  'Location_Kadugodi',
#  'Location_Kalyan Nagar',
#  'Location_Kanakapura Road Beyond Nice Ring Road',
#  'Location_Kannur on Thanisandra Main Road',
#  'Location_Kasavanahalli',
#  'Location_Kengeri',
#  'Location_Konanakunte',
#  'Location_Krishnarajapura',
#  'Location_Kumaraswamy Layout',
#  'Location_Kumbalgodu',
#  'Location_Narayanapura on Hennur Main Road',
#  'Location_Nelamangala',
#  'Location_RR Nagar',
#  'Location_Rajajinagar',
#  'Location_Ramamurthy Nagar',
#  'Location_Richmond Town',
#  'Location_Sarjapur',
#  'Location_Sarjapur Road Wipro To Railway Crossing',
#  'Location_Subramanyapura',
#  'Location_Talaghattapura',
#  'Location_Thanisandra',
#  'Location_Uttarahalli',
#  'Location_Uttarahalli Main Road',
#  'Location_Varthur',
#  'Location_Whitefield Hope Farm Junction',
#  'Location_Yelahanka',
#  'Location_Yeshwantpur',
#  'Location_other',
#  'Location_sarjapura attibele road']


# Collects user input features into dataframe
def user_input_features():
    location = st.sidebar.selectbox(
        "Location",
        locations_list,
        index=0,
    )
    Area = st.sidebar.slider("Area", 100, 10000, 1000)
    No_of_Bedrooms = st.sidebar.slider("No. of Bedrooms", 1, 10, 2)
    Resale = st.sidebar.slider("Resale", 0, 1, 1)
    Gasconnection = st.sidebar.slider("Gasconnection", 0, 1, 1)
    Childrensplayarea = st.sidebar.slider("Children'splayarea", 0, 1, 1)
    LiftAvailable = st.sidebar.slider("LiftAvailable", 0, 1, 1)
    Wardrobe = st.sidebar.slider("Wardrobe", 0, 1, 1)
    Price_per_sqft = st.sidebar.slider("Price_per_sqft", 100, 10000, 1000)
    data = {
        "Area": Area,
        "No. of Bedrooms": No_of_Bedrooms,
        "Resale": Resale,
        "Gasconnection": Gasconnection,
        "Children'splayarea": Childrensplayarea,
        "LiftAvailable": LiftAvailable,
        "Wardrobe": Wardrobe,
        "Price_per_sqft": Price_per_sqft,
    }

    features = pd.DataFrame(data, index=[0])
    # crete location variable according to the selected location
    selected_location = "Location_" + location
    # features[selected_location] = 1

    for i in list_of_selected_locations:
        if i == selected_location:
            features[i] = 1
        else:
            features[i] = 0
    # create location variable for other location

    # features = pd.DataFrame(data, index=[0])
    return features , location


df , location = user_input_features()

st.subheader("User Input parameters")
# st.write(
#     """
#     The user input parameters are:
#     """
# )
# st.write(
#     """
    
#     Area: **{}** sqft
#     """.format(
#         df["Area"].values[0]
#     )

# )
# st.write(
#     """
    
#     No. of Bedrooms: **{}**
#     """.format(
#         df["No. of Bedrooms"].values[0]
#     )

# )
# st.write(
#     """
    
#     Resale: **{}**
#     """.format(
#         df["Resale"].values[0]
#     )

# )
# st.write(
#     """
    
#     Gasconnection: **{}**
#     """.format(
#         df["Gasconnection"].values[0]
#     )

# )
# st.write(
#     """
    
#     Children'splayarea: **{}**
#     """.format(
#         df["Children'splayarea"].values[0]
#     )

# )
# st.write(
#     """
    
#     LiftAvailable: **{}**
#     """.format(
#         df["LiftAvailable"].values[0]
#     )

# )
# st.write(
#     """
    
#     Wardrobe: **{}**
#     """.format(
#         df["Wardrobe"].values[0]
#     )

# )

# st.write(
#     """
    
#     Price_per_sqft: **{}**
#     """.format(
#         df["Price_per_sqft"].values[0]
#     )

# )

# st.write(
#     """
    
#     Location: **{}**
#     """.format(
#        location
#     )

# )

user_input = {
    "Area": df["Area"].values[0],
    "No. of Bedrooms": df["No. of Bedrooms"].values[0],
    "Resale": df["Resale"].values[0],
    "Gasconnection": df["Gasconnection"].values[0],
    "Children'splayarea": df["Children'splayarea"].values[0],
    "LiftAvailable": df["LiftAvailable"].values[0],
    "Wardrobe": df["Wardrobe"].values[0],
    "Price_per_sqft": df["Price_per_sqft"].values[0],
    "Location": location
}

# Creating a Markdown table using st.write
st.write(
    "| Parameter | Value |" + "\n" +
    "| :--- | :--- |" + "\n" +
    "\n".join(f"| {key} | **{value}** |" for key, value in user_input.items())
)
# Reads in saved classification model
import pickle

load_clf = pickle.load(open("bangalore_house_price_model.pkl", "rb"))

# Apply model to make predictions
prediction = load_clf.predict(df)


st.subheader("Prediction")
st.write(
    """
    The predicted price of the house is **₹ {:.2f} Lakhs**.
    """
    .format(prediction[0]/100000)

)
