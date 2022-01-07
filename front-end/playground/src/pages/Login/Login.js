import React, { useState, useContext } from 'react';
import LoginComponent from "./LoginComponents";
import Button from 'react-bootstrap/Button';
import axios from 'axios';
import {UserContext} from '../../UserContext';
import { Link, Navigate } from 'react-router-dom';

import {getFollowings, getFollowers, getBlockeds} from '../../services/User';

function Login() {
 
  const {user, setUser} = useContext(UserContext);
  const [error, setError] = useState("");

  const Login = details => {

    axios.post('/users/login', {identifier:details.identifier, password:details.password})
    .then(function (response) {
        if(response.status === 200){
            axios.get(`/users/${response.data.user_id}`)
            .then(function (profile_response) {
                if(profile_response.status === 200){
                    const {
                      user_id, 
                      knowsAbout, 
                      "@context": context, 
                      "@id": id, 
                      "@type": type, 
                      ...profile
                    } = profile_response.data;
                    profile.sports = knowsAbout.map((element) => ({
                        sport: element.name, 
                        skill_level: element.value})) || [];
                    setUser({
                      identifier: details.identifier,
                      token: response.data.token,
                      user_id: response.data.user_id,
                      context, id, type, 
                      profile: profile,
                    });
                    localStorage.setItem("user",JSON.stringify({
                      identifier:details.identifier, 
                      token:response.data.token, 
                      user_id: response.data.user_id,
                      context, id, type, 
                      profile: profile,
                    }));

                    getFollowings()
                    .then((response) => {
                        setUser(prev => {
                          return {
                            ...prev,
                            followings: response.items.map(item => {
                              return item.object['@id']
                            })
                          }
                        });
                    })
                    .catch((error) => {
                        
                    });

                    getBlockeds()
                    .then((response) => {
                        setUser(prev => {
                          return {
                            ...prev,
                            blockeds: response.items.map(item => {
                              return item.object['@id']
                            })
                          }
                        });
                    })
                    .catch((error) => {
                        
                    });

                    getFollowers()
                    .then((response) => {
                        setUser(prev => {
                          return {
                            ...prev,
                            followers: response.items.map(item => {
                              return item.actor['@id']
                            })
                          }
                        });
                    })
                    .catch((error) => {
                        
                    });

                }
            })
            .catch(function (error) {
                //console.log(error);
                setUser({
                identifier:details.identifier,
                token: response.data.token,
                user_id: response.data.user_id,
                });
                localStorage.setItem("user",JSON.stringify({
                  identifier:details.identifier, 
                  token:response.data.token, 
                  user_id: response.data.user_id
                }));
            });
        } else{
            console.log("Some error occurred");
        }
    })
    .catch(function (error) {
        console.log(error);
    });
  }

  const Logout = () => { // need to connect with DB
      console.log("Logout")
      setUser({ 
        identifier : ""
      });
  }

  return (
    <div className="Login">
      {user.token ? <Navigate replace to="/" /> : <LoginComponent Login={Login} error = {error} />}
    </div>
  )

}


export default Login;