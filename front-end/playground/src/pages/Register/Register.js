import React, { useState } from 'react';
import RegisterComponent from "./RegisterComponents";
import axios from 'axios';

function Register() {
 
  const [user, setUser] = useState({email:"", password :"", identifier:""});
  const [error, setError] = useState("");

  const Register = details => {

    axios.post('/users', {email:details.email, password:details.password, identifier:details.identifier})
    .then(function (response) {
        if(response.status === 200){
            setUser(prevState => ({
                ...prevState,
                email:details.email,
                password:details.password,
                identifier:details.identifier,
                'successMessage' : 'Login successful. Redirecting to home page..'
            }))
            //localStorage.setItem("ACCESS_TOKEN_NAME",response.data.identifier);
            //redirectToHome();
            console.log("Registered in")
            console.log(response)

        } else{
            console.log("Some error occurred");
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
    <div className="Register">
      {(user.identifier !== "") ? (
        <div className="welcome">
          <h2>HomePage</h2>
        </div>
      ):(
        <RegisterComponent Register={Register} error = {error} />
      )}
    </div>
  )

}


export default Register;