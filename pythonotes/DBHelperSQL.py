#
# Module: DBHelper
# 
# This helper class manipulates the DB
# 
# 2013, Frank Caron

#Imports
import sqlite3 as lite
import json

#Global Vars
_db_name = 'pythonotes/notes.db'

#
# Module: DBWriter
# 
# Writes to the DB

class DBWriter:
    
    # Private Variables
    _db_con = None
    _db_cursor = None
    
    #Do a DB update
    def db_update(self, query):
        self._db_con = lite.connect(_db_name)
        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute(query)
            self._db_con.commit()
        except lite.ProgrammingError as e:
            print "DBHelper Error: " + e
        self._db_cursor.close()
        self._db_con.close()
        
    #Check if Notepad ID exists
    def db_check_notepad_id(self, notepad_id):
        self._db_con = lite.connect(_db_name)
        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute('SELECT COUNT(*) FROM notes WHERE notepad_id_key =' + str(notepad_id) + ';')
            return self._db_cursor.fetchone()[0]
        except lite.ProgrammingError as e:
            print "DBHelper Error: " + e
        self._db_cursor.close()
        self._db_con.close()
        
#
# Module: DBWriter
# 
# Reads from the DB

class DBReader:
    
    # Private Variables
    _db_con = None
    _db_cursor = None
    
    #Do a DB read for all notes
    def db_read_all(self):
        self._db_con = lite.connect(_db_name)
        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute('SELECT * from notes')

			#Dict Way
            r = [dict((self._db_cursor.description[idx][0], value)
               for idx, value in enumerate(row)) for row in self._db_cursor.fetchall()]
            return r 
            
        except lite.ProgrammingError as e:
            print "DBHelper Error: " + e
        self._db_cursor.close()
        self._db_con.close()

	#Do a DB read for a specific note
    def db_read_specific(self, note_id):
        self._db_con = lite.connect(_db_name)
        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute('SELECT * from notes where note_id =' + str(note_id))

			#Dict Way
            r = [dict((self._db_cursor.description[idx][0], value)
               for idx, value in enumerate(row)) for row in self._db_cursor.fetchall()]
            return r 
            
        except lite.ProgrammingError as e:
            print "DBHelper Error: " + e
        self._db_cursor.close()
        self._db_con.close()

	#Do a DB read for a specific notepad
    def db_read_specific_notepad(self, notepad_id):
        self._db_con = lite.connect(_db_name)
        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute('SELECT * from notes where notepad_id_key =' + str(notepad_id))
            
			#Dict Way
            r = [dict((self._db_cursor.description[idx][0], value)
               for idx, value in enumerate(row)) for row in self._db_cursor.fetchall()]
            return r 
            
        except lite.ProgrammingError as e:
            print "DBHelper Error: " + e
        self._db_cursor.close()
        self._db_con.close()
        
    def db_get_last_row_id(self):
        self._db_con = lite.connect(_db_name)
        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute("SELECT max(note_id) FROM notes")
            return str(self._db_cursor.fetchone()[0])
        except lite.ProgrammingError as e:
            print "DBHelper Error: " + e
        self._db_cursor.close()
        self._db_con.close()    
        
#
# Module: DBDeleter
# 
# Deletes from the DB  

class DBDeleter:
    
    # Private Variables
    _db_con = None
    _db_cursor = None 

    #Do a DB read
    def db_delete(self, note_id):
        self._db_con = lite.connect(_db_name)
        self._db_cursor = self._db_con.cursor()    
        try:
            self._db_cursor.execute("DELETE FROM notes WHERE note_id =" + str(note_id) + ";")
            self._db_con.commit()
        except lite.ProgrammingError as e:
            print "DBHelper Error: " + e
        self._db_cursor.close()
        self._db_con.close()
        