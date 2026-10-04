import streamlit as st


  
st.write('Welcome to the QUIZ Zone....\n')

st.write('Q1. WHat is the first alphabet of English?  \na.B    \nb.Y  \nc.A    \nd.E\n')
ans1 = st.text_input("enter your choice1....")
st.write('Q2. Who is theNational Animal of INdia?  \na.Bear    \nb.Giraffe   \nc.Lion     \nd.Tiger\n')
ans2 = st.text_input("enter your choice2....")
st.write('Q3. Who is the National Bird of INdia?  \na.Peacock    \nb.Nightingale    \nc.Hen       \nd.Crow\n')
ans3 = st.text_input("enter your choice3....")
st.write('Q4. HOw many COntinents are there in world?  \na.4     \nb.12    \nc.7     \nd.9\n')
ans4 = st.text_input("enter your choice4....")
st.write("which team won the 2026 fifa wc?    \na.England      \nb.argentina     \nc.germany     \nd.spain\n")
ans5 = st.text_input("enter your choice5....")
st.write("how many oceans are in the world?   \na.7     \nb.3      \nc.4      \nd.5\n")
ans6 = st.text_input("enter your choice6....")
st.write("which is the biggest ocean in the world  \na.antarctic     \nb.pacific     \nc.arctic     \nd.atlantic\n")
ans7 = st.text_input("enter your choice7....")
st.write("which is the biggest country in the world  \na.USA     \n\b.Australia     \nc.russia     \nd.canada\n")
ans8 = st.text_input("enter your choice8....")
st.write("Which is the largest continent in the world  \na.Europe     \n\b.Audtralia     \nc.Asia     \nd.Africa\n")
ans9 = st.text_input("enter your choice9....")
st.write("which is ths largest state India by area  \na.Maharashtra      \nb.Uttar pradesh     \nc.Rajasthan     \nd.Madhya Pradesh")
ans10 = st.text_input("enter your choice10....")

total = 0

if ans1 == 'c' or ans1 == 'C':
  total+= 5
else:
  total-=2
if ans2 == 'd' or ans2 == 'D':
  total+= 5
else:
  total-=2
if ans3 == 'A' or ans3 == 'a':
  total+= 5
else:
  total-=2
if ans4 == 'c' or ans4 == 'C':
  total+= 5
else:
  total-=2
if ans5 == "d" or ans5 == "D":
  total+=5
else:
  total-=2
if ans6 == "d" or ans6 == "D":
  total+=5
else:
  total-=2
if ans7 == "b" or ans7 == "B":
  total+=5
else:
  total-=2
if ans8 == "c" or ans8 == "C":
  total+=5
else:
  total-=2
if ans9 == "c" or ans9 == "C":
  total+=5
else:
  total-=2
if ans10 == "c" or ans10 == "C":
  total+=5
else:
  total-=2
st.write(total)

if total <= 50 and total > 45:
  st.write('Congratulations... you have got 1st position')
  st.ballons
elif total <= 45 and total > 40:
  st.write('Congratulations... you have got 2nd position')
elif total <=40  and total > 30 :
  st.write('you have successfully passed the quiz with average score of 10...')
else:
  st.write('Better Luck next time...')


  
