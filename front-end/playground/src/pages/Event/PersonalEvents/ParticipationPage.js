import {React, useState, Fragment, useContext, useEffect} from 'react';
import './ParticipationPage.css';
import {UserContext} from '../../../UserContext';
import {getUserInteresteds, getUserAccepteds, getUserSpectatings} from '../../../services/User';
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
  CardGroup,
  Card, 
  CardImg, 
  CardBody, 
  CardTitle, 
  CardText,
} from 'reactstrap';

import {Data} from './MockData';


function ParticipationPage(props) {
    const {user, setUser} = useContext(UserContext);
    const {user_id} = user;
    const [participationRequestedEvents, setParticipationRequestedEvents] = useState([]);
    const [acceptedEvents, setAcceptedEvents] = useState([]);
    const [spectatorEvents, setSpectatorEvents] = useState([]);
    useEffect(() =>{
        if (participationRequestedEvents.length === 0) {
            getUserInteresteds()
            .then((response) => {
                setParticipationRequestedEvents(response.additionalProperty.value)
            })
            .catch((error) => {})
        }
        if (acceptedEvents.length === 0) {
            getUserAccepteds()
            .then((response) => {
                setAcceptedEvents(response.additionalProperty.value)
            })
            .catch((error) => {})
        }
        if (spectatorEvents.length === 0) {
            getUserSpectatings()
            .then((response) => {
                setSpectatorEvents(response.additionalProperty.value)
            })
            .catch((error) => {})
        }
    }, [])

    return (
        <div className="personal-events-container">
            <Card style={{margin: '1rem'}} className="paticipations-events-element">
                <CardBody>
                    <CardTitle tag="h5">
                        Events You Sent Participation Request
                    </CardTitle>
                    <div className="participation-group-container">
                    {participationRequestedEvents.length > 0 ? participationRequestedEvents.map(event => {
                        return (
                            <CardComponent event={event} key={event.event_id || event['@id']} />
                        )
                    }) : <div style={{padding: '50px'}}>You have no pending requests.</div>
                    }
                    </div>
                </CardBody>
            </Card>
            <Card style={{margin: '1rem'}} className="paticipations-events-element">
                <CardBody>
                    <CardTitle tag="h5">
                        Events You Accepted
                    </CardTitle>
                    <div className="participation-group-container">
                    {acceptedEvents.length > 0 ? acceptedEvents.map(event => {
                        return (
                            <CardComponent event={event}/>
                        )
                    }) : <div style={{padding: '50px'}}>You have not been accepted to any event yet.</div>
                    }
                    </div>
                </CardBody>
            </Card>
            
            <Card style={{margin: '1rem'}} className="paticipations-events-element">
                <CardBody>
                    <CardTitle tag="h5">
                        Events You Are a Spectator
                    </CardTitle>
                    <div className="participation-group-container">
                    {spectatorEvents.length > 0 ? spectatorEvents.map(event => {
                        return (
                            <CardComponent event={event}/>
                        )
                    }) : <div style={{padding: '50px'}}>You have not decide to watch any event yet.</div>
                    }
                    </div>
                </CardBody>
            </Card>
        </div>
    )
}

export {ParticipationPage};
