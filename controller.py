from tkinter import *
from util import check_endpoint
from api import get_env_details, update_with_post
from filter import get_details_by_env

root = Tk()
root.configure(background="LightSteelBlue1")
root.geometry('800x800+450+100')
root.title("ENDPOINT CHANGER")
KeyName = StringVar()
Environment = StringVar()
CurrentStatus = StringVar()
prod_pesudo = IntVar()



def check_data():
    prod_pesudo_value = ""
    keynames = get_value()
    Envvalue = Environment.get()
    prod_pesudo = var.get()
    if(prod_pesudo == 1):
        prod_pesudo_value = "prod"
    if(prod_pesudo == 2):
        prod_pesudo_value = "pesudo"

    for keyname in keynames: 
        app_details, key_name = get_env_details(keyname, Envvalue, keyname, prod_pesudo_value)
        app_ids_to_post = get_details_by_env(app_details, Envvalue)
        result = check_endpoint(app_ids_to_post, key_name)
        res.config(text=result)
        print(result)

def getdata():
    prod_pesudo_value = ""
    keynames = get_value()
    Envvalue = Environment.get()
    include_global = is_global(need_global)
    global_only = is_global(only_global)
    prod_pesudo = var.get()
    # print(prod_pesudo)
    if(prod_pesudo == 1):
        prod_pesudo_value = "prod"
    if(prod_pesudo == 2):
        prod_pesudo_value = "pesudo"
    
    for keyname in keynames:    
        app_details, key_name = get_env_details(keyname, Envvalue, prod_pesudo_value)
        app_ids_to_post = get_details_by_env(app_details, Envvalue, keyname, include_global, global_only)  # Filter by environment 
        result = update_with_post(app_ids_to_post, Envvalue, key_name, prod_pesudo_value)
label_0 = Label(root, text="ENDPOINT CHANGER",width=20,font=("Verdana 20 bold"), bg="LightSteelBlue1")
label_0.place(x=50,y=53)
label_1 = Label(root, text="       KeyName",width=12,font=("Verdana 10 bold"), bg="LightSteelBlue1")
label_1.place(x=70,y=170)
#keys ={"AffiliateId", "ChannelName", "ContentServiceEndpoint", "LocalizationService", "PaymentService", "SalesChannelManagementService", "BaseUrl", "Mercury-RedirectUrl", "MyPlan-RedirectUrl"}
key=IntVar()
key1=IntVar()
key2=IntVar()
key3=IntVar()
key4=IntVar()
key5=IntVar()
key6=IntVar()
key7=IntVar()
key8=IntVar()
need_global = IntVar()
only_global = IntVar()

def is_global(check_box):
    return bool(check_box.get())

def get_value():
    name = ['AffiliateId', 'ChannelName', 'ContentServiceEndpoint', 'LocalizationService',
     'PaymentService', 'SalesChannelManagementService', 'BaseUrl', 'Mercury-RedirectUrl',
     'MyPlan-RedirectUrl']
    keys = []
    for k, n in zip((key,key1,key2,key3,key4,key5,key6,key7,key8), name):
        if k.get():
            keys.append(n)
    print(keys)
    return keys
Checkbutton(root, text ='AffiliateId', takefocus = 0, variable=key, bg="LightSteelBlue1").place(x = 240, y = 150)
Checkbutton(root, text ='ChannelName', takefocus = 0, variable=key1, bg="LightSteelBlue1").place(x = 380, y = 150)
Checkbutton(root, text ='ContentServiceEndpoint', takefocus = 0, variable=key2, bg="LightSteelBlue1").place(x = 520, y = 150)
Checkbutton(root, text ='LocalizationService', takefocus = 0, variable=key3, bg="LightSteelBlue1").place(x = 240, y = 170)
Checkbutton(root, text ='PaymentService', takefocus = 0, variable=key4, bg="LightSteelBlue1").place(x = 380, y = 170)
Checkbutton(root, text ='SalesChannelManagementService', takefocus = 0, variable=key5, bg="LightSteelBlue1").place(x = 520, y = 170)
Checkbutton(root, text ='BaseUrl', takefocus = 0, variable=key6, bg="LightSteelBlue1").place(x = 240, y = 190)
Checkbutton(root, text ='Mercury-RedirectUrl', takefocus = 0, variable=key7, bg="LightSteelBlue1").place(x = 380, y = 190)
Checkbutton(root, text ='MyPlan-RedirectUrl', takefocus = 0, variable=key8, bg="LightSteelBlue1").place(x = 520, y = 190)
Button(root,text='get value',command=get_value).place(x = 580, y = 230)

label_2 = Label(root, text="   Environment",width=12,font=("Verdana 10 bold"), bg="LightSteelBlue1")
label_2.place(x=68,y=250)
list2 = ['QA2','QA4','QA12','INT','STG'];
c=StringVar()
droplist=OptionMenu(root,Environment, *list2)
droplist.config(width=20)
Environment.set('Select the Environment')
droplist.place(x=240,y=240)
#label_3 = Label(root, text="current point",width=12,font=("Verdana 10 bold"), bg="LightSteelBlue1")
#label_3.place(x=70,y=240)
l1 = Label(root, text = "Current Status",width=12,font=("Verdana 10 bold"), bg="LightSteelBlue1") 
l1.place(x=70,y=300)
d=StringVar()
#e1 = Entry(root, text ="venkat") 
#e1.place(x=240,y=250) 
#Grid=Grid(root,text="test",width=10)
#Grid.place(x=250,y=210)
btn1 = Button(root, text='Check',width=10,bg='white',fg='Black',command=check_data)
btn1.place(x=380,y=300)
res = Label(root, width=15)
res.place(x=240,y=300)
label_4 = Label(root, text="   Prod/Pesudo",width=12,font=("Verdana 10 bold"), bg="LightSteelBlue1")
label_4.place(x=70,y=340)
var = IntVar()
Radiobutton(root, text="Prod",padx = 5, variable=var, value=1, 
            bg="LightSteelBlue1").place(x=230,y=340)
Radiobutton(root, text="Pseudo",padx = 20, variable=var,
            value=2, bg="LightSteelBlue1").place(x=290,y=340)
Checkbutton(root, text ='Include Global Value', takefocus = 0, variable=need_global, bg="LightSteelBlue1").place(x = 200, y = 400)
Checkbutton(root, text ='Only Global Value', takefocus = 0, variable=only_global, bg="LightSteelBlue1").place(x = 200, y = 430)
Button(root, text='Submit',width=20,bg='white',
        fg='Black',command=getdata).place(x=175,y=450)
#Button(root, text='tell',width=10,bg='white',fg='Black',command=get_value)

root.mainloop()