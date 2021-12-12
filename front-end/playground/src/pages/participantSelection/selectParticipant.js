import React, { useState, useContext } from 'react';
import selectParticipantComponent from "./selectParticipantComponents";
import Button from 'react-bootstrap/Button';
import axios from 'axios';
import {UserContext} from '../../UserContext';
import { Link, Navigate } from 'react-router-dom'

function selectParticipant() {
 
  const [error, setError] = useState("");
  const {user, setUser} = useContext(UserContext);

  const eventID = 1234
  const selectParticipant = details => {

    axios.post('/events/' + eventID + '/participants'  , {selectedParticant:details.selectedParticant})
    .then(function (response) {
        if(response.status === 200){
            axios.get(`/users/${response.data.user_id}`)
            .then(function (profile_response) {
                console.log('success');
            });
        }
        else{
            console.log("Some error ocurred");
        }
    })
    .catch(function (error) {
        console.log(error);
    });
  }


  return (
    <div className="selectParticipant">
      {user.token ? <Navigate replace to="/" /> : <selectParticipantComponent selectParticipant={selectParticipant} error = {error} />}
    </div>
  )

}


export default selectParticipant;