import {React, useState, useEffect, useContext} from 'react';
// import { Card } from 'react-bootstrap'
import './Badges.css';
import {UserContext} from '../../../../UserContext';
import axios from 'axios';
import SportNames from '../../../../PermanentComponents/SportNames.js';
import {useParams} from 'react-router-dom'
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

import {getOtherUsersBadges, changeBadgeVisibility} from '../../../../services/User';

function Badges_Tab(props) {
    const [eventBadges, setEventBadges] = useState([]);
    const [userBadges, setUserBadges] = useState([]);
    const user_id = parseInt(useParams().id);

    const {badgeVisibility} = props;
    
    useEffect(() => {
        if (badgeVisibility) {
            getOtherUsersBadges(user_id)
            .then((response) => {
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
                console.log(error)
                window.location.href = '/'
            });
        }
    }, [badgeVisibility]);

    return (
    <div className="pp-badges-container">
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
                }) : <div>The user don't have any user badges.</div>
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
                }) : <div>The user don't have any event badges.</div>
                }
                </div>
            </CardBody>
        </Card>
    </div>
    )
}

export default Badges_Tab;
