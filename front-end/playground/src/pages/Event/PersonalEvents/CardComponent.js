import {React, useState, Fragment, useEffect} from 'react';
import './CardComponent.css';
import {getCreatedEvents} from '../../../services/Events';

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

function CardComponent(props) {
    const {event} = props;
    return (
        <Link 
            key={event.event_id}
            to={`/event/${event.event_id}`} 
            // state={{ backgroundLocation: location }}
        >
            <Card className="event-card" onClick={() => {}}>
                <CardImg
                    alt="Card image cap"
                    src="https://picsum.photos/250/120"
                    top
                    width="100%"
                />
                <CardBody>
                    <CardTitle tag="h5">
                        {event.name}
                    </CardTitle>
                    <CardSubtitle className="mb-2 text-muted" tag="h6">
                        {event.sport}
                    </CardSubtitle>
                    <CardText>
                        {event.description}
                    </CardText>
                    <CardText>
                        {(event.participants && event.participantslength) || null }
                    </CardText>
                </CardBody>
                <CardFooter>
                    <div style={{display: 'flex', flexDirection: 'row', justifyContent: 'space-between'}}>
                        <span>{event.startDate}</span>
                        <span>Max: {event.maximumAttendeeCapacity}</span>
                    </div>                                     
                </CardFooter>
            </Card>
        </Link>
    )
}

export {CardComponent};
