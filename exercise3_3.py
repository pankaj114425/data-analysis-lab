Student = { 'UE183001': 'Ashish', 'UE183002': 'Bhavya', 'UE183003': 'Tanya', 
            'UE183004': 'John', 'UE183005': 'yes', 'UE183006': 'Manav', 
            'UE183007': 'chahak', 'UE183008': 'Dinesh', 'UE183009': 'Saurabh', 
            'UE183010': 'Devesh'}

Marks = [('UE183001', 'CS', 94 ), ('UE183002', 'CS', 64 ), ('UE183001', 'RV', 94), ('UE183002', 'CS', 74), 
  ('UE183003', 'CS', 64), ('UE183004', 'CS', 74), ('UE183005', 'RV', 84), ('UE183006', 'CS', 94), 
  ('UE183007', 'RV', 64), ('UE183008', 'CS', 74), ('UE183009', 'RV', 84), ('UE183010', 'CS', 94)]
  
total_marks = {}  # Create an empty dictionary to store the total marks of each student

# Iterate through the marks list and add the marks to the total_marks dictionary
for roll_number, subject, marks in Marks:
    if roll_number in total_marks:
        total_marks[roll_number] += marks
    else:
        total_marks[roll_number] = marks

for roll_number, marks in total_marks.items():  # print total marks and full name
    print(f'{Student[roll_number]} secured {marks} marks')
