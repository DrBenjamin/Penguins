##### `streamlit_app.py`
##### Penguins data visualisation example
#### Loading needed Python libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



#### Main program
### Title
st.title("Palmer's Penguins")
st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')

## Ask for data
penguin_file = st.file_uploader('Select Your Local Penguins CSV File')
if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    st.stop()

## User selection
selected_x_var = st.selectbox('What do you want the x variable to be?', ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('What about y?', ['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm', 'body_mass_g'])

## Filter NAs
x = penguins_df[selected_x_var].fillna(method = 'ffill')
y = penguins_df[selected_y_var].fillna(method = 'ffill')

## Plotting
# Color tweaks
sns.set_style('darkgrid')
sns.set(style = "ticks", context = "talk")
plt.style.use("dark_background")
# Setting plot
fig, ax = plt.subplots()
markers = {
    'Adelie': 'X',
    'Gentoo': 's',
    'Chinstrap': 'o'
}

ax = sns.scatterplot(data = penguins_df, x = x, y = y, hue = 'species', markers = markers, style = 'species')
plt.title('Scatterplot of Palmers Penguins', fontsize = 18, color = 'orange')
plt.xlabel(selected_x_var, fontsize = 14, color = 'orange')
plt.ylabel(selected_y_var, fontsize = 14, color = 'orange')
plt.title("Scatterplot of Palmer's Penguins")
st.pyplot(fig)

