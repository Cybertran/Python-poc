import sqlite3
db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT,phone INTEGER ,email TEXT)")
db.execute("INSERT INTO contacts(name,phone,email) values('jitendra','41352139834723','jeetu345@gmail.com')")
db.execute("INSERT INTO contacts (name,phone,email) values('saif','41352139834723','saif945@gmail.com')")
db.execute("INSERT INTO contacts(name,phone,email) values('poja','41139834723','poja.k@gmail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
for name,phone,email in cursor:
    print(name)
    print(email)
    print(phone)
    print("-" * 20)


# fetch one by one from db
print(cursor.fetchone())

# fetch all records
print(cursor.fetchall())

print("----------------------------")
for name,email, phone in db.execute("SELECT * FROM contacts"):
    print(name ,email ,phone)
    print("-"*30)


db.commit()
db.close()