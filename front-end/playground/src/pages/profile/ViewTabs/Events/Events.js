import {React, useState, Fragment, useEffect} from 'react';
import './Events.css';
import {getOtherUsersCreatedEvents} from '../../../../services/Events';
import {changeCreatedEventsVisibility} from '../../../../services/User';
import { CardComponent } from './CardComponent';

import { Link, useLocation, Routes, Route, useParams } from "react-router-dom";

import {
  Tabs, 
  Tab, 
  TabContainer, 
  TabContent, 
  TabPane, 
  Nav, 
  NavItem, 
  NavLink, 
  Card, 
  CardImg,
  CardHeader,
  CardFooter,
  CardBody, 
  CardTitle,
  CardSubtitle, 
  CardText,
  ButtonGroup, 
  Button
} from 'reactstrap';

function UserEvents(props) {
    const [events, setEvents] = useState([]);
    const [badgeVisibility, setBadgeVisibility] = useState(true);
    const user_id = parseInt(useParams().id);
    const {createdEventVisibility} = props;

    useEffect(() =>{
        if (createdEventVisibility) {
            getOtherUsersCreatedEvents(user_id)
            .then((response) => {
                setEvents(response.items)
            })
            .catch((error) => {})
        } 
    }, [createdEventVisibility])

    return (
        <>
        <div className="personal-events-container">
            
            {events.length > 0 ? events.map(event => {
                return (
                    <CardComponent event={event}/>
                )
            }) : <div style={{padding: '50px'}}>User did not create any events</div>
            }
        </div>
        
        </>
    )
}

export default UserEvents;
