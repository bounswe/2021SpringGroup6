import {React, useState, useEffect} from 'react';
import './EventParticipationInfoPage.css';
import {Button, Modal, ModalHeader, ModalBody, ModalFooter} from 'reactstrap';
import {Link} from 'react-router-dom';
import { Map, Marker } from "pigeon-maps";
import {
    postSpectatorDecleration, 
    postParticipationRequest, 
    getEventInteresteds,
    acceptInterested,
    rejectInterested
} from '../../../services/Events';

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

function EventParticipationInfoPage(props) {
    const {eventInfo, setEventInfo, isLoading} = props;
    const localData = JSON.parse(localStorage.getItem('user'));

    const [interesteds, setInteresteds] = useState([]);
    const [participationModal, setParticipationModal] = useState(false);
    const [participationModalInfo, setParticipationModalInfo] = useState({})
    
    const isCreator = eventInfo.organizer.identifier === localData.identifier;
    const acceptWithoutApproval = eventInfo.additionalProperty.filter(
        item => item.name === "acceptWithoutApproval")[0].value;

    useEffect(() => {
        if (!acceptWithoutApproval) {
            getEventInteresteds(eventInfo.event_id)
            .then((response) => {
                        setInteresteds(response.additionalProperty.value)
                    })
                    .catch((error) => {
                        alert('Event can not be loaded. You are redirecting to home page. Please try again later.');
                        window.location.href = '/'
                    });
        }
    }, [])

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
                                    <Button outline>
                                        <Link to={`/profile/${person['@id']}`} className="participation-link" >
                                            {person.identifier}
                                        </Link>
                                    </Button>
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

                    <Card style={{marginTop: '2rem'}}>
                        <CardBody style={{}}>
                            <CardTitle tag="h4">
                                Interesteds 
                                {isCreator && 
                                    <div style={{fontSize: '1.2rem', fontWeight: 'normal'}}>
                                        {' '}(You can respond interesteds. Click on their names)
                                    </div>}
                            </CardTitle>
                            {interesteds.length > 0 ? interesteds.map((person, i) => {
                                return (
                                    isCreator ? 
                                        <Button 
                                            outline
                                            onClick={() => {
                                                setParticipationModalInfo({...person})
                                                setParticipationModal(true);
                                                }}
                                        >
                                            {person.identifier}
                                        </Button>
                                        :
                                        <Button outline>
                                            <Link to={`/profile/${person['@id']}`} className="participation-link" >
                                                {person.identifier}
                                            </Link>
                                        </Button>
                                    
                                )
                            })
                            :
                            <div>
                                {acceptWithoutApproval ? 
                                    'This event accepts participants without approval.' 
                                    : 
                                    'There is no interest yet.'}
                            </div>
                            }
                        </CardBody>
                    </Card>
                </CardBody>
            </Card>
            )
        }
        <Modal
            toggle={() => {
                setParticipationModal(false);
            }}
            isOpen={participationModal}
            style={{marginTop: '20%'}}
        >
            <ModalHeader>
                Participation Request
            </ModalHeader>
            <ModalBody>
                <Link to={`/profile/${participationModalInfo['@id']}`} className="participation-request-link" >
                    {participationModalInfo.identifier}
                </Link>
                <span>
                    {' '}wants to join your event. What do you want?
                </span>
            </ModalBody>
            <ModalFooter>
                <Button 
                    color="primary"
                    onClick={() => {
                            acceptInterested(eventInfo.event_id, participationModalInfo['@id']);
                            setInteresteds(prev => prev.filter(item => item['@id'] !== participationModalInfo['@id']));
                            setEventInfo(prev => ({
                                ...prev,
                                attendee: [...prev.attendee, {...participationModalInfo}],
                                
                            }));
                            setParticipationModal(false);
                        }}
                >
                    Accept
                </Button>
                <Button 
                    color="danger"
                    onClick={() => {
                            rejectInterested(eventInfo.event_id, participationModalInfo['@id']);
                            setInteresteds(prev => prev.filter(item => item['@id'] !== participationModalInfo['@id']));
                            setParticipationModal(false);
                        }}
                >
                    Reject
                </Button>
            </ModalFooter>
        </Modal>
        </>
    )
}

export {EventParticipationInfoPage}
