from ..controllers.guest import Guest

def create_mock_user(user_info):
    guest= Guest(user_info['identifier'], user_info['password'])
    guest.register(user_info)

