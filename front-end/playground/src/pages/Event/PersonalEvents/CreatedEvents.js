import {React, useState, Fragment, useEffect} from 'react';
import './CreatedEvents.css';
import {getCreatedEvents} from '../../../services/Events';
import { CardComponent } from './CardComponent';

import { Link, useLocation, Routes, Route } from "react-router-dom";

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
} from 'reactstrap';

import {Data} from './MockData'

function CreatedEvents(props) {
    const [events, setEvents] = useState([]);
    useEffect(() =>{
        if (events.length === 0) {
            getCreatedEvents()
            .then((response) => {
                setEvents(response.items)
            })
            .catch((error) => {})
        } 
    }, [])

    return (
        <div className="personal-events-container">
            {events.length > 0 ? events.map(event => {
                return (
                    <CardComponent event={event}/>
                )
            }) : <div style={{padding: '50px'}}>You did not create any events</div>
            }
        </div>
    )
}

export {CreatedEvents};
