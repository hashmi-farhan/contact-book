print("welcome to your contact book app")


import json

def load_contacts():
    try:
        with open("contacts.json","r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("file khali h")
        return []
    except json.JSONDecodeError:
        print("WARNING:file corrupt h!")
        return []


def search_contact(contact_list,keyword):
    results=[]
    keyword_lower=keyword.lower()
    for data in contact_list:
        name_lower=data["name"].lower()
        phone_lower=data["phone"].lower()
        if (keyword_lower in name_lower  or 
            keyword_lower in phone_lower):
            results.append(data)
    return results


contact_list=load_contacts()

while True:
    
    try:
        task_number=int(input("enter the task u want to done:"))
    except ValueError:
        print("wrong,insert only numbers from 1 to 6 only!")
        continue
    if task_number==1:
        print("for adding contact:")
        contact_name=str(input("enter the naam:"))

        while True:
            phone_number=str(input("enter the contact number:"))
            if phone_number.isdigit() and len(phone_number)==10:
                print("contact added successfully")
                break
            
            else:
                print("please insert 10 digits")
        contact_list.append({"name":contact_name,"phone":phone_number})
    

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

                contact["phone"]=phone_number
                print("successfully saved!")
                break
            
        else:
            print("no contact!")


    elif task_number==5:
        print("for deleting the contact:")
        contact_name=str(input("enter the name:")) 
        # phone_number =str(input("enter the mobile number :"))
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
    else:
        print("wrong input ,insert again between 1 to 6")
        continue


