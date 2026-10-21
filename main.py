email = 'alice.johnson@company.com'
print(f'Email: {email}')

at_position = email.find('@')
print(f'Position of @: {at_position}')

username = email[:at_position]
print(f'Username: {username}')

has_at = '@' in email
print(f'Has @ symbol: {has_at}')

has_com = '.com' in email
print(f'Has .com: {has_com}')

messy_name = '  sARaH dAVis  '
print(f"Original name: '{messy_name}'")

clean_name = messy_name.strip().title()
print(f"Cleaned name: '{clean_name}'")

messy_email = '  SARAH.DAVIS@COMPANY.COM  '
clean_email = messy_email.strip().lower()
print(f"Original email: '{messy_email}'")
print(f"Cleaned email: '{clean_email}'")

name_badge = clean_name.upper()
print(f'Name badge: {name_badge}')

at_pos = clean_email.find('@')
email_user = clean_email[:at_pos]

print(f'Email: {clean_email}')
print(f'Username: {email_user}')

display_name = email_user.replace('.', ' ').title()
print(f'Display name: {display_name}')

phone = '123-456-7890'
phone_clean = phone.replace('-', '')
print(f'Phone with dashes: {phone}')
print(f'Phone without dashes: {phone_clean}')

full_address = '123 Main Street, Springfield, IL'
address_parts = full_address.split(', ')
print(f'Address parts: {address_parts}')

rejoined = ' | '.join(address_parts)
print(f'Rejoined: {rejoined}')

employee_code = 'EMP-2024-SD'
starts_with_emp = employee_code.startswith('EMP')
ends_with_com = clean_email.endswith('.com')

print(f'Code: {employee_code}')
print(f'Starts with EMP: {starts_with_emp}')
print(f'Clean email: {clean_email}')
print(f'Ends with .com: {ends_with_com}')

dot_count = clean_email.count('.')
dash_count = employee_code.count('-')

print(f'Dots in email: {dot_count}')
print(f'Dashes in code: {dash_count}')

# ============================================================
# My extension: interactive employee profile validator
# ============================================================

def show_result(label, is_valid):
    status = 'PASS' if is_valid else 'FAIL'
    print(f'{label}: {status}')


print('\n--- Employee Profile Validator ---')

raw_name = input('Full name: ')
raw_email = input('Email: ')
raw_phone = input('Phone (e.g. 123-456-7890): ')
raw_code = input('Employee code (e.g. EMP-2024-SD): ')
raw_department = input('Department: ')

# Clean the input
name = raw_name.strip().title()
email = raw_email.strip().lower()
phone = raw_phone.strip().replace('-', '').replace(' ', '')
code = raw_code.strip().upper()
department = raw_department.strip().title()

# Validate each field
name_valid = ' ' in name
email_valid = (
    email.count('@') == 1
    and email.find('@') > 0
    and email.endswith('.com')
)
phone_valid = phone.isdigit() and len(phone) == 10
code_valid = code.startswith('EMP') and code.count('-') == 2
department_valid = len(department) > 0

# Show results
print('\n--- Cleaned Profile ---')
print(f'Name: {name}')
print(f'Email: {email}')
print(f'Phone: {phone}')
print(f'Employee code: {code}')
print(f'Department: {department}')

print('\n--- Validation Results ---')
show_result('Name (first and last)', name_valid)
show_result('Email', email_valid)
show_result('Phone (10 digits)', phone_valid)
show_result('Employee code', code_valid)
show_result('Department', department_valid)

all_valid = (
    name_valid and email_valid and phone_valid
    and code_valid and department_valid
)
print(f'\nOverall: {"PROFILE VALID" if all_valid else "PROFILE INVALID"}')
