import {React, useState, Fragment} from 'react';
import './Profile.css';

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

// import {DiscussionPage} from './Discussion/DiscussionPage';
import PersonalInfo from './Tabs/PersonalInfo/PersonalInfo';
import Badges_Tab from './Tabs/Badges/Badges';

function Profile(props) {
  const [tabName, setTabName] = useState('Personal-Info');
  const changeTab = (name) => {
      setTabName(name)
  }

  return (
      <div className="profile-page-container">
        <Nav tabs justified className="profile-page-nav">
            <NavItem>
                <NavLink
                active={tabName === 'Personal-Info'}
                onClick={() => {
                    changeTab('Personal-Info')
                }}
                >
                Personal Info
                </NavLink>
            </NavItem>
            <NavItem>
                <NavLink
                active={tabName === 'Badges'}
                onClick={() => {
                    changeTab('Badges')
                }}
                >
                Badges
                </NavLink>
            </NavItem>
            {/* <NavItem>
                <NavLink
                active={tabName === 'Discussion'}
                onClick={() => {
                    changeTab('Discussion')
                }}
                >
                Discussion
                </NavLink>
            </NavItem> */}
        </Nav>

        {/* pay attention to custom class. it makes the container a flexbox. if flexbox does not work for you, please contact with the author */}
        <TabContent activeTab={tabName} className={`custom-tab-content-pp-general custom-tab-content-${tabName}-settings`}>
            <TabPane tabId='Personal-Info'>
              <PersonalInfo/>
            </TabPane>
            <TabPane tabId="Badges">
              <Badges_Tab/>
            </TabPane>
            {/* <TabPane tabId="Discussion">
              <DiscussionPage/>
            </TabPane> */}
        </TabContent>
    </div>
  );
}

export default Profile;
