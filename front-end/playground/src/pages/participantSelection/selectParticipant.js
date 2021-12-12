import React, { useState } from 'react';
import selectParticipantComponent from "./selectParticipantComponents";
import axios from 'axios';
import Navigate from 'react-router-dom'

function SelectParticipant(props) {
 
  const {user, setUser} = useState({value:"", selectedParticipant :[]});
  const [error] = useState("");
 


  const eventID = props.event_id
  const selectParticipant = details => {

    

    axios.post('/events/' + eventID + '/participants', {selectedParticant:details.selectedParticant})
    .then(function (response) {
          if(response.status === 200){
            setUser(prevState => ({
                ...prevState,
                selectedParticant:details.selectedParticant,
            }))

            console.log("Participant list posted")
            console.log(response)

        } else{
            console.log("Some error ocurred");
        }
    })
    .catch(function (error) {
        console.log(error);
    });  
  }


  return (
    <div className="selectParticipant">
      {user.token ? <Navigate replace to='/events'/> : <selectParticipantComponent selectParticipant={selectParticipant} error = {error} />}
    </div>
  )

}


export default SelectParticipant;