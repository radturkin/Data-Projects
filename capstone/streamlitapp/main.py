import streamlit as st
import streamlit as st
import pandas as pd
import pickle
import lightgbm
import sklearn
from transformers import AutoTokenizer, AutoModelForCausalLM
from arctic import Arctic, ArcticSeqCLM



# token = "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"
# model = ArcticSeqCLM(token=token)

st.title("What is your weightclass?")

text = """
fill out the form below

"""

st.write(text)
user_age=st.slider("How old are you?", 10,110 )
user_weight=st.slider("How much do you weigh in kgs", 10, 500)
user_height=st.slider("How tall are you in meters", 1.0,2.5 )
user_fam_hist=st.toggle("family member is or was overweight?")

user_gender=st.selectbox("whats your bodies primary hormone?", ['0 estrogen', '1 testosterone'])

user_highcal=st.toggle("Frequent consumption of high caloric food?")

user_veg=st.selectbox("Do you usually eat vegetables in your meals?", ["1 never", "2 sometimes", "3 always"])

user_meals=st.slider("How many main meals do you have daily?",1,4)


user_snack=st.selectbox("Do you eat any food between meals?",["No", "Sometimes", "Frequently", "Always"])

user_smoke=st.toggle("Do you smoke?")

user_water=st.slider("How many liters of water do you drink daily?",1.0,3.0)

user_cal=st.toggle("Do you monitor the calories you eat daily?")

user_phys=st.selectbox("How often do you have physical activity?",["0","1 or 2 days","2 or 4 days", "4 or 5 days"])

user_tech=st.selectbox("How much time do you use technological devices such as cell phone, videogames, television, computer and others?",["0–2 hours","3–5 hours","5 or more hours"])

user_drink=st.selectbox("how often do you drink alcohol?",['Never', 'Sometimes', 'Frequently', 'Always'])

user_trans=st.selectbox("Which transportation do you usually use?",['Automobile','Motorbike','Bike','Public Transportation','Walking'])

print(user_trans)
vals=[user_age, user_height,user_weight, user_highcal, user_meals, user_water, ]
columns=['Age', 'Height', 'Weight', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE',
   'Gender_Male', 'family_history_with_overweight_yes', 'FAVC_yes',
   'CAEC_Frequently', 'CAEC_Sometimes', 'CAEC_no', 'SMOKE_yes', 'SCC_yes',
   'CALC_Frequently', 'CALC_Sometimes', 'CALC_no', 'MTRANS_Bike',
   'MTRANS_Motorbike', 'MTRANS_Public_Transportation', 'MTRANS_Walking']
df_dict={
}
df_dict["Age"]=user_age
df_dict['Height']=user_height
df_dict["Weight"]=user_weight
df_dict["FCVC"]=int((str(user_veg)[:1]))
df_dict["NCP"]=user_meals
df_dict["CH20"]=user_water
faf=int(str(user_phys)[:1])
if faf<4:
  df_dict["FAF"]=faf
else:
  df_dict["FAF"]=3

tue=int(str(user_tech)[:1])//2

df_dict["TUE"]=tue

df_dict["Gender_Male"]=int(str(user_gender)[:1])

df_dict['family_history_with_overweight_yes']=int(user_fam_hist)
df_dict['FAVC_yes']=int(user_highcal)

df_dict['CAEC_Frequently']=0
df_dict['CAEC_Sometimes']=0 
df_dict['CAEC_no']=0
if user_snack=="Sometimes":
  df_dict['CAEC_Sometimes']=1
if user_snack=='Frequently':
  df_dict['CAEC_Frequently']=1
if user_snack=="No":
  df_dict['CAEC_no']=1
df_dict['SMOKE_yes']=int(user_smoke)
df_dict['SCC_yes']=int(user_cal)

df_dict['CALC_Frequently']=0
df_dict['CALC_Sometimes']=0
df_dict['CALC_no']=0
if user_drink=="Sometimes":
  df_dict['CALC_Sometimes']=1
if user_drink=='Frequently':
  df_dict['CALC_Frequently']=1
if user_drink=="Never":
  df_dict['CALC_no']=1

df_dict['MTRANS_Bike']=0
df_dict['MTRANS_Motorbike']=0
df_dict['MTRANS_Public_Transportation']=0
df_dict['MTRANS_Walking']=0

if user_trans=="Bike":
  df_dict['MTRANS_Bike']=1
if user_trans=='Motorbike':
  df_dict['MTRANS_Motorbike']=1
if user_trans=="Public Transportation":
  df_dict['MTRANS_Public_Transportation']=1
if user_trans=="Walking":
  df_dict['MTRANS_Walking']=1
  
print(df_dict)

df=pd.DataFrame(df_dict, index=[0])

with open('lgbm_model.pkl', 'rb') as file:
  loaded_model = pickle.load(file)
results=loaded_model.predict(df)
print(results)

# text = """
# fill out the form below

# """

st.write(f"your weight class is: {results[0]}")

tokenizer = AutoTokenizer.from_pretrained("Snowflake/Arctic-seq-clm")
model = AutoModelForCausalLM.from_pretrained("Snowflake/Arctic-seq-clm")

# Define a function to generate text based on user input
def generate_text(prompt, max_length=100):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=max_length)
    return tokenizer.decode(outputs[0])

# # Create a Streamlit app interface
# st.title("Arctic Chatbot")
# user_input = st.text_input("Enter your message:", value="Hello, Arctic!")
# if st.button("Send"):
#     generated_text = generate_text(user_input)
#     st.write("Arctic: " + generated_text)