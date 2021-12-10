import {React, useState, Fragment} from 'react';
import './EventPage.css';

import {Tabs, Tab, TabContainer, TabContent} from 'react-bootstrap';

function EventPage(props) {
  const [tabName, setTabName] = useState('home');
  const changeTab = (name) => {
      setTabName(name)
  }

  return (
      <div className="event-container">
        <Tabs
        id="tab-eg"
        activeKey={tabName}
        onSelect={(k) => setTabName(k)}
        className="tabs-title"
        >
        {/* <TabContainer> */}
            <Tab eventKey="home" title="Home">
                <div className="tab-contentt">home</div>
            </Tab>
            <Tab eventKey="profile" title="Profile">
                <div>profile</div>
            </Tab>
            <Tab eventKey="contact" title="Contact">
                <div>contact</div>
            </Tab>
        {/* </TabContainer> */}
        </Tabs>
    </div>
  );
}

export default EventPage;