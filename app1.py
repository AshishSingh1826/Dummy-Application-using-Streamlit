import streamlit as st

st.title('Title -> Hello World!!')
st.header('Header -> Hello World!!')
st.subheader('Subheader -> Hello World!!')
st.text('Text -> Hello World!!')

st.markdown('# Hi')
# st.markdown('## Hi')
# st.markdown('### Hi')
# st.markdown('#### Hi')
# st.markdown('##### Hi')

st.markdown('Hi')

st.success('Success!')
st.info('Information!')
st.warning('Warning!')
st.error('Error!')

st.exception(ZeroDivisionError('Divison not possible with zero'))

st.help(ZeroDivisionError)

st.write('range(1,10)')
st.write(range(1,10))
st.write('1+2+3')
st.write(1+2+3)

st.code('num = 11 \n'
'# If given number is greater than 1 \n'
'if num > 1: \n'
'    # Iterate from 2 to n / 2 \n'
'    for i in range(2, int(num/2)+1): \n'
'        # If num is divisible by any number between \n'
'        # 2 and n / 2, it is not prime \n'
'        if (num % i) == 0: \n'
'            print(num, "is not a prime number") \n'
'            break \n'
'    else: \n'
'        print(num, "is a prime number") \n'
'else: \n'
'    print(num, "is not a prime number") \n')

male=st.checkbox("Male",help="For male it is 20%% discount")
female=st.checkbox("Female",help="For female it is 50%% discount")

if(male):
    st.write("Male option is chosen")
elif(female):
    st.write("Female option is chosen")

radioButton=st.radio("Select : ",("Male","Female","Other"))
if(radioButton=="Male"):
    st.write("You're a male")
elif(radioButton=="Female"):
    st.write("Yo're a female")
elif(radioButton=="Other"):
    st.write("You're an other gender")

selectBox =  st.selectbox("Data Science : ", [  'Data Analsis', 'Web Scraping','Machine Learning',
                                                'Deep Learning','Natural Language Processing',
                                                'Computer Vision','Image Processing'])
st.write("You've selected : ", selectBox)

multiSelect=st.multiselect("Data Science : ", [  'Data Analsis', 'Web Scraping','Machine Learning',
                                                'Deep Learning','Natural Language Processing',
                                                'Computer Vision','Image Processing'])

st.write("You've selected : ", len(multiSelect), "couses")

button=st.button("Click me")
if(button):
    st.write("Hello There")

# to link a webpage 
url = 'https://www.wikipedia.org/'

st.markdown(f'''
<a href={url}><button style="background-color:white;">Wikipedia</button></a>
''',
unsafe_allow_html=True)

level=st.slider('Select the level ', 0, 100, step=1)
st.write("Currently the level is : ", level)

input=st.text_input('Name : ')
if(input):
    st.write('Hii, ',input)

username=st.text_input('Username : ')
password=st.text_input('Password : ', type='password')

textArea=st.text_area('Write your Address : ', max_chars=10)
st.write(textArea)

st.number_input('Select your age : ', 18,50)
st.date_input("Date of birth : ")
st.time_input('Time : ')