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
    const [participationRequestedEvents, setParticipationRequestedEvents] = useState(Data.slice(0,3));
    const [acceptedEvents, setAcceptedEvents] = useState(Data.slice(0,3));
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
            <Card style={{margin: '1rem'}}>
                <CardBody>
                    <CardTitle tag="h5">
                        Events You Sent Participation Request
                    </CardTitle>
                    <CardGroup className="participation-groups">
                    {participationRequestedEvents.length > 0 ? participationRequestedEvents.map(event => {
                        return (
                            <CardComponent event={event}/>
                        )
                    }) : <div style={{padding: '50px'}}>You have no pending requests.</div>
                    }
                    </CardGroup>
                </CardBody>
            </Card>
            <Card style={{margin: '1rem'}}>
                <CardBody>
                    <CardTitle tag="h5">
                        Events You Accepted
                    </CardTitle>
                    <CardGroup className="participation-groups">
                    {acceptedEvents.length > 0 ? acceptedEvents.map(event => {
                        return (
                            <CardComponent event={event}/>
                        )
                    }) : <div style={{padding: '50px'}}>You have not been accepted to any event yet.</div>
                    }
                    </CardGroup>
                </CardBody>
            </Card>
            
            <Card style={{margin: '1rem'}}>
                <CardBody>
                    <CardTitle tag="h5">
                        Events You Are a Spectator
                    </CardTitle>
                    <CardGroup className="participation-groups">
                    {spectatorEvents.length > 0 ? spectatorEvents.map(event => {
                        return (
                            <CardComponent event={event}/>
                        )
                    }) : <div style={{padding: '50px'}}>You have not decide to watch any event yet.</div>
                    }
                    </CardGroup>
                </CardBody>
            </Card>
        </div>
    )
}

export {ParticipationPage};
