import React, { useState } from 'react';
import LoginComponent from "./LoginComponents";
import Button from 'react-bootstrap/Button';
import axios from 'axios';

function Login() {
 
  const [user, setUser] = useState({identifier:""});
  const [error, setError] = useState("");

  const Login = details => {

    axios.post('/users/login', {identifier:details.identifier, password:details.password})
    .then(function (response) {
        if(response.status === 200){
            setUser(prevState => ({
                ...prevState,
                identifier:details.identifier,
                'successMessage' : 'Registration successful. Redirecting to home page..'
            }))
            localStorage.setItem("ACCESS_TOKEN_NAME",response.data.identifier);
            //redirectToHome();
            console.log("Logged in")
            console.log(response)
            const token = localStorage.getItem("ACCESS_TOKEN_NAME")
            console.log(token)
        } else{
            console.log("Some error ocurred");
        }
    })
    .catch(function (error) {
        console.log(error);
    });  

    console.log(details);


  }

  const Logout = () => { // need to connect with DB
      console.log("Logout")
      setUser({ 
        identifier : ""
      });
  }

  return (
    <div className="Login">
      {(user.identifier !== "") ? (
        <div className="welcome">
          <h2>HomePage</h2>
          <Button onClick={Logout}>Logout</Button>
        </div>
      ):(
        <LoginComponent Login={Login} error = {error} />
      )}
    </div>
  )

}


export default Login;