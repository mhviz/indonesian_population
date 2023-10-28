import pickle
import streamlit as st

st.title("Testing App")
st.write("Indonesian Population Prediction")

# load the trained model
model = pickle.load(open('model/indonesian_population_model.pkl', 'rb') )

 
@st.cache_data()
def prediction(year: int):
    result = int(model.predict([[year]]))
    return result

def main():       
    Year = st.number_input('Year',min_value=1950, format='%d')
    if st.button("Predict"): 
        result = prediction(Year) 
        st.success(f'Indonesian Population in {Year} is: {result}')
        print(Year)

if __name__=='__main__': 
    main()