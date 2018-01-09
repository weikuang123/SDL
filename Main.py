from Records import Records


def processRecord():
    userList=[]
    user_file = open('transaction.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        record=Records(list[0], int(list[1]), int(list[2]),list[3],int(list[4],))

        userList.append(record)
    return userList



def newRecord( people, payment, percentage_cost, max_cap, amount_paid):
    userdata=people+","+payment+","+percentage_cost+","+max_cap+","+amount_paid
    user_file=open("transaction.txt","a")
    user_file.write(userdata)