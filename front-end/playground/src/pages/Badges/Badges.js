import {React, useState, useEffect, useContext} from 'react';
// import { Card } from 'react-bootstrap'
import './Badges.css';
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
  CardSubtitle,
  CardText,
  ButtonGroup,
  Button,
  Badge
} from 'reactstrap';

import {Generic_Badges} from '../../PermanentComponents/Badges'

function Badges() {

    return (
    <div className="pp-badges-container">
        <Card style={{margin: '1rem'}} className="">
            <CardBody>
                <CardTitle tag="h5">
                    Generic Badges
                </CardTitle>
                <CardSubtitle className="text-muted" tag="h5">
                    If you have idea about badges, you can send <a href="mailto:squadgamebypluto@gmail.com">email</a> to us.
                </CardSubtitle>
                <div className="pp-badges-category-container">
                {Generic_Badges.length > 0 ? Generic_Badges.map(badge => {
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

export default Badges;
