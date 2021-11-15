import {React, Fragment, useState, useEffect} from 'react';
import { Card } from 'react-bootstrap'
import './Profile.css';

function Profile() {
    const [userAttributes, setUserAttributes] = useState({})
    useEffect(() => {
        // set user attributes
    }, [])

    return (
    <Fragment>
        <Card style={{minWidth: '50%', minHeight: '50%'}}></Card>
    </Fragment>
    )
}

export default Profile;
