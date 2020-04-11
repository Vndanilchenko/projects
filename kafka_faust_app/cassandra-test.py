from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.auth import PlainTextAuthProvider

def create_connection():
   auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
   cluster = Cluster(['127.0.0.1'], auth_provider=auth_provider)

   session = cluster.connect()
   session.execute("CREATE KEYSPACE IF NOT EXISTS demo " +
         "WITH REPLICATION = {" +
       "'class' : 'SimpleStrategy'," +
       "'replication_factor' : 1 };")
   session.set_keyspace('demo')
   session.execute("DROP TABLE IF EXISTS users;")
   session.execute("CREATE TABLE users (lastname text PRIMARY KEY, age int)")
   return session

###############
### CREATE ####
###############
def set_user(session, lastname, age, city, email, firstname):
     # TO DO: execute SimpleStatement that inserts one user into the table
     rowkey = lastname + '_' + firstname
     session.execute("INSERT INTO users (lastname, age) VALUES (%s,%s)", [lastname, age])

#############
### READ ####
#############
def get_user(session, lastname):
    # TO DO: execute SimpleStatement that retrieves one user from the table
    # TO DO: print firstname and age of user
    result = session.execute("SELECT * FROM users WHERE lastname = %s;", [lastname]).one()
    print(result.lastname, result.age)

###############
### UPDATE ####
###############
def update_user(session, new_age, lastname):
    # TO DO: execute SimpleStatement that updates the age of one user
    session.execute("UPDATE users SET age =%s WHERE lastname = %s", [new_age, lastname])

###############
### DELETE ####
###############
def delete_user(session, lastname):
    # TO DO: execute SimpleStatement that deletes one user from the table
    session.execute("DELETE FROM users WHERE lastname = %s", [lastname])


def main():
    session = create_connection()

    lastname = "Jones"
    age = 35
    city = "Austin"
    email = "bob@example.com"
    firstname = "Bob"
    new_age = 36

    set_user(session, lastname, age, city, email, firstname)

    get_user(session, lastname)

    update_user(session, new_age, lastname)

    get_user(session, lastname)

    delete_user(session, lastname)

if __name__ == "__main__":
    main()
