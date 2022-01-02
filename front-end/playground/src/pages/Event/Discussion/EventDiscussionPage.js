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
    const {eventDiscussionInfo, isLoading} = props;
    const localData = JSON.parse(localStorage.getItem('user'));
    console.log('BURDAAAA')
    console.log(eventDiscussionInfo)

    let buttonActive = (() => {
        console.log(eventDiscussionInfo)
        return true;
    })();



    function participate() {
        postEventDiscussion(eventDiscussionInfo.event_id);
    }

    return (
        <>
        <div>
        <CardSubtitle className="text-muted" tag="h5" style={{marginTop: '0'}} >
                                    Sport: {eventDiscussionInfo}
                                </CardSubtitle>
        </div>
        </>
    )
}

export {EventDiscussionPage}