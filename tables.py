import mainDB
import classes


def countryTable():
    move = input("""
        1.Insert
        2.Select
        3.Delete
        4.Update
        0.Back
>>> """)

    if move == "1":
        name = input("Name: ")
        country = classes.Country(name)
        print(country.insert())
        return countryTable()

    elif move == "2":
        for i in classes.Country.select("country"):
            print(i)
        return countryTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "country_id":
            print(classes.Country.delete(column, data))
        else:
            print(classes.Country.deleteID(column, data))
        return countryTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.Country.update(column, data, idColumn, id))
        return countryTable()

    elif move == "0":
        return mainDB.main()

    else:
        print("ERROR!!!")
        return countryTable()


def cityTable():
    move = input("""
            1.Insert
            2.Select
            3.Delete
            4.Update
            0.Back
    >>> """)

    if move == "1":
        name = input("Name: ")
        countryId = input("Country ID: ")
        city = classes.City(name, countryId)
        print(city.insert())
        return cityTable()

    elif move == "2":
        for i in classes.City.select("city"):
            print(i)
        return cityTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "city_id":
            print(classes.Country.delete(column, data, "city"))
        else:
            print(classes.Country.deleteID(column, data, "city"))
        return cityTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.Country.update(column, data, idColumn, id, "city"))
        return cityTable()

    elif move == "0":
        return mainDB.main()

    else:
        print("ERROR!!!")
        return cityTable()


def addressTable():
    move = input("""
            1.Insert
            2.Select
            3.Delete
            4.Update
            0.Back
    >>> """)

    if move == "1":
        name = input("Name: ")
        cityId = input("City ID: ")
        address = classes.Address(name, cityId)
        print(address.insert())
        return addressTable()

    elif move == "2":
        for i in classes.Address.select("address"):
            print(i)
        return addressTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "address_id":
            print(classes.Address.delete(column, data, "address"))
        else:
            print(classes.Address.deleteID(column, data, "address"))
        return addressTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.Address.update(column, data, idColumn, id, "address"))
        return addressTable()

    elif move == "0":
        return mainDB.main()

    else:
        print("ERROR!!!")
        return addressTable()


def userTable():
    move = input("""
            1.Insert
            2.Select
            3.Delete
            4.Update
            0.Back
    >>> """)

    if move == "1":
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        username = input("Username: ")
        password = input("Password: ")
        gmail = input("g-Mail: ")
        createDate = input("Create Date: ")
        users = classes.Users(firstName, lastName, username, password, gmail, createDate)
        print(users.insert())
        return userTable()

    elif move == "2":
        for i in classes.Users.select("users"):
            print(i)
        return userTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "user_id":
            print(classes.Users.delete(column, data, "users"))
        else:
            print(classes.Users.deleteID(column, data, "users"))
        return userTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.Users.update(column, data, idColumn, id, "users"))
        return userTable()

    elif move == "0":
        return mainDB.main()

    else:
        print("ERROR!!!")
        return userTable()


def studentTable():
    move = input("""
            1.Insert
            2.Select
            3.Delete
            4.Update
            0.Back
    >>> """)

    if move == "1":
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        username = input("Username: ")
        password = input("Password: ")
        gmail = input("g-Mail: ")
        createDate = input("Create Date: ")
        addressId = input("Address ID: ")
        student = classes.Student(firstName, lastName, username, password, gmail, createDate, addressId)
        print(student.insert())
        return studentTable()

    elif move == "2":
        for i in classes.Student.select("users"):
            print(i)
        return studentTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "student_id":
            print(classes.Student.delete(column, data, "student"))
        else:
            print(classes.Student.deleteID(column, data, "student"))
        return studentTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.Student.update(column, data, idColumn, id, "student"))
        return studentTable()

    elif move == "0":
        return mainDB.main()

    else:
        print("ERROR!!!")
        return studentTable()


def mentorTable():
    move = input("""
            1.Insert
            2.Select
            3.Delete
            4.Update
            0.Back
    >>> """)

    if move == "1":
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        username = input("Username: ")
        password = input("Password: ")
        gmail = input("g-Mail: ")
        createDate = input("Create Date: ")
        cityId = input("Address ID: ")
        mentor = classes.Mentor(firstName, lastName, username, password, gmail, createDate, cityId)
        print(mentor.insert())
        return mentorTable()

    elif move == "2":
        for i in classes.Mentor.select("users"):
            print(i)
        return mentorTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "mentor_id":
            print(classes.Mentor.delete(column, data, "mentor"))
        else:
            print(classes.Mentor.deleteID(column, data, "mentor"))
        return mentorTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.Mentor.update(column, data, idColumn, id, "mentor"))
        return mentorTable()

    elif move == "0":
        return mainDB.main()

    else:
        print("ERROR!!!")
        return mentorTable()


def courseTable():
    move = input("""
            1.Insert
            2.Select
            3.Delete
            4.Update
            0.Back
    >>> """)

    if move == "1":
        name = input("Name: ")
        description = input("Description: ")
        rating = input("Rating: ")
        price = input("Price: ")
        language = input("Language: ")
        createDate = input("Create Date: ")
        course = classes.Course(name, description, rating, price, language, createDate)
        print(course.insert())
        return courseTable()

    elif move == "2":
        for i in classes.Course.select("users"):
            print(i)
        return courseTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "course_id":
            print(classes.Course.delete(column, data, "course"))
        else:
            print(classes.Course.deleteID(column, data, "course"))
        return courseTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.Course.update(column, data, idColumn, id, "course"))
        return courseTable()

    elif move == "0":
        return mainDB.main()

    else:
        print("ERROR!!!")
        return courseTable()


def courseStudentTable():
    move = input("""
            1.Insert
            2.Select
            3.Delete
            4.Update
            0.Back
    >>> """)

    if move == "1":
        courseId = input("Course ID: ")
        studentId = input("Student ID: ")
        course = classes.CourseStudent(courseId, studentId)
        print(course.insert())
        return courseStudentTable()

    elif move == "2":
        for i in classes.CourseStudent.select("users"):
            print(i)
        return courseStudentTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "course_student_id":
            print(classes.CourseStudent.delete(column, data, "course_student"))
        else:
            print(classes.CourseStudent.deleteID(column, data, "course_student"))
        return courseStudentTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.CourseStudent.update(column, data, idColumn, id, "course_student"))
        return courseStudentTable()

    elif move == "0":
        return mainDB.main()

    else:
        print("ERROR!!!")
        return courseStudentTable()


def courseMentorTable():
    move = input("""
            1.Insert
            2.Select
            3.Delete
            4.Update
            0.Back
    >>> """)

    if move == "1":
        courseId = input("Course ID: ")
        mentorId = input("Mentor ID: ")
        course = classes.CourseMentor(mentorId, courseId)
        print(course.insert())
        return courseMentorTable()

    elif move == "2":
        for i in classes.CourseMentor.select("course_mentor"):
            print(i)
        return courseMentorTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "course_mentor_id":
            print(classes.CourseMentor.delete(column, data, "course_mentor"))
        else:
            print(classes.CourseMentor.deleteID(column, data, "course_mentor"))
        return courseMentorTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.CourseMentor.update(column, data, idColumn, id, "course_mentor"))
        return courseMentorTable()

    elif move == "0":
        return mainDB.main()

    else:
        print("ERROR!!!")
        return courseMentorTable()


def specialityTable():
    move = input("""
            1.Insert
            2.Select
            3.Delete
            4.Update
            0.Back
    >>> """)

    if move == "1":
        name = input("Name: ")
        description = input("Description: ")
        courseNumber = input("Number Course: ")
        createDate = input("Create Date: ")
        speciality = classes.Speciality(name, description, courseNumber, createDate)
        print(speciality.insert())
        return specialityTable()

    elif move == "2":
        for i in classes.Speciality.select("speciality"):
            print(i)
        return specialityTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "speciality_id":
            print(classes.Speciality.delete(column, data, "speciality"))
        else:
            print(classes.Speciality.deleteID(column, data, "speciality"))
        return specialityTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.Speciality.update(column, data, idColumn, id, "speciality"))
        return specialityTable()

    elif move == "0":
        return mainDB.main()

    else:
        print("ERROR!!!")
        return specialityTable()


def specialityCourseTable():
    move = input("""
                1.Insert
                2.Select
                3.Delete
                4.Update
                0.Back
        >>> """)

    if move == "1":
        courseId = input("Course ID: ")
        specialityId = input("Speciality ID: ")
        courseSpec = classes.SpecialityCourse(specialityId, courseId)
        print(courseSpec.insert())
        return specialityCourseTable()

    elif move == "2":
        for i in classes.SpecialityCourse.select("speciality_course"):
            print(i)
        return specialityCourseTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "speciality_course_id":
            print(classes.SpecialityCourse.delete(column, data, "speciality_course"))
        else:
            print(classes.SpecialityCourse.deleteID(column, data, "speciality_course"))
        return specialityCourseTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.SpecialityCourse.update(column, data, idColumn, id, "speciality_course"))
        return specialityCourseTable()

    elif move == "0":
        return mainDB.main()

    else:
        print("ERROR!!!")
        return specialityCourseTable()


def modulTable():
    move = input("""
                1.Insert
                2.Select
                3.Delete
                4.Update
                0.Back
        >>> """)

    if move == "1":
        name = input("Name: ")
        lessonNumber = input("Lesson Number: ")
        createDate = input("Create Date: ")
        courseId = input("Course ID: ")
        modul = classes.Modul(name, lessonNumber, createDate, courseId)
        print(modul.insert())
        return modulTable()

    elif move == "2":
        for i in classes.Modul.select("modul"):
            print(i)
        return modulTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "modul_id":
            print(classes.Modul.delete(column, data, "modul"))
        else:
            print(classes.Modul.deleteID(column, data, "modul"))
        return modulTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.Modul.update(column, data, idColumn, id, "modul"))
        return modulTable()

    elif move == "0":
        return mainDB.main()

    else:
        print("ERROR!!!")
        return modulTable()


def lessonTable():
    move = input("""
                1.Insert
                2.Select
                3.Delete
                4.Update
                0.Back
        >>> """)

    if move == "1":
        name = input("Name: ")
        modulId = input("Modul ID: ")
        lesson = classes.Lesson(name,modulId)
        print(lesson.insert())
        return lessonTable()

    elif move == "2":
        for i in classes.Lesson.select("lesson"):
            print(i)
        return lessonTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "lesson_id":
            print(classes.Lesson.delete(column, data, "lesson"))
        else:
            print(classes.Lesson.deleteID(column, data, "lesson"))
        return lessonTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.Lesson.update(column, data, idColumn, id, "lesson"))
        return lessonTable()

    elif move == "0":
        return mainDB.main()

    else:
        print("ERROR!!!")
        return lessonTable()


def paymentTypeTable():
    move = input("""
                1.Insert
                2.Select
                3.Delete
                4.Update
                0.Back
        >>> """)

    if move == "1":
        name = input("Name: ")
        paymentType = classes.PaymentType(name)
        print(paymentType.insert())
        return paymentTypeTable()

    elif move == "2":
        for i in classes.PaymentType.select("payment_type"):
            print(i)
        return paymentTypeTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "payment_type_id":
            print(classes.PaymentType.delete(column, data, "payment_type"))
        else:
            print(classes.PaymentType.deleteID(column, data, "payment_type"))
        return paymentTypeTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.PaymentType.update(column, data, idColumn, id, "payment_type"))
        return paymentTypeTable()

    elif move == "0":
        return mainDB.main()

    else:
        print("ERROR!!!")
        return paymentTypeTable()


def paymentTable():
    move = input("""
                1.Insert
                2.Select
                3.Delete
                4.Update
                0.Back
        >>> """)

    if move == "1":
        amount = input("Amount: ")
        studentId = input("student ID: ")
        courseId = input("Course ID: ")
        paymentTypeId = input("Payment Type ID: ")
        createDate = input("Create Date: ")
        payment = classes.Payment(amount, studentId, courseId, paymentTypeId, createDate)
        print(payment.insert())
        return paymentTable()

    elif move == "2":
        for i in classes.Payment.select("payment"):
            print(i)
        return paymentTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "payment_id":
            print(classes.Payment.delete(column, data))
        else:
            print(classes.Payment.deleteID(column, data))
        return paymentTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.Payment.update(column, data, idColumn, id))
        return paymentTable()

    elif move == "0":
        return mainDB.main()

    else:
        print("ERROR!!!")
        return paymentTable()
