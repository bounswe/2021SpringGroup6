import {React, useState, Fragment} from 'react';
import './EventPage.css';

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

import {DiscussionPage} from './Discussion/DiscussionPage';
import {PersonalEvents} from './PersonalEvents/PersonalEvents';

function EventPage(props) {
  const [tabName, setTabName] = useState('Event');
  const changeTab = (name) => {
      setTabName(name)
  }

  return (
      <div className="event-container">
        <Nav tabs justified className="event-nav">
            <NavItem>
                <NavLink
                active={tabName === 'Event'}
                onClick={() => {
                    changeTab('Event')
                }}
                >
                Event
                </NavLink>
            </NavItem>
            <NavItem>
                <NavLink
                active={tabName === 'Participation'}
                onClick={() => {
                    changeTab('Participation')
                }}
                >
                Participation
                </NavLink>
            </NavItem>
            <NavItem>
                <NavLink
                active={tabName === 'Discussion'}
                onClick={() => {
                    changeTab('Discussion')
                }}
                >
                Discussion
                </NavLink>
            </NavItem>
        </Nav>

        {/* pay attention to custom class. it makes the container a flexbox. if flexbox does not work for you, please contact with the author */}
        <TabContent activeTab={tabName} className={`custom-tab-content-${tabName}`}>
            <TabPane tabId='Event'>
              <PersonalEvents/>
            </TabPane>
            <TabPane tabId="Participation">
              <div>Participation</div>
            </TabPane>
            <TabPane tabId="Discussion">
              <DiscussionPage/>
            </TabPane>
        </TabContent>
    </div>
  );
}

export default EventPage;