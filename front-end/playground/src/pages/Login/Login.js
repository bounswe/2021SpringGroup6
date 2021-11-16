import React, { useState, useContext } from 'react';
import LoginComponent from "./LoginComponents";
import Button from 'react-bootstrap/Button';
import axios from 'axios';
import {UserContext} from '../../UserContext';
import { Link, Navigate } from 'react-router-dom'

function Login() {
 
  const {user, setUser} = useContext(UserContext);
  const [error, setError] = useState("");

  const Login = details => {

    axios.post('/users/login', {identifier:details.identifier, password:details.password})
    .then(function (response) {
        if(response.status === 200){
            setUser(prevState => ({
                //...prevState,
                identifier:details.identifier,
                token: response.data.token,
                user_id: response.data.user_id,
            }))
            localStorage.setItem("user",{
              identifier:details.identifier, 
              token:response.data.token, 
              user_id: response.data.user_id
            });
            //redirectToHome();
            console.log("Logged in")
            console.log('\nresponse\n', response)
        } else{
            console.log("Some error ocurred");
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