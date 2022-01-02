import {React, useState, Fragment, useEffect} from 'react';
import { useParams } from 'react-router-dom'
import './EventPage.css';

import {EventDiscussionPage} from './Discussion/EventDiscussionPage';
import {EventInformation} from './EventInformation/EventInformation';
import {EventParticipationInfoPage} from './EventParticipationInfoPage/EventParticipationInfoPage';

import {getEvent} from '../../services/Events';
import {getEventDiscussion} from '../../services/Events';



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
  CardBody, 
  CardTitle, 
  CardText,
} from 'reactstrap';

function EventPage(props) {
  const [tabName, setTabName] = useState('Event');
  const changeTab = (name) => {
      setTabName(name)
  }
  const [isLoading, setIsLoading] = useState(true);

  const {id: event_id} = useParams();
  const {id: event_discussion_id} = useParams();


  const [eventInfo, setEventInfo] = useState(
      // dummy data
      {
        event_id: event_id,
      }
  );
  const [eventDiscussionInfo, setDiscussionInfo] = useState(
    // dummy data
    {
      event_discussion_id: event_discussion_id,
    }
);

  useEffect(() => {
      if (!eventDiscussionInfo.created_on) {
        setIsLoading(true);
        getEventDiscussion(event_discussion_id)
        .then((response) => {
            setDiscussionInfo(response);
            setIsLoading(false);
        })
        .catch((error) => {
            alert('Event can not be loaded. You are redirecting to home page. Please try again later.');
            window.location.href = '/'
        });
      }
  }, []);

  useEffect(() => {
    if (!eventInfo.created_on) {
      setIsLoading(true);
      getEvent(event_id)
      .then((response) => {
          setEventInfo(response);
          setIsLoading(false);
      })
      .catch((error) => {
          alert('Event can not be loaded. You are redirecting to home page. Please try again later.');
          window.location.href = '/'
      });
    }
}, []);



  return (
      <div className="event-container">
        <Nav tabs justified className="event-nav">
            <NavItem>
                <NavLink
                active={tabName === 'Event'}
                onClick={() => {
                    changeTab('Event')
                }}
                >
               Event Information
                </NavLink>
            </NavItem>
            <NavItem>
                <NavLink
                active={tabName === 'Participation'}
                onClick={() => {
                    changeTab('Participation')
                }}
                >
                Participation
                </NavLink>
            </NavItem>
            <NavItem>
                <NavLink
                active={tabName === 'Discussion'}
                onClick={() => {
                    changeTab('Discussion')
                }}
                >
                Discussion
                </NavLink>
            </NavItem>
        </Nav>

        {/* pay attention to custom class. it makes the container a flexbox. if flexbox does not work for you, please contact with the author */}
        <TabContent activeTab={tabName} className={`custom-tab-content-${tabName}`}>
            {eventInfo.startDate ? 
                <>
                    <TabPane tabId='Event'>            
                        <EventInformation eventInfo={eventInfo} isLoading={isLoading} /> 
                    </TabPane>
                    <TabPane tabId="Participation">
                        <EventParticipationInfoPage eventInfo={eventInfo} isLoading={isLoading} />
                    </TabPane>

                </>
                :
                <div>Loading</div>
            }
        </TabContent>

        <TabContent activeTab={tabName} className={`custom-tab-content-${tabName}`}>
            {eventDiscussionInfo.startDate ? 
                <>

                    <TabPane tabId="Discussion">
                        <EventDiscussionPage eventDiscussionInfo={eventDiscussionInfo} isLoading={isLoading}/>
                    </TabPane>
                </>
                :
                <div> </div>
            }
        </TabContent>
    </div>
  );
}

export default EventPage;