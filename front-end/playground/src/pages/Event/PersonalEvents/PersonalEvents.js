import {React, useState, Fragment} from 'react';
import './PersonalEvents.css';

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
  CardBody, 
  CardTitle, 
  CardText,
} from 'reactstrap';

import {Data} from './MockData'
import { EventModal } from '../EventModal';

function PersonalEvents(props) {
    const [events, setEvents] = useState(Data || []);
    // const location = useLocation();
    // console.log('location\n', location)

    return (
        <div className="personal-events-container">
            <Routes //location={(location.state && location.state.backgroundLocation) || location}
            >
                <Route path="modal/:id" element={<EventModal />} />
            </Routes>
            {events.map(event => {
                return (
                    <Fragment key={event.id}>
                        <Link 
                            key={event.id}
                            to={`/event/modal/${event.id}`} 
                            // state={{ backgroundLocation: location }}
                        >
                            <Card className="event-card" onClick={() => {}}>
                                <CardImg
                                    alt="Card image cap"
                                    src="https://picsum.photos/318/180"
                                    top
                                    width="100%"
                                />
                                <CardBody>
                                    <CardTitle tag="h5">
                                        {event.title}
                                    </CardTitle>
                                    <CardText>
                                        {event.description}
                                    </CardText>
                                    <CardText>
                                        {(event.participants && event.participantslength) || null }
                                    </CardText>
                                </CardBody>
                            </Card>
                        </Link>
                    </Fragment>
                )
            })}
        </div>
    )
}

export {PersonalEvents};
