import {React, Fragment} from 'react';
import axios from 'axios';

function ActivityStream(props) {
    const localData = JSON.parse(localStorage.getItem('user'));
    const token = `Token ${props.token}`; // `Token ${localData.token}`;
    const getCreatedEvents = async () => {

        return axios({
            method: 'GET',
            url: `activitystream`,
            headers: {
                Authorization: token,
                Limit: 10,
            },
            data: {
            }
        })
            .then(response => {
            return response.data.body
            })
            .catch(error => {
            console.log(error)
            })
    }

    const streamObj = getCreatedEvents();
    console.log('streamObj\n', streamObj)

    return (
        <div>Hello!</div>
    )
}

export default ActivityStream;
