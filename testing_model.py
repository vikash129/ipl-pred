import pickle as p
#model = p.load(open('ipl_tree_model.dat' , 'rb'))
#type = <class '_io.BufferedReader'>

encrypt = p.load(open('encrypted_data.dat' , 'rb'))
decrypt = p.load(open('decrypted_data.dat' , 'rb'))


#print(p.load(model))
print(encrypt)
print(decrypt)

#encrypt
'''
{'Chennai Super Kings': 74, 'Kolkata Knight Riders': 76, 'Royal Challengers Bangalore': 80, 'Kings XI Punjab': 79, 'Rajasthan Royals': 78,
'Mumbai Indians': 75, 'Sunrisers Hyderabad': 77, 'Delhi Capitals': 81, 'Kolkata': 16, 'Mumbai': 17, 'Chennai': 18, 'Chandigarh': 19, 'Abu Dhabi': 20,
'Jaipur': 21, 'Dubai': 22, 'Bangalore': 23, 'Hyderabad': 24, 'Delhi': 25, 'Bengaluru': 26, 'Sharjah': 27, 'Durban': 28, 'Ahmedabad': 29, 'Cape Town': 30,
'Ranchi': 31, 'Centurion': 32, 'Pune': 33, 'Port Elizabeth': 34, 'Johannesburg': 35, 'Visakhapatnam': 36, 'Eden Gardens': 37, 'MA Chidambaram Stadium,
Chepauk': 38, 'Wankhede Stadium': 39, 'Sheikh Zayed Stadium': 40, 'Dubai International Cricket Stadium': 41, 'Sawai Mansingh Stadium': 42,
'Punjab Cricket Association Stadium, Mohali': 43, 'M Chinnaswamy Stadium': 44, 'Rajiv Gandhi International Stadium, Uppal': 45, 'Feroz Shah Kotla': 46,
'Sharjah Cricket Stadium': 47, 'M.Chinnaswamy Stadium': 48, 'Brabourne Stadium': 49, 'Kingsmead': 50, 'Sardar Patel Stadium, Motera': 51,
'Punjab Cricket Association IS Bindra Stadium, Mohali': 52, 'Dr DY Patil Sports Academy': 53, 'JSCA International Stadium Complex': 54,
'Newlands': 55, 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium': 56,
'New Wanderers Stadium': 57, 'Maharashtra Cricket Association Stadium': 58, "St George's Park": 59, 'SuperSport Park': 60, 'field': 61, 'bat': 62,
'runs': 63, 'wickets': 64, 'tie': 65, 'N': 82, 'Y': 83}'''


#decrypted
'''
{74: 'Chennai Super Kings', 76: 'Kolkata Knight Riders', 80: 'Royal Challengers Bangalore', 79: 'Kings XI Punjab', 78: 'Rajasthan Royals',
75: 'Mumbai Indians', 77: 'Sunrisers Hyderabad', 81: 'Delhi Capitals', 16: 'Kolkata', 17: 'Mumbai', 18: 'Chennai', 19: 'Chandigarh', 20: 'Abu Dhabi',
21: 'Jaipur', 22: 'Dubai', 23: 'Bangalore', 24: 'Hyderabad', 25: 'Delhi', 26: 'Bengaluru', 27: 'Sharjah', 28: 'Durban', 29: 'Ahmedabad', 30: 'Cape Town',
31: 'Ranchi', 32: 'Centurion', 33: 'Pune', 34: 'Port Elizabeth', 35: 'Johannesburg', 36: 'Visakhapatnam', 37: 'Eden Gardens', 38: 'MA Chidambaram Stadium,
Chepauk', 39: 'Wankhede Stadium', 40: 'Sheikh Zayed Stadium', 41: 'Dubai International Cricket Stadium', 42: 'Sawai Mansingh Stadium',
43: 'Punjab Cricket Association Stadium, Mohali', 44: 'M Chinnaswamy Stadium', 45: 'Rajiv Gandhi International Stadium, Uppal',
46: 'Feroz Shah Kotla', 47: 'Sharjah Cricket Stadium', 48: 'M.Chinnaswamy Stadium', 49: 'Brabourne Stadium', 50: 'Kingsmead',
51: 'Sardar Patel Stadium, Motera', 52: 'Punjab Cricket Association IS Bindra Stadium, Mohali', 53: 'Dr DY Patil Sports Academy',
54: 'JSCA International Stadium Complex', 55: 'Newlands', 56: 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium', 57: 'New Wanderers Stadium',
58: 'Maharashtra Cricket Association Stadium', 59: "St George's Park", 60: 'SuperSport Park', 61: 'field', 62: 'bat', 63: 'runs', 64: 'wickets',
65: 'tie', 82: 'N', 83: 'Y'}
'''

