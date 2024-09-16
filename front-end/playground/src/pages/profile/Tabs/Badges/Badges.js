import {React, useState, useEffect, useContext} from 'react';
// import { Card } from 'react-bootstrap'
import './Badges.css';
import {UserContext} from '../../../../UserContext';
import axios from 'axios';
import SportNames from '../../../../PermanentComponents/SportNames.js';
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
  ButtonGroup,
  Button,
  Badge
} from 'reactstrap';

import {getUserBadges, changeBadgeVisibility} from '../../../../services/User';

function Badges_Tab() {
    const [eventBadges, setEventBadges] = useState([]);
    const [userBadges, setUserBadges] = useState([]);
    const [badgeVisibility, setBadgeVisibility] = useState(true);
    
    
    useEffect(() => {
        if (!(eventBadges.length > 0 || userBadges.length > 0)) {
            getUserBadges()
            .then((response) => {
                console.log(response.additionalProperty);
                response.additionalProperty.forEach((badge_group) => {
                    if (badge_group.name === "event_badges") {
                        setEventBadges([...badge_group.value])
                    } else if (badge_group.name === "user_badges") {
                        setUserBadges([...badge_group.value])
                    }
                }) 
            })
            .catch((error) => {
                alert('Badges can not be loaded. You are redirecting to home page. Please try again later.');
                window.location.href = '/'
            });
        }
    }, []);

    useEffect(() => {console.log('eventBadges\n', eventBadges)}, [eventBadges])

    return (
    <div className="pp-badges-container">
        <div style={{marginBottom: '1rem', marginRight: '1rem'}}>
            <ButtonGroup style={{float: 'right', marginBottom: '0.4rem'}}>
                <Button
                    active={badgeVisibility}
                    outline
                    color="secondary"
                    onClick={() => {changeBadgeVisibility(true); setBadgeVisibility(true)}}
                    size="sm"
                >
                    Show
                </Button>
                <Button
                    active={!badgeVisibility}
                    outline
                    color="secondary"
                    onClick={() => {changeBadgeVisibility(false); setBadgeVisibility(false)}}
                    size="sm"
                >
                    Hide
                </Button>
            </ButtonGroup>
            <div style={{color: 'white'}}>.</div>
        </div>
        <Card style={{margin: '1rem'}} className="">
            <CardBody>
                <CardTitle tag="h5">
                    User Badges
                </CardTitle>
                <div className="pp-badges-category-container">
                {userBadges.length > 0 ? userBadges.map(badge => {
                    return (
                        <>
                            <Badge className="badge-pill" pill color="primary">
                                {badge.name}
                            </Badge>
                            {/* <CardComponent event={event}/> */}
                        </>
                    )
                }) : <div>You don't have any user badges.</div>
                }
                </div>
            </CardBody>
        </Card>
        <Card style={{margin: '1rem'}} className="">
            <CardBody>
                <CardTitle tag="h5">
                    Event Badges
                </CardTitle>
                <div className="pp-badges-category-container">
                {eventBadges.length > 0 ? eventBadges.map(badge => {
                    return (
                        <>
                            <Badge className="badge-pill" pill color="primary" >
                                {badge.name}
                            </Badge>
                            {/* <CardComponent event={event}/> */}
                        </>
                    )
                }) : <div>You don't have any event badges.</div>
                }
                </div>
            </CardBody>
        </Card>
    </div>
    )
}

export default Badges_Tab;
