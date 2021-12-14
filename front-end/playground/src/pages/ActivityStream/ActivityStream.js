import {React, useState, useEffect} from 'react';
import axios from 'axios';
import './ActivityStream.css';

import {Button, Spinner} from 'reactstrap'

import Timeline from '@mui/lab/Timeline';

import StreamCards from './StreamCards';


function ActivityStream(props) {
    // const localData = JSON.parse(localStorage.getItem('user'));
    const token = `Token ${props.token}`; // `Token ${localData.token}`;
    const [activityArray, setActivityArray] = useState([]);
    const defaultPerPage = 4;
    const [itemPerPage,setItemPerPage] = useState(defaultPerPage);
    const [pageCounter, setPageCounter] = useState(1);
    const [loading, setLoading] = useState(false);
    const [buttonDisabled, setButtonDisabled] = useState(false);

    useEffect(() => {
        axios({
            method: 'GET',
            url: `/activitystream?limit=${defaultPerPage}`,
            headers: {
                Authorization: token,
            },
            data: {
            }
        })
        .then(response => {
            if (response.status === 200) {
                setActivityArray(response.data.orderedItems)
                if (response.data.orderedItems.length == 0)
                    setButtonDisabled(true)
            } else {
                setActivityArray([])
            }
        })
        .catch(error => {
        console.log('error\n',error)
        setActivityArray([])
        })

        return setActivityArray([])
    }, [])

    function loadMore() {
        
        setLoading(true)
        axios({
            method: 'GET',
            url: `/activitystream?limit=${itemPerPage*(pageCounter+1)}`,
            headers: {
                Authorization: token,
            },
            data: {
            }
        })
        .then(response => {
            if (response.status === 200) {
                setActivityArray(response.data.orderedItems)
            } else {
                setActivityArray([])
            }
            setLoading(false)
        })
        .catch(error => {
            console.log('error\n',error)
            setActivityArray([])
            setLoading(false)
        })
        setPageCounter(prev => prev+1)
    }

    useEffect(() => {
        if(activityArray.length > 0 && activityArray.length === activityArray[0].id){
            setButtonDisabled(true)
        }
    }, [activityArray])

    return (
        <>
        {activityArray.length > 0 ? 
            <div className="activity-stream-continer">
                <Timeline className="activity-stream-timeline" position="alternate">
                {activityArray.map(activity => {
                    return (
                        <>
                        <StreamCards 
                            key={activity.id} 
                            summary={activity.summary} 
                            actor={activity.actor} 
                            target={activity.target}
                            object={activity.object} 
                        />
                        {/* <TimelineItem key={activity.id}>
                            <TimelineOppositeContent
                                align="right"
                                variant="body2"
                                color="text.secondary"
                                style={{marginTop: '0.45rem'}}
                                >
                                9:30 am
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
                                style={{marginTop: '0'}}
                            >
                                <Link 
                                    className="link-clear"
                                    to={`/event/${activity.target ? 
                                        activity.target['@id'] : activity.object['@id']}`}
                                >
                                    <div 
                                        style={{
                                            fontSize: '1.2rem',
                                            fontWeight: 'bold'
                                        }}
                                    >
                                        <Link 
                                            to={`/profile/${activity.actor['@id']}`}
                                            className="link-clear link-hover-black"
                                            style={{zIndex: '10'}}
                                        >
                                            {activity.actor.identifier}
                                        </Link>
                                    </div>
                                    <div>
                                        {activity.summary}
                                    </div>
                                </Link>
                            </TimelineContent>
                        </TimelineItem> */}
                        </>
                    )
                })} 
                </Timeline>
                <Button
                    disabled={buttonDisabled}
                    onClick={() => {loadMore()}}
                >
                    {loading ? 
                        <Spinner size="sm" /> 
                        :
                        buttonDisabled ? 
                            'No More Activity'
                            :
                            'Load More'
                    }
                </Button>
            </div>
            : 
            <div className="activity-stream-empty">
                <div style={{padding: '50px'}}>
                    There are no current activities yet
                </div>
            </div>
        }
        </>
    )
}

export default ActivityStream;
