import {React, useState, useEffect} from 'react';
import './EventDiscussionPage.css';
import {Button} from 'reactstrap';
import {Link} from 'react-router-dom';
import { Map, Marker } from "pigeon-maps";
import {getEventDiscussion, postEventDiscussion} from '../../../services/Events';


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
    CardHeader,
    CardFooter,
    CardBody, 
    CardTitle,
    CardSubtitle, 
    CardText,
  } from 'reactstrap';

function EventDiscussionPage(props) {
    const {eventInfo, isLoading} = props;
    const localData = JSON.parse(localStorage.getItem('user'));
    console.log('BURDAAAA')
    console.log(eventInfo)


    function participate() {
        getEventDiscussion(eventInfo.event_id);
    }

    return (
        <>
        <div>
            <Button
                color="secondary"
                onClick={participate}
            >
                Show event discussions
            </Button>
        </div>
        </>
    )
}

export {EventDiscussionPage}