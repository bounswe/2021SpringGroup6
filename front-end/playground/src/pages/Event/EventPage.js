import {React, useState, Fragment} from 'react';
import {Tabs, Tab} from 'react-bootstrap';

function EventPage(props) {
  const [tabName, setTabName] = useState('home');
  const changeTab = (name) => {
      setTabName(name)
  }

  return (
      <Fragment>
        <Tabs
        id="controlled-tab-example"
        activeKey={tabName}
        onSelect={(k) => setTabName(k)}
        className="mb-3"
        >
            <Tab eventKey="home" title="Home">
                <div>home</div>
            </Tab>
            <Tab eventKey="profile" title="Profile">
                <div>profile</div>
            </Tab>
            <Tab eventKey="contact" title="Contact">
                <div>contact</div>
            </Tab>
        </Tabs>
        <Tabs
        id="controlled-tab-example"
        activeKey={tabName}
        onSelect={(k) => setTabName(k)}
        className="mb-3"
        >
            <Tab eventKey="home" title="Home">
                <div>home</div>
            </Tab>
            <Tab eventKey="profile" title="Profile">
                <div>profile</div>
            </Tab>
            <Tab eventKey="contact" title="Contact">
                <div>contact</div>
            </Tab>
        </Tabs>
        <Tabs
        id="controlled-tab-example"
        activeKey={tabName}
        onSelect={(k) => setTabName(k)}
        className="mb-3"
        >
            <Tab eventKey="home" title="Home">
                <div>home</div>
            </Tab>
            <Tab eventKey="profile" title="Profile">
                <div>profile</div>
            </Tab>
            <Tab eventKey="contact" title="Contact">
                <div>contact</div>
            </Tab>
        </Tabs>
        <Tabs
        id="controlled-tab-example"
        activeKey={tabName}
        onSelect={(k) => setTabName(k)}
        className="mb-3"
        >
            <Tab eventKey="home" title="Home">
                <div>home</div>
            </Tab>
            <Tab eventKey="profile" title="Profile">
                <div>profile</div>
            </Tab>
            <Tab eventKey="contact" title="Contact">
                <div>contact</div>
            </Tab>
        </Tabs>
        <Tabs
        id="controlled-tab-example"
        activeKey={tabName}
        onSelect={(k) => setTabName(k)}
        className="mb-3"
        >
            <Tab eventKey="home" title="Home">
                <div>home</div>
            </Tab>
            <Tab eventKey="profile" title="Profile">
                <div>profile</div>
            </Tab>
            <Tab eventKey="contact" title="Contact">
                <div>contact</div>
            </Tab>
        </Tabs>
        <Tabs
        id="controlled-tab-example"
        activeKey={tabName}
        onSelect={(k) => setTabName(k)}
        className="mb-3"
        >
            <Tab eventKey="home" title="Home">
                <div>home</div>
            </Tab>
            <Tab eventKey="profile" title="Profile">
                <div>profile</div>
            </Tab>
            <Tab eventKey="contact" title="Contact">
                <div>contact</div>
            </Tab>
        </Tabs>
    </Fragment>
  );
}

export default EventPage;