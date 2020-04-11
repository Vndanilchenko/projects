from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.auth import PlainTextAuthProvider
from broker_detection import cassandra_cluster

print('%'*100)
print(cassandra_cluster)
print('%'*100)

def create_connection():
   auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
   cluster = Cluster([cassandra_cluster], auth_provider=auth_provider)

   session = cluster.connect()
   session.execute("CREATE KEYSPACE IF NOT EXISTS greetings_counter " +
                    "WITH REPLICATION = {" +
                   "'class' : 'SimpleStrategy'," +
                   "'replication_factor' : 1 };")
   session.set_keyspace('greetings_counter')
   # session.execute("DROP COLUMNFAMILY IF EXISTS ds_greetings;")
   session.execute("CREATE COLUMNFAMILY IF NOT EXISTS ds_greetings (firstname text PRIMARY KEY, counter int);")
   return session

def increase_and_get_number_of_greetings(session, firstname):
    # создаём запись, если она ещё не существует со значением 0
    session.execute("INSERT INTO ds_greetings (firstname, counter) VALUES (%s,%s) IF NOT EXISTS", [firstname, 0])
    # считываем для данного ключа в базе данных
    result = session.execute("SELECT * FROM ds_greetings WHERE firstname = %s;", [firstname]).one()
    # берём текущее значение и увеличиваем на 1
    total_greetings = result.counter + 1
    # обновляем запись в базе знаний
    session.execute("UPDATE ds_greetings SET counter =%s WHERE firstname = %s", [total_greetings, firstname])
    return total_greetings
