from base import Database

class Country:
    def __init__(self, name:str):
        self.name = name


    def insert(self, table = "country"):
        query = f"""INSERT INTO {table}(name) 
        VALUES('{self.name}');"""
        return Database.connect(query,"insert")
    
    @staticmethod
    def select(table = "country"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query,"select")
    
    @staticmethod
    def delete(column, data, table = "country"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""
        return Database.connect(query,"delete")
    
    @staticmethod
    def deleteID(column, data, table = "country"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query,"delete")
    
    @staticmethod
    def update(column, data, idColumn, id, table = "country"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query,"update")
    

class City(Country):
    def __init__(self, name: str, country_id: int):
        super().__init__(name)
        self.country_id = country_id

    def insert(self, table = "city"):
        query = f"""INSERT INTO {table}(name, country_id) 
        VALUES('{self.name}', {self.country_id});"""
        return Database.connect(query,"insert")
    

class Address(Country):
    def __init__(self, name: str, city_id:int):
        super().__init__(name)
        self.city_id = city_id

    def insert(self, table = "address"):
        query = f"""INSERT INTO {table}(name, city_id) 
        VALUES('{self.name}', {self.city_id});"""
        return Database.connect(query,"insert")
    

class Users:
    def __init__(self, first_name:str, last_name:str, username:str, password:str, gmail:str, create_date:str):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.gmail = gmail
        self.create_date = create_date


    def insert(self, table = "users"):
        query = f"""INSERT INTO {table}(name) 
        VALUES('{self.first_name}', '{self.last_name}', '{self.username}', '{self.password}', '{self.gmail}', '{self.create_date}');"""
        return Database.connect(query,"insert")
    
    @staticmethod
    def select(table = "users"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query,"select")
    
    @staticmethod
    def delete(column, data, table = "users"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""
        return Database.connect(query,"delete")
    
    @staticmethod
    def deleteID(column, data, table = "users"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query,"delete")
    
    @staticmethod
    def update(column, data, idColumn, id, table = "users"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query,"update")
    

class Student(Users):
    def __init__(self, first_name: str, last_name: str, username: str, password: str, gmail: str, create_date: str, address_id:int):
        super().__init__(first_name, last_name, username, password, gmail, create_date)
        self.address_id = address_id

    def insert(self, table = "city"):
        query = f"""INSERT INTO {table}(first_name, last_name, username, password, gmail, create_date, address_id) 
        VALUES('{self.first_name}', '{self.last_name}', '{self.username}', '{self.password}', '{self.gmail}', '{self.create_date}', {self.address_id});"""
        return Database.connect(query,"insert")
    

class Mentor(Users):
    def __init__(self, first_name: str, last_name: str, username: str, password: str, gmail: str, create_date: str, city_id:int):
        super().__init__(first_name, last_name, username, password, gmail, create_date)
        self.city_id = city_id

    def insert(self, table = "address"):
        query = f"""INSERT INTO {table}(first_name, last_name, username, password, gmail, create_date, city_id) 
        VALUES('{self.first_name}', '{self.last_name}', '{self.username}', '{self.password}', '{self.gmail}', '{self.create_date}', {self.city_id});"""
        return Database.connect(query,"insert")
    

class Course:
    def __init__(self, name:str, description:str, rating:float, price:float, language:str, create_date:str):
        self.name = name
        self.description = description
        self.rating = rating
        self.price = price
        self.language = language
        self.create_date = create_date

    def insert(self, table = "course"):
        query = f"""INSERT INTO {table}(name, description, rating, price, language, create_date) 
        VALUES('{self.name}', '{self.description}', {self.rating}, {self.price}, '{self.language}', '{self.create_date}');"""
        return Database.connect(query,"insert")
    
    @staticmethod
    def select(table = "course"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query,"select")
    
    @staticmethod
    def delete(column, data, table = "course"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""
        return Database.connect(query,"delete")
    
    @staticmethod
    def deleteID(column, data, table = "course"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query,"delete")
    
    @staticmethod
    def update(column, data, idColumn, id, table = "course"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query,"update")
    

class CourseStudent:
    def __init__(self, course_id:int, student_id:int):
        self.course_id = course_id
        self.student_id = student_id

    def insert(self, table = "course_student"):
        query = f"""INSERT INTO {table}(course_id, student_id) 
        VALUES({self.course_id}, {self.student_id});"""
        return Database.connect(query, "insert")
    
    @staticmethod
    def select(table = "course_student"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    @staticmethod
    def delete(column, data, table = "course_student"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""
        return Database.connect(query, "delete")

    @staticmethod
    def deleteID(column, data, table = "course_student"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(column, data, idColumn, id, table = "course_student"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query,"update")
    

class CourseMentor:
    def __init__(self, course_id:int, mentor_id:int):
        self.mentor_id = mentor_id
        self.course_id = course_id

    def insert(self, table = "course_mentor"):
        query = f"""INSERT INTO {table}(mentor_id, course_id) 
        VALUES({self.mentor_id}, {self.course_id});"""
        return Database.connect(query, "insert")
    
    @staticmethod
    def select(table = "course_mentor"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    @staticmethod
    def delete(column, data, table = "course_mentor"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""
        return Database.connect(query, "delete")

    @staticmethod
    def deleteID(column, data, table = "course_mentor"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(column, data, idColumn, id, table = "course_mentor"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query,"update")
    

class Speciality:
    def __init__(self, name:str, description:str, courseNumber:int, create_date:str):
        self.name = name
        self.description = description
        self.courseNumber = courseNumber
        self.create_date = create_date

    def insert(self, table = "speciality"):
        query = f"""INSERT INTO {table}(name, description, courseNumber, create_date) 
        VALUES('{self.name}', '{self.description}', {self.courseNumber}, '{self.create_date}');"""
        return Database.connect(query, "insert")
    
    @staticmethod
    def select(table = "speciality"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    @staticmethod
    def delete(column, data, table = "speciality"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""
        return Database.connect(query, "delete")

    @staticmethod
    def deleteID(column, data, table = "speciality"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(column, data, idColumn, id, table = "speciality"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query,"update")
    

class SpecialityCourse:
    def __init__(self, speciality_id:int, course_id:int):
        self.speciality_id = speciality_id
        self.course_id = course_id

    @staticmethod
    def select(table = "speciality_course"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    def insert(self, table = "speciality_course"):
        query = f"""INSERT INTO {table}(speciality_id, course_id) 
        VALUES({self.speciality_id}, {self.course_id});"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table = "speciality_course"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""
        return Database.connect(query, "delete")

    @staticmethod
    def deleteID(column, data, table = "speciality_course"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(column, data, idColumn, id, table = "speciality_course"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query,"update")
    

class Modul:
    def __init__(self, name:str, lessonNumber:int, create_date:str, course_id:int):
        self.name = name
        self.lessonNumber = lessonNumber
        self.create_date = create_date
        self.course_id = course_id

    def insert(self, table = "modul"):
        query = f"""INSERT INTO {table}(name, lessonNumber, create_date, course_id) 
        VALUES('{self.name}', {self.lessonNumber}, '{self.create_date}', {self.course_id});"""
        return Database.connect(query, "insert")
    
    @staticmethod
    def select(table = "modul"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    @staticmethod
    def delete(column, data, table = "modul"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""
        return Database.connect(query, "delete")

    @staticmethod
    def deleteID(column, data, table = "modul"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(column, data, idColumn, id, table = "modul"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query,"update")
    

class Lesson:
    def __init__(self, name:str, modul_id:int):
        self.name = name
        self.modul_id = modul_id

    def insert(self, table = "lesson"):
        query = f"""INSERT INTO {table}(name, modul_id) 
        VALUES('{self.name}', {self.modul_id});"""
        return Database.connect(query, "insert")
    
    @staticmethod
    def select(table = "lesson"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    @staticmethod
    def delete(column, data, table = "lesson"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""
        return Database.connect(query, "delete")

    @staticmethod
    def deleteID(column, data, table = "lesson"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(column, data, idColumn, id, table = "lesson"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query,"update")
    

class PaymentType:
    def __init__(self, name:str):
        self.name = name

    def insert(self, table = "payment_type"):
        query = f"""INSERT INTO {table}(name) 
        VALUES('{self.name}');"""
        return Database.connect(query, "insert")
    
    @staticmethod
    def select(table = "payment_type"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    @staticmethod
    def delete(column, data, table = "payment_type"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""
        return Database.connect(query, "delete")

    @staticmethod
    def deleteID(column, data, table = "payment_type"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(column, data, idColumn, id, table = "payment_type"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query,"update")
    

class Payment:
    def __init__(self, amount:float, student_id:int, course_id:int, payment_type_id:int, create_date:str):
        self.amount = amount
        self.student_id = student_id
        self.course_id = course_id
        self.payment_type_id = payment_type_id
        self.create_date = create_date

    def insert(self, table = "payment"):
        query = f"""INSERT INTO {table}(amount, student_id, course_id, payment_type_id, create_date) 
        VALUES({self.amount}, {self.student_id}, {self.course_id}, {self.payment_type_id}, '{self.create_date}');"""
        return Database.connect(query, "insert")
    
    @staticmethod
    def select(table = "payment"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    @staticmethod
    def delete(column, data, table = "payment"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""
        return Database.connect(query, "delete")

    @staticmethod
    def deleteID(column, data, table = "payment"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(column, data, idColumn, id, table = "payment"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query,"update")
    
    