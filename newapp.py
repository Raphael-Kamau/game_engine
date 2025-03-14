
patient_first_name = input('Patient First Name >>> ')
patient_second_name = input('Patient Second Name >>> ')
birth_year = input('Birth Year >>> ')
current_year = str(2025)

if birth_year >= current_year:
    print('''
    Please enter your accurate birth year❗❗❗
    ''')
    print("Invalid input for birth year. Please enter a valid year.")
else:
    print(f'''
    ❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤

    Welcome to Loyal Hospital, {patient_first_name}

    ❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤
    ''')

patient_status = input('Are you a new patient here? (yes/no) ').lower()
if patient_status == 'no':
   print(f'''
   ----------------------------------------------------------------

   Worry not {patient_first_name}, welcome back to Loyal Hospital.
   You shall be attended to as soon as possible...

   ----------------------------------------------------------------''')
elif patient_status == 'yes':
     print(f'''
     ----------------------------------------------------------------

     Have no worries {patient_first_name}, you shall be attended to as soon as possible

     ----------------------------------------------------------------''')
else:
     print(f'''
     ----------------------------------------------------------------

     Welcome {patient_first_name} to Loyal Hospital, your best health care institution.
     You shall be attended to as soon as possible...

     ----------------------------------------------------------------
     ''')


