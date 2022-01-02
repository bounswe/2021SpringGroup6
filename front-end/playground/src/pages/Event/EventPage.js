import {React, useState, Fragment, useEffect} from 'react';
import { useParams } from 'react-router-dom'
import './EventPage.css';

import {EventDiscussionPage} from './Discussion/EventDiscussionPage';
import {EventInformation} from './EventInformation/EventInformation';
import {EventParticipationInfoPage} from './EventParticipationInfoPage/EventParticipationInfoPage';

import {getEvent} from '../../services/Events';



import {
  TabContent, 
  TabPane, 
  Nav, 
  NavItem, 
  NavLink, 

} from 'reactstrap';

function EventPage(props) {
  const [tabName, setTabName] = useState('Event');
  const changeTab = (name) => {
      setTabName(name)
  }
  const [isLoading, setIsLoading] = useState(true);

  const {id: event_id} = useParams();


  const [eventInfo, setEventInfo] = useState(
      // dummy data
      {
        event_id: event_id,
      }
  );


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
                    <TabPane tabId="Discussion">
                        <EventDiscussionPage eventInfo={eventInfo} isLoading={isLoading}/>
                    </TabPane>

                </>
                :
                <div>Loading</div>
            }
        </TabContent>


    </div>
  );
}

export default EventPage;