import streamlit as st


  
st.write('Welcome to the QUIZ Zone....\n')

st.write('Q1. WHat is the first alphabet of English? \na.B    b.Y\nc.A    d.E\n')
ans1 = st.input("enter your choice....")
st.write('Q2. Who is theNational Animal of INdia? \na.Bear    b.Giraffe  \nc.Lion    d.Tiger\n')
ans2 = st.input("enter your choice....")
st.write('Q3. Who is the National Bird of INdia? \na.Peacock    b.Nightingale   \nc.Hen        d.Crow\n')
ans3 = st.input("enter your choice....")
st.write('Q4. HOw many COntinents are there in world? \na.4    b.12   \nc.7    d.9\n')
ans4 = st.input("enter your choice....")
st.write("which team won the 2026 fifa wc? \na.England     b.argentina    \nc.germany    d.spain\n")
ans5 = st.input("enter your choice....")
st.write("how many oceans are in the world? \na.7    b.3    \nc.4     d.5\n")
ans6 = st.input("enter your choice....")
st.write("which is the biggest ocean in the world \na.antarctic    b.pacific    \nc.arctic    d.atlantic\n")
ans7 = st.input("enter your choice....")
st.write("which is the biggest country in the world \na.USA    \b.Australia    \nc.russia    d.canada\n")
ans8 = st.input("enter your choice....")
st.write("Which is the largest continent in the world \na.Europe    \b.Audtralia    \nc.Asia    d.Africa\n")
ans9 = st.input("enter your choice....")
st.write("which is ths largest state India by area \na.Maharashtra     b.Uttar pradesh    \nc.Rajasthan    d.Madhya Pradesh")
ans10 = st.input("enter your choice....")

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
elif total <= 45 and total > 40:
  st.write('Congratulations... you have got 2nd position')
elif total <=40  and total > 30 :
  st.write('you have successfully passed the quiz with average score of 10...')
else:
  st.write('Better Luck next time...')


  
