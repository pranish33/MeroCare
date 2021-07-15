import sqlite3

def insert_data(firstName, lastName, phoneNumber, date, problem):
 conn = sqlite3.connect('demo.db') 
 cursor = conn.cursor()
 print("Database created and Successfully Connected to SQLite")
 
 # sql='''CREATE TABLE d2(
    # firstName VARCHAR,
    # lastName VARCHAR,
    # phoneNumber VARCHAR,
    # date VARCHAR,
    # problem VARCHAR,
  # ) '''
   
 cursor.execute('''INSERT INTO d2(firstName, lastName, phoneNumber, date, problem) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (firstName, lastName, phoneNumber, date, problem))
   
	
 print("Table created successfully........")

 # Commit your changes in the database
 conn.commit()

 #Closing the connection
 conn.close()

 
#if __name__ == "__main__":
 #insert_data('Pranish','Acharya', 9874747433, 'this week', 'heart problem')