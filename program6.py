#Program6 :

def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name:  {kwargs['student_name']}")
    
    if 'student_name' and 'student_class' in kwargs:
            print(f"\nStudent Name:  {kwargs['student_name']}")
            print(f"Student Class:  {kwargs['student_class']}")


student_data(student_id="2005693", student_name="Sarah")

student_data(student_id="2005693", student_name="Sarah", student_class ="VII")



