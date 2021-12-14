import {React, useState, Fragment, useEffect} from 'react';

import { Link, useLocation, Routes, Route } from "react-router-dom";

import {getEvent} from '../../services/Events';
import './StreamCards.css';

import Timeline from '@mui/lab/Timeline';
import TimelineItem from '@mui/lab/TimelineItem';
import TimelineSeparator from '@mui/lab/TimelineSeparator';
import TimelineConnector from '@mui/lab/TimelineConnector';
import TimelineContent from '@mui/lab/TimelineContent';
import TimelineOppositeContent from '@mui/lab/TimelineOppositeContent';
import TimelineDot from '@mui/lab/TimelineDot'

import gif from '../../images/squadgamegif_circle.gif'

function StreamCards(props) {
    const {summary, actor, target, object} = props
    const event_id = target ? target['@id'] : object['@id']
    const [eventInfo, setEventInfo] = useState(undefined);

    useEffect(() => {
        if (! eventInfo){
            getEvent(event_id)
            .then(response => {
                setEventInfo(response)
            })
            .catch(error => {
                // do nothing
            })
        }
    }, [])

    return (
        <TimelineItem>
            <TimelineOppositeContent
                align="right"
                variant="body2"
                color="text.secondary"
                className="activity-timeline-opposite"
                >
                {eventInfo ? 
                    <>
                    <div>
                        {(new Date(eventInfo.startDate).toString()).split(' GMT')[0]}
                    </div>
                    <div>
                        {eventInfo.location.address}
                    </div>
                    </>
                    : 
                    'Soon'
                }
            </TimelineOppositeContent>
            <TimelineSeparator>
                <TimelineDot 
                    className="activity-timeline-dot"
                >
                    <img src={gif} width="35" alt="logo" />
                </TimelineDot>
                <TimelineConnector />
            </TimelineSeparator>
            <TimelineContent                      
                className="activity-hover-shadow"          
                style={{marginTop: '0', marginBottom: '1.8rem'}}
            >
                <Link 
                    className="link-clear"
                    to={`/event/${target ? 
                        target['@id'] : object['@id']}`}
                >
                    <div 
                        style={{
                            fontSize: '1.2rem',
                            fontWeight: 'bold'
                        }}
                    >
                        <Link 
                            to={`/profile/${actor['@id']}`}
                            className="link-clear link-hover-black"
                            style={{zIndex: '10'}}
                        >
                            {actor.identifier}
                        </Link>
                    </div>
                    <div>
                        {summary}
                    </div>
                </Link>
            </TimelineContent>
        </TimelineItem>
    )
}

export default StreamCards;