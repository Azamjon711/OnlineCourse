import tables


def main():
    print(" JADVALLAR ROYXATI: ")
    move = input(""""
                1.Country Table
                2.City Table
                3.Address Table
                4.User Table
                5.Student Table
                6.Mentor Table
                7.Course Table
                8.Course_Student Table
                9.Course_Mentor Table
                10.Speciality Table
                11.Speciality_Course Table
                12.Modul Table
                13.Lesson Table
                14.Payment_Type Table
                15.Payment Table
>>> """)

    if move == "1":
        return tables.countryTable()
    elif move == "2":
        return tables.cityTable()
    elif move == "3":
        return tables.addressTable()
    elif move == "4":
        return tables.userTable()
    elif move == "5":
        return tables.studentTable()
    elif move == "6":
        return tables.mentorTable()
    elif move == "7":
        return tables.courseTable()
    elif move == "8":
        return tables.courseStudentTable()
    elif move == "9":
        return tables.courseMentorTable()
    elif move == "10":
        return tables.specialityTable()
    elif move == "11":
        return tables.specialityCourseTable()
    elif move == "12":
        return tables.modulTable()
    elif move == "13":
        return tables.lessonTable()
    elif move == "14":
        return tables.paymentTypeTable()
    elif move == "15":
        return tables.paymentTable()
    else:
        print("ERROR!!!")
        return main()


if __name__ == "__main__":
    main()
