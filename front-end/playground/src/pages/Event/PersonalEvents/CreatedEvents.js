import {React, useState, Fragment, useEffect} from 'react';
import './CreatedEvents.css';
import {getCreatedEvents} from '../../../services/Events';
import {changeCreatedEventsVisibility} from '../../../services/User';
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
  ButtonGroup, 
  Button
} from 'reactstrap';

import {Data} from './MockData'

function CreatedEvents(props) {
    const [events, setEvents] = useState([]);
    const [badgeVisibility, setBadgeVisibility] = useState(true);
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
        <>
        <div style={{marginRight: '1rem', marginTop: '1rem'}}>
            <ButtonGroup style={{float: 'right', marginBottom: '0.4rem'}}>
                <Button
                    active={badgeVisibility}
                    outline
                    color="secondary"
                    onClick={() => {changeCreatedEventsVisibility(true); setBadgeVisibility(true)}}
                    size="sm"
                >
                    Show
                </Button>
                <Button
                    active={!badgeVisibility}
                    outline
                    color="secondary"
                    onClick={() => {changeCreatedEventsVisibility(false); setBadgeVisibility(false)}}
                    size="sm"
                >
                    Hide
                </Button>
            </ButtonGroup>
            <div style={{color: 'white'}}>.</div>
        </div>
        <div className="personal-events-container">
            
            {events.length > 0 ? events.map(event => {
                return (
                    <CardComponent event={event}/>
                )
            }) : <div style={{padding: '50px'}}>You did not create any events</div>
            }
        </div>
        
        </>
    )
}

export {CreatedEvents};
