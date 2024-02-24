import base

def createTables():
    country_table = f"""
        CREATE TABLE country(
            country_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            last_update TIMESTAMP DEFAULT now());"""
    
    city_table = f"""
        CREATE TABLE city(
            city_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            country_id INT REFERENCES country(country_id),
            last_update TIMESTAMP DEFAULT now());"""
    
    address_table = f"""
        CREATE TABLE address(
            address_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            city_id INT REFERENCES city(city_id),
            last_update TIMESTAMP DEFAULT now());"""
    
    user_table = f"""
        CREATE TABLE users(
            user_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            username VARCHAR(50),
            password VARCHAR(20) NOT NULL,
            gmail VARCHAR(50),
            create_date DATE);"""
    
    student_table = f"""
        CREATE TABLE student(
            student_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            username VARCHAR(50),
            password VARCHAR(50) NOT NULL,
            gmail VARCHAR(50),
            create_date DATE,
            last_update TIMESTAMP DEFAULT now(),
            address_id INT REFERENCES address(address_id));"""
    
    mentor_table = f"""
        CREATE TABLE mentor(
            mentor_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            username VARCHAR(50),
            password VARCHAR(50) NOT NULL,
            gmail VARCHAR(50),
            create_date DATE,
            city_id INT REFERENCES city(city_id));"""
    
    course_table = f"""
        CREATE TABLE course(
            course_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            description TEXT,
            rating FLOAT,
            price FLOAT,
            language VARCHAR(50),
            create_date DATE);"""
    
    course_student_table = f"""
        CREATE TABLE course_student(
            course_student_id SERIAL PRIMARY KEY,
            course_id INT REFERENCES course(course_id),
            student_id INT REFERENCES student(student_id),
            last_update TIMESTAMP DEFAULT now());"""
    
    course_mentor_table = f"""
        CREATE TABLE course_mentor(
            course_mentor_id SERIAL PRIMARY KEY,
            mentor_id INT REFERENCES mentor(mentor_id),
            course_id INT REFERENCES course(course_id),
            last_update TIMESTAMP DEFAULT now());"""
    
    speciality_table = f"""
        CREATE TABLE speciality(
            speciality_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            description TEXT,
            courseNumber INT,
            last_update TIMESTAMP DEFAULT now(),
            create_date DATE);"""
    
    speciality_course_table = f"""
        CREATE TABLE speciality_course(
            speciality_course_id SERIAL PRIMARY KEY,
            speciality_id INT REFERENCES speciality(speciality_id),
            course_id INT REFERENCES course(course_id),
            last_update TIMESTAMP DEFAULT now());"""
    
    modul_table = f"""
        CREATE TABLE modul(
            modul_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            lessonNumber INT,
            create_date DATE,
            course_id INT REFERENCES course(course_id));"""
    
    lesson_table = f"""
        CREATE TABLE lesson(
            lesson_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            modul_id INT REFERENCES modul(modul_id),
            last_update TIMESTAMP DEFAULT now());"""
    
    payment_type_table = f"""
        CREATE TABLE payment_type(
            payment_type_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            last_update TIMESTAMP DEFAULT now());"""
    
    payment_table = f"""
        CREATE TABLE payment(
            payment_id SERIAL PRIMARY KEY,
            amount FLOAT,
            student_id INT REFERENCES student(student_id),
            course_id INT REFERENCES course(course_id),
            payment_type_id INT REFERENCES payment_type(payment_type_id),
            last_update TIMESTAMP DEFAULT now(),
            create_date DATE);"""
    

    dataTable = {
        "country_table": country_table,
        "city_table": city_table,
        "address_table": address_table,
        "user_table": user_table,
        "student_table": student_table,
        "mentor_table": mentor_table,
        "course_table": course_table,
        "course_student_table": course_student_table,
        "course_mentor_table": course_mentor_table,
        "speciality_table": speciality_table,
        "speciality_course_table": speciality_course_table,
        "modul_table": modul_table,
        "lesson_table": lesson_table,
        "payment_type_table": payment_type_table,
        "payment_table": payment_table
    }

    # for i in dataTable:
    #     print(f"{i} {base.Database.connect(dataTable[i], "create")}")

# if __name__ == "__main__":
#     createTables()
    