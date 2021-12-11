import {React, useState, Fragment} from 'react';
import './PersonalEvents.css';

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

function PersonalEvents(props) {
    const [events, setEvents] = useState(Data || []);

    return (
        <div className="personal-events-container">
            {events.map(event => {
                return (
                    <Fragment key={event.id}>
                    <Card className="event-card">
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
                    </Fragment>
                )
            })}
        </div>
    )
}

export {PersonalEvents};
