import React, {useEffect, useState} from "react";
import './style.css'
import {getNotifications} from "../../services/User";

const Notifications = (props) => {

    const [notifications, setNotifications] = useState([])
    useEffect(() => {

        getNotifications().then((response) => {
            console.log('response - ', response)
            setNotifications(response.Items)
        })
    },[])

    return (
        <div className="notification-container d-flex flex-column">
            <h1 className="m-5">NOTIFICATIONS</h1>

            {
                notifications && notifications.length >= 1 ? notifications.map(notification => (
                        <div>
                            <p>{notification.description}</p>
                            <h5>{notification.date}</h5>
                        </div>
                    )) :
                    <h2>No Notification !</h2>
            }
        </div>
    )

}


export default Notifications

