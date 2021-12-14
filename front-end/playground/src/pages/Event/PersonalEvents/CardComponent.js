import {React, useState, Fragment, useEffect} from 'react';
import './CardComponent.css';
import {getCreatedEvents} from '../../../services/Events';

import { Link, useLocation, Routes, Route } from "react-router-dom";
import { Map, Marker } from "pigeon-maps";

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

function CardComponent(props) {
    const {event} = props;
    const {latitude, longitude} = event.location.geo;

    return (
        // <Link 
        //     key={event.event_id}
        //     to={`/event/${event.event_id || event['@id'] || ''}`} 
        //     // state={{ backgroundLocation: location }}
        // >
            <Card className="event-card" onClick={() => {}}>
                <Map height={300} defaultCenter={[latitude, longitude]} defaultZoom={17}>
                    <Marker width={50} anchor={[latitude, longitude]}>
                        <img src="https://static3.depositphotos.com/1000868/261/v/950/depositphotos_2614173-stock-illustration-beach-ball.jpg" width={40} height={37} alt="Pigeon!" />
                    </Marker>
                </Map>
                <Link 
                    to={`/event/${event.event_id || event['@id'] || ''}`}
                    className="card-body-hover"
                >
                <CardBody>
                    <CardTitle tag="h5">
                        {event.name}
                    </CardTitle>
                    <CardSubtitle className="mb-2 text-muted" tag="h6">
                        {event.sport}
                    </CardSubtitle>
                    <CardText>
                        {(event.location && event.location.address) || 'Unknown location'}
                    </CardText>
                    <CardText>
                        {(event.participants && event.participantslength) || null }
                    </CardText>
                </CardBody>
                <CardFooter>
                    <div style={{display: 'flex', flexDirection: 'row', justifyContent: 'space-between'}}>
                        <span>{(new Date(event.startDate).toString()).split(' GMT')[0]}</span>
                        {/* {event.maximumAttendeeCapacity ? 
                            <span style={{paddingLeft: '1rem'}} >
                                Max: {event.maximumAttendeeCapacity}
                            </span> 
                            : 
                            null
                        } */}
                    </div>                                     
                </CardFooter>
                </Link>
            </Card>
        // </Link>
    )
}

export {CardComponent};
