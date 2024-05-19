a={"biryani":10,"cola":24,"chips":3000}
user_dict={}
while True:
    option=int(input("1.Biryani FOR 10\n2.cola FOR 24\n3.chips FOR 3000\n4.To exit menu"))
    if(option==4):
        break
    qty=int(input("\nEnter the Quantity of the product:\n"))
    print("\n")
    if(option==1):
        user_dict["biryani"]=[qty,a["biryani"]]
    elif(option==2):
        user_dict["cola"]=[qty,a["cola"]]
    elif(option==3):
        user_dict["chips"]=[qty,a["chips"]]
print("The Cart is ready!!")
def adr_check():
    adr=input("Enter your address:\n")
    for i in adr.split():
        if(i.lower()=="ksr"):
            return False
        else:
            return True
while(True):
    if(adr_check()==True):
        print("Deliver Ok")
        break
    else:
        print("Try other address")

total_amt=0
for i in user_dict:
    if(i=="biryani"):
        total_amt+=user_dict[i][0]*user_dict[i][1]
    elif(i=="cola"):
        total_amt+=user_dict[i][0]*user_dict[i][1]
    elif(i=="chips"):
        total_amt+=user_dict[i][0]*user_dict[i][1]
if(total_amt>50):
    total_amt-=total_amt*0.1
elif(total_amt>100):
    total_amt-=total_amt*0.15
print("\n")
print(f"After deducting the discount the total amount is: ${total_amt}")
        
        
    

    
