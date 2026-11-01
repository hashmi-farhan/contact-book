print("welcome to your contact book app")
#code line by line chalti h islye chize overwrite bhi ho skti h like agar tumne contact list ko 
#JSON se use krne ke lye list banaya but agle step me list khali kar diya(by mistake or jaan buch ke)
#to fir finally list khaali hi hojayegi

import json
#JSON: Ye text (string) aur Python dictionary/list ke beech mein translator ka kaam karta hai

def load_contacts():
    #file operations me v try/except krna aroori hai.


    try:
        with open("contacts.json","r") as f:
            return json.load(f)


    except FileNotFoundError:
        #FileNotFoundError: Jab program pehli baar chalta hai, toh contacts.json file hoti hi nahi hai.
        #  Agar tum bina try/except ke file padhne jaoge, toh program crash ho jayega.
        #  except pakad ke khaali list [] de deta hai, taaki program aage badh sake.
        print("file khali h")
        return []


    except json.JSONDecodeError:
        #JSONDecodeError: Agar user ne galti se file ka data kharab kar diya(jaise manually file
        #  edit ki aur bracket hata diya). except isko pakadta hai aur batata hai ki file corrupt hai.


        print("WARNING:file corrupt h!")
        return []
    


#hum yaha q search func define kr rhe h ,task 3 ke andar q nhi?
#Functions hamesha code ke Top (sabse upar) likhe jate hain, kisi loop ya if ke andar nahi
#Agar function top pe hai, toh tum use Task 1 mein bhi call kar sakte ho, Task 3 mein bhi, aur Task 4 mein bhi
#Function ke andar kya hona chahiye? Sirf logic. Kabhi bhi input() function ke andar mat rakho.
#  input() menu mein hoga, aur value function ko parameter ke roop mein jayegi.

def search_contact(contact_list,keyword):
    results=[]
    keyword_lower=keyword.lower()

    #ye lower func use krke naam kaise save h uppercase me ya lowercase me iske drame ko 
    #neglect krta h ye func
    for data in contact_list:
        name_lower=data["name"].lower()
        phone_lower=data["phone"].lower()

        #yaha pr jo humne "in" func use kya h usse farhan hashmi me agar user ne sirf "farhan" 
        #ya sirf "hashmi" v input diya tab bhi contact match kr jayega 
        if (keyword_lower in name_lower  or 
            keyword_lower in phone_lower):
            results.append(data)
            #search function list kyun return karta hai, seedha print nahi karta.
            #return ka matlab: "Main kaam kar ke result de raha hoon, ab tum jo karna chahte ho kar lo
            
    return results
#Kyun return? Agar search function print karega, toh tum us result ko save nahi kar sakte,
#  usko delete nahi kar sakte. Par agar wo list return karega, toh tum us list ko
#  variable mein rakh sakte ho (matches = search_contact(...)), aur uske baad jo chahe kar sakte ho
#  (print karo, count karo, etc.). Search function ka kaam hai "dhoondhna", "dikhana" nahi.


contact_list=load_contacts()
#json ke data k lye func banaya fir usse list me save kya taaki is list ko hi manipulate kr saku 
#as hum direct json me manipulation nhi khel skte h 

while True:
    
    try:
        task_number=int(input("enter the task u want to done:"))

    except ValueError:
        #ValueError: Jab user input mein int() (integer) expect kar rahe the, aur usne "hello" type kar diya.

        print("wrong,insert only numbers from 1 to 6 only!")
        continue
        #continue ka matlab:"Is baar ki galti maaf karo, wapas loop ke shuru mein jao, agla input lo."
        #iske use se loop shuru se start hogi and user ko fir se input dena hoga and ye kaam tab
        #tak chalte rhega jab tak user rule based input naa dede.
        #try/except mein agar user ne task ke liye "hello" type kiya,
        #toh continue lagaya taaki wapas menu se naya task number puche.


    if task_number==1:
        print("for adding contact:")
        contact_name=str(input("enter the naam:"))

        while True:
            #iske andar loop chalaya taaki jab tak user valid number provide naa kre tab tak wo attempts krta rhe..
            phone_number=str(input("enter the contact number:"))
            if phone_number.isdigit() and len(phone_number)==10:
                #as humne to phone_number ko str use kya h to iska func use kr le rhe jisse ki sare digits hi honge
                # sare digits hi honge input me 
                print("contact added successfully")
                break
                #break ka matlab: "Loop ko hamesha ke liye band karo aur bahar nikal jao
            
            else:
                print("please insert 10 digits")
        contact_list.append({"name":contact_name,"phone":phone_number})
        #loop ke bahar append kya taaki sare drame finish ho jaaye and data end me add kr pau
    

    elif task_number==2:
        print("for viewing the list or if empty then print it also")
        print(contact_list)

        
    elif task_number==3:
        print("for searching the contactna")
        keyword=input("enter either name or phone number:")
        matches=search_contact(contact_list,keyword)
        if matches:
            for match in matches:
                print(match)
        else:
            print("no contact found")

    
    elif task_number==4:
        print("for updating the old mobile number:")
        contact_name=str(input("kis contact ka number update krna h:"))

        for contact in contact_list:
            if contact["name"].lower()==contact_name.lower():
                while True:
                    phone_number=str(input("enter the updated contact number:"))
                    if phone_number.isdigit() and len(phone_number)==10:
                        print("contact updated successfully")
                        break
                            
                    else:
                        print("please insert 10 digits")
    #ek confusion-->== vs = me : "==" ka significance ye h ki dono chiz completely equal h
    #"="  ka ye h ki hum indono ko assign kr rhe h iske jageh pr wo 
                contact["phone"]=phone_number
                print("successfully saved!")
                break

            
        else:
            print("no contact!")
        #Agar tumhe check karna hai ki "Koi match mila ya nahi?", 
        # toh hamesha for-else use karo. for ke andar sirf if rakho. 
        # else ko bilkul for ke bahar (indentation kam karke) likho.
        #wrna program har ek pe traverse krega and har baar contact not found
        #ye show krta rhega tab tak jab tak contact naa miljaye jisse ki 
        #program bekaar hojayga,same kaam task me bhi chalega ...
    


    elif task_number==5:
        print("for deleting the contact:")
        contact_name=str(input("enter the name:"))
        for contact in contact_list:
            if contact["name"].lower()==contact_name.lower():
                contact_list.remove(contact)
                print("deleted contact successfully")
                break
        else:
            print("contact not found")

    elif task_number==6:
        with open("contacts.json","w") as f:
            json.dump(contact_list,f,indent=2)
            print("data has rearanged,contacts are deleted or update or added succefully to the file")
            print("program finished ,thanku for visiting!")
            break  
            #yaha break lagaya taki program band ho jaye.Phone number sahi mil gaya toh validation loop se break kiya.


    else:
        print("wrong input ,insert again between 1 to 6")
        continue


