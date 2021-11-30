def filter_visibility(user_db_data, serialized_user):
    visibility_attributes_mapping = {'email_visibility': 'email', 'name_visibility':'name', 'familyName_visibility': 'familyName', 
                                    'birthDate_visibility': 'birthDate', 'gender_visibility': 'gender'}
    
    for visibility, attribute in visibility_attributes_mapping.items():
        if not user_db_data[visibility]:
            try:
                del serialized_user[attribute]
            except KeyError:
                continue
    
    return serialized_user
