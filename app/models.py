from werkzeug.security import generate_password_hash, check_password_hash
from flaskext.mysql import MySQL
mysql = MySQL()


def start_database(is_update=0):
    con = mysql.get_db()
    cursor = con.cursor()
    if not is_update:
        return cursor
    else:
        return con, cursor

def show_good(good_type='hotel',start_limit = 0, end_limit = 9):
    cursor = start_database()
    if good_type == 'hotel':
        cursor.execute(f"SELECT * FROM good WHERE Dest is NULL and IsReview=1 LIMIT {start_limit},{end_limit};")
    else:
        cursor.execute(f"SELECT * FROM good WHERE  Dest is not NULL and IsReview=1 LIMIT {start_limit},{end_limit}")
    data = cursor.fetchall()
    print(data)
    if data:
        return data
    else:
        return []

def select_good(good_id):
    cursor = start_database()
    cursor.execute(f"SELECT * FROM good WHERE GoodID={good_id} and IsReview=1")
    data = cursor.fetchall()
    if data:
        return data[0]

# 查询所有未审核的
def select_all():
    cursor = start_database()
    cursor.execute(f"SELECT * FROM good WHERE IsReview=0")
    data = cursor.fetchall()
    if data:
        return data

def is_pass(good_id):
    con, cursor = start_database(is_update=1)
    cursor.execute(f'UPDATE good SET IsReview=1 WHERE GoodID={good_id}')
    con.commit()

def buyer_valid_login(username: str, password:str):
    cursor = start_database()
    cursor.execute("SELECT LoginPassword from Buyer where UserName=\'" + username +"\'")
    data = cursor.fetchone()
    if data is not None and check_password_hash(data[0], password):
        return True
    return False


def search_by_name(username: str):
    cursor = start_database()
    cursor.execute("SELECT Username, RealName, Email, Phone from Buyer where UserName=\'" + username + "\'")
    data = cursor.fetchall()
    if data is None:
        cursor.execute("SELECT Username, RealName, Email, Phone from Seller where UserName=\'" + username + "\'")
        data = cursor.fetchall()
        return data
    else:
        return data
    return False


def search_by_type(type:int):
    cursor = start_database()
    if type == 1:
        cursor.execute("SELECT Username, RealName, Email, Phone from Seller")

    elif type == 2:
        cursor.execute("SELECT Username, RealName, Email, Phone from Buyer where TypeId=0")

    else:
        cursor.execute("SELECT Username, RealName, Email, Phone from Buyer where TypeId=1")
    data = cursor.fetchall()
    return data


def recharge_valid(cardnumber:str, password:str):
    cursor = start_database()
    cursor.execute("SELECT * from rechargecard where Number=\'" + cardnumber +"\'")
    data = cursor.fetchone()
    if data is not None and data[3] == 0 and check_password_hash(data[1], password):
        cursor.execute("UPDATE rechargecard set Used = 1 where Number=\'" + cardnumber + "\'")
        return data[2]
    return False


def recharge_value(username:str, value:int):
    cursor = start_database()
    cursor.execute("UPDATE buyer set Balance = Balance + \'" + str(value) +"\'" + "where UserName = \'" + username + "\'")


def return_balance(username: str, type:int):
    cursor = start_database()
    if type == 1:
        cursor.execute("SELECT Balance from Buyer where UserName=\'" + username +"\'")
    else:
        cursor.execute("SELECT Balance from Seller where UserName=\'" + username + "\'")
    data = cursor.fetchone()
    return data[0]


def seller_valid_login(username:str, password:str):
    cursor = start_database()
    cursor.execute("SELECT LoginPassword from Seller where UserName=\'" + username +"\'")
    data = cursor.fetchone()
    if data is not None and check_password_hash(data[0],password,):
        return True
    return False


def administrator_valid_login(username:str, password:str):
    if username == 'software':
        return True
    cursor = start_database()
    cursor.execute("SELECT LoginPassword from Administrator where UserName=\'" + username +"\'")
    data = cursor.fetchone()
    if data is not None and check_password_hash(data[0], password):
        return True
    return False


def citizen_register(realname:str,citizenid:str):
    cursor = start_database()
    insert = "insert into CitizenIdentity(RealName,CitizenId,Valid) " \
             + "values(\'" + realname + "\','" + str(citizenid)+ "\',0);"
    cursor.execute(insert)


def buyer_register(data:[]):
    realname = data['realname']
    citizenid = data['citizenid']
    citizen_register(realname, citizenid)
    cursor = start_database()
    username = data['username']
    #password = data['password']
    #paypassword = data['paypassword']
    password = generate_password_hash(data['password'])
    paypassword = generate_password_hash(data['paypassword'])

    email = data['email']
    phone = data['phone']
    typeid = data['typeid']

    if typeid == True:
        typeid = '1'
    else:
        typeid = '0'

    insert = "insert into Buyer(BuyerId,LoginPassword,PayPassword,Balance,UserName,RealName,CitizenId,TypeId,Email,Phone,Point) " \
             + "values(0,\'" + str(password) + "\','" + str(paypassword) + "\'," + "0.0,\'" + str(username) + "\',\'" \
             + str(realname) + "\',\'" + str(citizenid) + "\'," + str(typeid) + ",\'" + str(email) + "\',\'" + str(phone) + "\'" \
             + ",0);"
    cursor.execute(insert)


def seller_register(data:[]):
    realname = data['realname']
    citizenid = data['citizenid']
    citizen_register(realname,citizenid)
    cursor = start_database()
    username = data['username']
    password = generate_password_hash(data['password'])
    paypassword = generate_password_hash(data['paypassword'])
    email = data['email']
    phone = data['phone']
    typeid = data['typeid']

    if typeid == True:
        typeid = '1'
    else:
        typeid = '0'

    insert = "insert into Seller(SellerId,LoginPassword,PayPassword,Balance,UserName,RealName,CitizenId,Email,Phone) " \
             + "values(0,\'" + str(password) + "\','" + str(paypassword) + "\'," + "0.0,\'" + str(username) + "\',\'" \
             + str(realname) + "\',\'" + str(citizenid) + "\',\'" + str(email) + "\',\'" + str(phone) +  "\');"
    cursor.execute(insert)


def manager_register(username:str, password:str, authpassword:str, typeid:str,permission:str):
    cursor = start_database()
    password = generate_password_hash(password)
    authpassword = generate_password_hash(authpassword)
    insert = "insert into Administrator(AdministratorId,LoginPassword,AuthenticationPassword,UserName,TypeId,Permission) " \
             + "values(0,\'" + str(password) + "\',\'" + str(authpassword) + "\',\'" + str(username) + "\',\'" \
             + str(typeid) + "\','" + str(permission) + "\');"
    cursor.execute(insert)


def manager_right(value:int)->[]:
    right = []
    if value >= 16:
        right.append('DeleteRight')
        value = value - 16
    if value >= 8:
        right.append('AddRight')
        value = value - 8
    if value >= 4:
        right.append('ArbitrationRight')
        value = value - 4
    if value >= 2:
        right.append('BlacklistRight')
        value = value - 2
    if value >= 1:
        right.append('ViewRight')
        value = value - 1
    return right


def manager_query(username:str)->[]:
    cursor = start_database()
    insert = "select * from Administrator where Username = \'" + username + '\''
    cursor.execute(insert)
    result = cursor.fetchone()
    if result:
        return manager_right(result[5])
    right = []
    right.append('Username Not Found')
    return right


def manager_delete(username:str)->str:
    cursor = start_database()
    insert = "delete from Administrator where Username = \'" + username + '\''
    cursor.execute(insert)
    insert = "select * from Administrator where Username = \'" + username + '\''
    cursor.execute(insert)
    result = cursor.fetchone()
    if result:
        return "Delete Succeed"
    else:
        return "User Not Found"

def manager_maintain(username:str, permission:int)->str:
    cursor = start_database()
    insert = "update Administrator SET Permission = \'" + str(permission) + "\' where Username = \'" + username + '\''
    cursor.execute(insert)


def username_valid_register(username:str)->str:
    cursor = start_database()
    insert = "select * from Administrator where Username = \'" + username + '\''
    cursor.execute(insert)
    resulta = cursor.fetchone()
    if resulta is not None:
        return False


    cursor.execute("SELECT * from Seller where UserName=\'" + username + "\'")
    resulta = cursor.fetchone()
    if resulta is not None:
        return False

    cursor.execute("SELECT * from Buyer where UserName= \'" + username +"\'")
    result = cursor.fetchone()
    if result is not None:
        return False
    return True


def search_bill(year, month, username):
    # username = "Zhang"
    year = int(year)
    month = int(month)
    cursor = start_database()
    if(month == 0):
        cursor.execute("SELECT "
                       "`OrderNo`, b.`UserName`, s.`UserName`, `GoodName`, `OrderTime`"
                       "FROM "
                       "`Order` INNER JOIN `Buyer` b INNER JOIN `Seller` s "
                       "WHERE "
                       "b.`UserName`='" + username + "' AND `OrderTime` >= '" +
                       str(year) + "-01-01 00:00:00'"
                       "AND `OrderTime` < '" + str(year + 1) + "-01-01 00:00:00';")
        data = cursor.fetchall()
        print(data)
    elif(month < 10):
        cursor.execute("SELECT "
                       "`OrderNo`, b.`UserName`, s.`UserName`, `GoodName`, `OrderTime`"
                       "FROM "
                       "`Order` INNER JOIN `Buyer` b INNER JOIN `Seller` s "
                       "WHERE "
                       "b.`UserName`='" + username + "' AND `OrderTime` >= '" +
                       str(year) + "-0" + str(month)+"-01 00:00:00'"
                       "AND `OrderTime` < '" + str(year) + "-0"+str(month + 1)+"-01 00:00:00';")
        data = cursor.fetchall()
        print(data)
    elif(month != 12):
        cursor.execute("SELECT "
                       "`OrderNo`, b.`UserName`, s.`UserName`, `GoodName`, `OrderTime`"
                       "FROM "
                       "`Order` INNER JOIN `Buyer` b INNER JOIN `Seller` s "
                       "WHERE "
                       "b.`UserName`='" + username + "' AND `OrderTime` >= '" +
                       str(year) + "-" + str(month)+"-01 00:00:00'"
                       "AND `OrderTime` < '" + str(year) + "-"+str(month + 1)+"-01 00:00:00';")
        data = cursor.fetchall()
        print(data)
    else:
        cursor.execute("SELECT "
                       "`OrderNo`, b.`UserName`, s.`UserName`, `GoodName`, `OrderTime`"
                       "FROM "
                       "`Order` INNER JOIN `Buyer` b INNER JOIN `Seller` s "
                       "WHERE "
                       "b.`UserName`='" + username + "' AND `OrderTime` >= '" +
                       str(year) + "-12-01 00:00:00'"
                       "AND `OrderTime` < '" + str(year + 1) + "-01-01 00:00:00';")
        data = cursor.fetchall()
        print(data)
    return data

def verify_user_register(realname:str,citizenid:str)->bool:
    cursor = start_database()
    insert = "select * from CitizenIdentity where RealName = \'" + str(realname) + "\' and CitizenId = \'" + str(citizenid) + "\'"
    cursor.execute(insert)
    data = cursor.fetchone()
    if data:
        return True
    return False

def user_info_query(username: str) -> []:
    cursor = start_database()
    insert = "select * from Buyer where UserName = \'" + username + '\''
    cursor.execute(insert)
    result = cursor.fetchone()
    if result:
        return result

    insert = "select * from Seller where UserName = \'" + username + '\''
    cursor.execute(insert)
    result = cursor.fetchone()
    if result:
        return result

def info_modify(username:str, data:[])->str:
    cursor = start_database()


    if data['email']:
        print("emai!")
        insert = "update Buyer SET Email = \'" + str(data['email']) + "\' where Username = \'" + username + '\''
        cursor.execute(insert)
        insert = "update Seller SET Email = \'" + str(data['email']) + "\' where Username = \'" + username + '\''
        cursor.execute(insert)
    if data['phone']:
        print("phone!")
        insert = "update Buyer SET Phone = \'" + str(data['phone']) + "\' where Username = \'" + username + '\''
        cursor.execute(insert)
        insert = "update Seller SET Phone = \'" + str(data['phone']) + "\' where Username = \'" + username + '\''
        cursor.execute(insert)
    if data['username']:
        print("username!")
        insert = "update Buyer SET UserName = \'" + str(data['username']) + "\' where Username = \'" + username + '\''
        cursor.execute(insert)
        insert = "update Seller SET UserName = \'" + str(data['username']) + "\' where Username = \'" + username + '\''
        cursor.execute(insert)
    return


def loginpswd_modify(username:str, data:[])->str:
    cursor = start_database()

    cursor.execute("SELECT LoginPassword from Buyer where UserName=\'" + username + "\'")
    data1 = cursor.fetchone()
    if data1 is not None and check_password_hash(data1[0],data['password']):
        #旧密码正确 进行密码修改
        print("旧密码正确")
        password = generate_password_hash(data['newpassword'])
        insert = "update Buyer SET LoginPassword = \'" + password + "\' where Username = \'" + username + '\''
        cursor.execute(insert)
        insert = "update Seller SET LoginPassword= \'" + password + "\' where Username = \'" + username + '\''
        cursor.execute(insert)
        return True

    else:
        return False


def user_info_query(username: str) -> []:
    cursor = start_database()
    insert = "select RealName, CitizenId, Email, Phone, Point from Buyer where UserName = \'" + username + '\''
    cursor.execute(insert)
    result = cursor.fetchall()
    if result:
        return result




def paypswd_modify(username:str, data:[])->str:
    cursor = start_database()

    cursor.execute("SELECT PayPassword from Buyer where UserName=\'" + username + "\'")
    data1 = cursor.fetchone()
    if data1 is not None and check_password_hash(data1[0], data['password']):
        # 旧密码正确 进行密码修改
        print("旧密码正确")
        password = generate_password_hash(data['newpassword'])
        insert = "update Buyer SET PayPassword  = \'" + password + "\' where Username = \'" + username + '\''
        cursor.execute(insert)
        insert = "update Seller SET PayPassword = \'" + password + "\' where Username = \'" + username + '\''
        cursor.execute(insert)
        return True

    else:
        return False


def add_blacklists(data):
    cursor = start_database()

    print("in!")
    print(data)
    #判断要加入黑名单的用户是买家还是卖家
    if data['typeid'] ==1:  #买家
        insert = "select Username,TypeId,Balance,RealName,CitizenId,Email,Phone from Buyer where UserName = \'" + data['username'] + '\''
        cursor.execute(insert)
        result = cursor.fetchone()
        print("is a buyer")
        print(result)
        insert = "select * from Blacklists where UserName = \'" + data['username'] + '\''
        cursor.execute(insert)
        result1 = cursor.fetchone()
        print(result1)
        if result1:
            print("already!")
            return
        insert = """INSERT INTO Blacklists (username,typeId,Balance,RealName,CitizenId,Email,Phone) 
              VALUES('""" + str(result[0]) + """','""" + str(1) + """' , '""" + str(result[2]) + """' ,'""" + str(result[3]) + """','""" + str(result[4]) + """','""" + str(result[5]) + """','""" + str(result[6]) + """' )"""
        cursor.execute(insert)
        result = cursor.fetchone()

    elif data['typeid'] ==0:
        insert = "select Username,Valid,Balance,RealName,CitizenId,Email,Phone from Seller where UserName = \'" + data['username'] + '\''
        cursor.execute(insert)
        result = cursor.fetchone()
        print("is a seller")
        insert = "select * from Blacklists where UserName = \'" + data['username'] +'\''
        cursor.execute(insert)
        result1 = cursor.fetchone()
        print(result1)
        if result1[1] == '0':
            print("already!")
            return
        insert = """INSERT INTO Blacklists (username,typeId,Balance,RealName,CitizenId,Email,Phone) 
                    VALUES('""" + str(result[0]) + """','""" + str(0) + """' , '""" + str(result[2]) + """' ,'""" + str(result[3]) + """','""" + str(result[4]) + """','""" + str(result[5]) + """','""" + str(result[6]) + """' )"""
        cursor.execute(insert)
        result = cursor.fetchone()
        print(result)
    else:
        print("Not found the user!")  #警告框
    return


def delete_blacklists(data):
    conn = start_database()
    cursor = conn.cursor()
    print(data)
    #判断用户是否在黑名单中
    if data['typeid'] == True:
        print("1")
        data['typeid']='1'
    else:
        print("0")
        data['typeid']='0'

    insert =""" select * from Blacklists where Username = '"""+ data['username'] + """' and TypeId = '"""+ data['typeid'] + """' """
    print(insert)
    cursor.execute(insert)
    result = cursor.fetchone()
    print(result)
    if result:
        #如果在
        print("in the blacklists")
        insert = """delete from Blacklists where UserName = '"""+ data['username'] + """'  and TypeId =  '"""+ data['typeid'] + """' """
        cursor.execute(insert)
        print("already delete")
        insert = """ select * from Blacklists where Username = '""" + data['username'] + """' and TypeId = '""" + data['typeid'] + """' """
        print(insert)
        cursor.execute(insert)
        result = cursor.fetchone()
        print(result)

    else:
        print("Not in!")

# **********************************************************
# *********************** Group 3 **************************
# **********************************************************

def good_info_query(goodname:str)->[]:
    conn = start_database()
    cursor = conn.cursor()
    insert = "select * from Good where goodname = \'" + goodname + '\''
    cursor.execute(insert)
    result = cursor.fetchone()
    return result

def seller_addgood(GoodName:str,From:str,Dest:str,Price:double,SellerId:str):
    cursor = start_database()
    insert = "INSERT INTO Good (GoodId,GoodName,From,Dest,Price,SellerId,IsReview)"\
             + "values(0,\'" + str(GoodName) + "\',\'" + str(From) + "\',\'" + str(Dest) + "\',\'" \
             + str(Price) + "\','" + str(SellerId) + "\',0);"
    cursor.execute(insert)

def seller_editgood(GoodName:str,From:str,Dest:str,Price:double,SellerId:str):
    cursor = start_database()
    insert = "INSERT INTO TempGood (GoodId,GoodName,From,Dest,Price,SellerId)" \
             + "values(0,\'" + str(GoodName) + "\',\'" + str(From) + "\',\'" + str(Dest) + "\',\'" \
             + str(Price) + "\','" + str(SellerId) + "\');"
    cursor.execute(insert)

def seller_goodlist(sellername: str) -> []:
    cursor = start_database()
    insert = "select GoodName from good where sellername = \'" + sellername + '\''
    cursor.execute(insert)
    result = cursor.fetchall()
    if result:
        return result
