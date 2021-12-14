import {React, useState, useEffect} from 'react';
import './EventInformation.css';
import {Button} from 'reactstrap';
import {Link} from 'react-router-dom';
import { Map, Marker } from "pigeon-maps";

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

function EventInformation(props) {
    const {eventInfo, isLoading} = props;
    const localData = JSON.parse(localStorage.getItem('user'));
    const {latitude, longitude} = eventInfo.location.geo;

    let minimumAttendeeCapacity = null;
    for (let i = 0; i < eventInfo.additionalProperty.length; i++) {
        if (eventInfo.additionalProperty[i].name === 'minimumAttendeeCapacity') {
            minimumAttendeeCapacity = eventInfo.additionalProperty[i].value;
        }
    }

    let userSkill = 0;
    for (let i = 0; i < localData.profile.sports.length; i++) {
        if (localData.profile.sports[i].sport === eventInfo.sport){
            userSkill = localData.profile.sports[i].skill_level;
        }
    }

    return (
        <>
        { isLoading ?
            <div>Loading</div>
            :
            (
            <Card style={{margin: '1rem', minWidth: '60vw', minHeight: '80vh', fontSize: '1.2rem'}}>
                <CardBody>
                    <CardTitle tag="h4" className="mb-4">
                        <div style={{display: 'flex', flexDirection: 'row', justifyContent: 'space-between'}} >
                            <div>
                                <span>{eventInfo.name}</span>
                                <CardSubtitle className="text-muted" tag="h5" style={{marginTop: '0'}} >
                                    Sport: {eventInfo.sport}
                                </CardSubtitle>
                            </div>
                            {eventInfo.organizer.identifier === localData.identifier ?
                                <Button
                                    color="secondary"
                                    onClick={() => {window.location.href=`/modify-event/${eventInfo.event_id}`}}
                                >
                                    Modify Event
                                </Button>
                                :
                                null
                            }
                        </div>
                    </CardTitle>

                    <Card>
                        <CardBody style={{}}>
                            <div>
                                <b>Description:</b> {eventInfo.description}
                            </div>
                            <div>
                                Creator: <Link to="/profile/">{eventInfo.organizer.identifier}</Link>
                            </div>
                        </CardBody>
                    </Card>

                    <CardSubtitle className="mt-2 mb-2 text-muted">
                        <div style={{margin: '0 1rem'}}>
                            <span>
                                Starting on {(new Date(eventInfo.startDate).toString()).split(' GMT')[0]}
                            </span>
                            <span style={{float: 'right', color: 'blue'}}>
                                {eventInfo.duration} minutes event
                            </span>
                        </div>
                    </CardSubtitle>

                    <Card style={{marginTop: '2rem'}} >
                        <CardBody>
                            <CardTitle tag="h4">
                                Skill Requirements (0 - 5)
                            </CardTitle>

                            <label for="minSkill" style={{float: 'right'}} >Minimum Skill Level</label>
                            <input 
                                id="minSkill"
                                type="range" 
                                min="0" max="5" 
                                step="1" 
                                value={`${eventInfo.minSkillLevel}`} 
                                style={{width: '100%', color: 'red'}}
                            />
                            
                            <label for="maxSkill" style={{float: 'right'}} >Maximum Skill Level</label>
                            <input 
                                id="maxSkill"
                                type="range" 
                                min="0" max="5" 
                                step="1" 
                                value={`${eventInfo.maxSkillLevel}`} 
                                style={{width: '100%'}}
                            />
                            {}
                            <label for="userSkill" style={{float: 'right'}} >Your Skill Level</label>
                            <input 
                                id="userSkill"
                                type="range" 
                                min="0" max="5" 
                                step="1" 
                                value={`${userSkill}`} 
                                style={{width: '100%'}}
                            />
                        </CardBody>
                    </Card>

                    <Card style={{marginTop: '2rem'}} >
                        <CardBody>
                            <CardTitle tag="h4">
                                Participation Requirements ({minimumAttendeeCapacity || 0} - {eventInfo.maximumAttendeeCapacity})
                            </CardTitle>
                            
                            {minimumAttendeeCapacity && (
                            <>
                                <label for="minSkill" style={{float: 'right'}} >Minimum Attendee</label>
                                <input 
                                    id="minSkill"
                                    type="range" 
                                    min="0" max={`${eventInfo.maximumAttendeeCapacity}`} 
                                    step="1" 
                                    value={`${minimumAttendeeCapacity}`} 
                                    style={{width: '100%', color: 'red'}}
                                />
                            </>
                            )}
                            
                            <label for="maxSkill" style={{float: 'right'}} >Maximum Attendee</label>
                            <input 
                                id="maxSkill"
                                type="range" 
                                min="0" max={`${eventInfo.maximumAttendeeCapacity}`} 
                                step="1" 
                                value={`${eventInfo.maximumAttendeeCapacity}`} 
                                style={{width: '100%'}}
                            />
                            {}
                            <label for="userSkill" style={{float: 'right'}} >Current Attendee</label>
                            <input 
                                id="userSkill"
                                type="range" 
                                min="0" max={`${eventInfo.maximumAttendeeCapacity}`} 
                                step="1" 
                                value={`${eventInfo.attendee.length}`} 
                                style={{width: '100%'}}
                            />
                        </CardBody>
                    </Card>

                    <Card style={{marginTop: '2rem'}} >
                        <CardBody>
                            <Map height={300} defaultCenter={[latitude, longitude]} defaultZoom={17}>
                                <Marker width={50} anchor={[latitude, longitude]}>
                                    <img src="https://static3.depositphotos.com/1000868/261/v/950/depositphotos_2614173-stock-illustration-beach-ball.jpg" width={40} height={37} alt="Pigeon!" />
                                </Marker>
                            </Map>
                        </CardBody>
                    </Card>
                </CardBody>
            </Card>
            )
        }
        </>
    )
}

export {EventInformation}
