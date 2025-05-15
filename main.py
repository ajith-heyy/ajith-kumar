import streamlit as ak
from streamlit_option_menu import option_menu


#for side bar:
with ak.sidebar:
    select=option_menu(
        menu_title="INTERNSHIP",
        options=["COMPANY📈","ABOUT","PROJECTS"],
        icons=["book","file-person","telephone"]
    )
    
if select=="COMPANY📈":
    ak.title("🔥VINSUP INFO-TECH🔥")
    ak.header("Seamless Solutions for a Digital World")
    ak.write("Innovate | Automate | Elevate")
    col1, col2 = ak.columns(2)
    with col2:
        ak.image("https://vinsupinfotech.com/assets/img/about/v1/big-img.jpg")
    with col1:
        ak.image("https://vinsupinfotech.com/assets/img/about/v1/small-img.jpg")
    ak.header("At Vinsup Infotech, we don’t just build software—we create experiences that drive success. Let’s shape the future, together.")
    ak.write("***")
    col1,col2,col3=ak.columns(3)
    with col2:
        ak.write("INDUSTRIES")
    ak.header("TAILOR MADE SOLUTION DESIGNED SPECIFICALLY FOR YOUR INDUSTRY")
    col1,col2=ak.columns(2)
    with col1:
        ak.image("https://vinsupinfotech.com/assets/img/service/v1/education.jpg",ak.write("Education & E-Learning"))
        ak.button("Learn more ➤")

    with col2:
        ak.image("https://vinsupinfotech.com/assets/img/service/v1/healthcare.jpg",ak.write("Healthcare & Medical"))
        ak.button("Learn More ➤")

elif(select=="about"):
    ak.title("abbb")
elif(select=="contact"):
    ak.title("contactt")










# #text elements:

# ak.title("VINSUP INFOTECH")
# ak.header("VINSUP INFOTECH")
# ak.subheader("VINSUP INFOTECH")
# ak.text("VINSUP INFOTECH")
# ak.write("VINSUP INFOTECH")

# #badge tag--> it make square on given text eg:
# ak.badge("hello",color="red")

# #metric tag--> it shows ups and downs diffrence in color eg:
# ak.metric("age","18","20")  #age--> name, "18"--> limit, "20"-->actual value. if the actual value less means red if not it is green

# #latex tag--> this tag change the text into formula tag eg:
# ak.latex("l*b*h")

# #code tag---> it shows our code with colorfull font and copy paste options like(chat gpt) eg:
# ak.code(""" 
#         a=10
#         b=20
#         c=a+b
#         print(c)""",language="python")

# #printing tag---> with variable op and without varible.
# #with out variable op shows "(give insider)",
# #with variable op shows we can use further implementations. code:"ak.write(a)"
# a=ak.text_input("enter the name")
# #for variable run code
# ak.write(a)

# #input tags:
# ak.text_input("enter the name:") #it recieve the input in string format
# ak.number_input("enter the age:",max_value=0) #it only recieve only int format
# ak.selectbox("gender:",["male","female"]) #this tag use to select 1 option itself
# ak.multiselect("skills:",["py","c","c++","java"]) #this tag helps to choose more options
# ak.radio("state",["tn","kl","bgnlr"])
# ak.checkbox("agree to terms and condition")
# ak.button("submit")
# ak.button("click")

# #for coloumn:
# col1,col2=ak.columns(2)

# with col1:
#     ak.text_input("username:")
#     ak.image("https://images.pexels.com/photos/3052361/pexels-photo-3052361.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2")
# with col2:
#     ak.text_input("password")



