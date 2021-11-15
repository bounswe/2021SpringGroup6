import React, { useState } from 'react';
import LoginComponent from "./LoginComponents";
import Button from 'react-bootstrap/Button';
import axios from 'axios';

function Login() {
  const adminUser = {
    email : "admin@admin.com",
    password : "admin"
  }


  const [user, setUser] = useState({email:""});
  const [error, setError] = useState("");

  const Login = details => {
    console.log(details);

    if (details.email === adminUser.email && details.password === adminUser.password){ // need to connect with DB
      console.log("Logged in")
      setUser({ 
        email : details.email
      });
    }else {
      console.log("Can't logged in");
      setError("Please Sign Up")
    }
  }

  const Logout = () => { // need to connect with DB
      console.log("Logout")
      setUser({ 
        email : ""
      });
  }

  return (
    <div className="Login">
      {(user.email !== "") ? (
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