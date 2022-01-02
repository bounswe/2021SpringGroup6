import {React, useState, useEffect} from 'react';
import './EventParticipationInfoPage.css';
import {Button} from 'reactstrap';
import {Link} from 'react-router-dom';
import { Map, Marker } from "pigeon-maps";
import {postSpectatorDecleration, postParticipationRequest} from '../../../services/Events';

import {
  Card, 
  CardBody, 
  CardTitle,
  CardSubtitle, 
} from 'reactstrap';

function EventParticipationInfoPage(props) {
    const {eventInfo, isLoading} = props;
    const localData = JSON.parse(localStorage.getItem('user'));

    let buttonActive = (() => {
        if (eventInfo.organizer.identifier === localData.identifier)
            return false;
        for (let i = 0; i < eventInfo.audience.length; i++) {
            if (eventInfo.audience[i].identifier === localData.identifier) {
                return false;
            }
        }
        for (let i = 0; i < eventInfo.attendee.length; i++) {
            if (eventInfo.attendee[i].identifier === localData.identifier) {
                return false;
            }
        }
        return true;
    })();

    function spectate() {
        postSpectatorDecleration(eventInfo.event_id);
    }

    function participate() {
        postParticipationRequest(eventInfo.event_id);
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
                            {buttonActive ?
                                <div>
                                <Button
                                    color="secondary"
                                    onClick={spectate}
                                    style={{marginRight: '1rem'}}
                                >
                                    Spectate the Event
                                </Button>
                                <Button
                                    color="secondary"
                                    onClick={participate}
                                >
                                    Send Participation Request
                                </Button>
                                </div>
                                :
                                null
                            }
                        </div>
                    </CardTitle>

                    <Card>
                        <CardBody style={{}}>
                            <CardTitle tag="h4">
                                Participants
                            </CardTitle>
                            {eventInfo.attendee.length > 0 ? eventInfo.attendee.map((person, i) => {
                                return (
                                    <Button outline>{person.identifier}</Button>
                                )
                            })
                            :
                            <div>There is no participants yet.</div>
                            }
                        </CardBody>
                    </Card>

                    <Card style={{marginTop: '2rem'}}>
                        <CardBody style={{}}>
                            <CardTitle tag="h4">
                                Spectators
                            </CardTitle>
                            {eventInfo.audience.length > 0 ? eventInfo.audience.map((person, i) => {
                                return (
                                    <Button outline>
                                        <Link to={`/profile/${person['@id']}`} className="participation-link" >
                                            {person.identifier}
                                        </Link>
                                    </Button>
                                )
                            })
                            :
                            <div>There is no audience yet.</div>
                            }
                        </CardBody>
                    </Card>
                </CardBody>
            </Card>
            )
        }
        </>
    )
}

export {EventParticipationInfoPage}
