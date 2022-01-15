import {React, useState, useEffect, useContext} from 'react';
import axios from 'axios';
import {useParams} from 'react-router-dom'

import './ProfileView.css';
import {UserContext} from '../../UserContext';



// import { Card } from 'react-bootstrap'
import SportNames from '../../PermanentComponents/SportNames.js';
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


import PersonalInfo from './ViewTabs/PersonalInfo/PersonalInfo';
import Badges_Tab from './ViewTabs/Badges/Badges';
import UserEvents from './ViewTabs/Events/Events';

import {getOneUserInfo} from '../../services/User';

function Profile() {
    const [tabName, setTabName] = useState('Personal-Info');
    const changeTab = (name) => {
        setTabName(name)
    }

    const [badgeVisibility, setBadgeVisibility] = useState(false);
    const [createdEventVisibility, setCreatedEventVisibility] = useState(false);
    

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
            <NavItem>
                <NavLink
                active={tabName === 'Events'}
                onClick={() => {
                    changeTab('Events')
                }}
                >
                Events
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
              <PersonalInfo 
                setBadgeVisibility={setBadgeVisibility} 
                setCreatedEventVisibility={setCreatedEventVisibility}
                />
            </TabPane>
            <TabPane tabId="Badges">
              <Badges_Tab badgeVisibility={badgeVisibility}/>
            </TabPane>
            <TabPane tabId="Events">
              <UserEvents createdEventVisibility={createdEventVisibility} />
            </TabPane>
            {/* <TabPane tabId="Discussion">
              <DiscussionPage/>
            </TabPane> */}
        </TabContent>
    </div>
    )
}

export default Profile;
