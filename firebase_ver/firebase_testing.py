from firebase import firebase
import requests

firebase = firebase.FirebaseApplication('https://testunessayproject.firebaseio.com/', None)


# data = {
#             'name' : 'USERPROFILE1',
#             'keystroke'  : 'ajodsoiasdfiao',
#             'passwords' : 'passwords',
#             'potential password' : 'potential password',
#             'username' : 'username',
#             'all strings': 'all strings'
#         }    

# firebase.post('person', data, {'print': 'silent'})

result = firebase.get('person', None)
print(result)
                 
# for i in result:
#     if (result[i]['name']) == 'USERPROFILE1':
#         firebase.delete('person', i)
# firebase.post('person', data, {'print': 'silent'})

