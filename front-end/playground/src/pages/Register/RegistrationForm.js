import React, {useState} from 'react';
import axios from 'axios';
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';

function RegistrationForm(props) {
    const [state , setState] = useState({
        email : "",
        password : "",
        identifier:"",
        name:"",
        surname:"",
        location:"",
        age:0,
        gender:""
    })
    
    const sendDetailsToServer = () => {
        if(state.email.length && state.password.length) {
            
            const payload={
                "email":state.email,
                "password":state.password,
                "identifier":state.identifier,
                "name":state.name,
                "surname":state.surname,
                "location":state.location,
                "age":state.age,
                "gender":state.gender
            }

            axios.post('http://13.59.0.178:8080/users', payload)
                .then(function (response) {
                    if(response.status === 200){
                        setState(prevState => ({
                            ...prevState,
                            'successMessage' : 'Registration successful. Redirecting to home page..'
                        }))
                        //localStorage.setItem(ACCESS_TOKEN_NAME,response.data.token);
                        //redirectToHome();
                        console.log("aa")
                    } else{
                        console.log("Some error ocurred");
                    }
                })
                .catch(function (error) {
                    console.log(error);
                });    
        } else {
            console.log('Please enter valid username and password')    
        }
        
    }

    const handleSubmitClick = (e) => {
        e.preventDefault();
        if(state.password === state.confirmPassword) {
            sendDetailsToServer()    
        } else {
            console.log('Passwords do not match');
        }
    }
    const handleChange = (e) => {

        const {id , value} = e.target   
        setState(prevState => ({
            ...prevState,
            [id] : value
        }))
        //console.log(this.state.password)
    }
    const paperStyle={padding :20,height:'70vh',width:380, margin:"20px auto"}
    const btnstyle={margin:'8px 0'}
  return(
        <Grid>
            <Paper elevation={10} style={paperStyle}>


                            <TextField label='E-mail' placeholder='Enter e-mail' fullWidth required type ="email" name="email" id="email" 
                                onChange={handleChange}
                            />

                            <TextField label='Password' placeholder='Enter password' fullWidth required type ="password" name="password" id="password"
                                onChange={handleChange}
                            />

                            <TextField label='Confirm Password' placeholder='Enter password' fullWidth required type ="password" name="confirmPassword" id="confirmPassword"
                                onChange={handleChange}
                            />
                            <TextField label='Identifier' placeholder='Enter identifier' fullWidth required type ="identifier" name="identifier" id="identifier"
                                onChange={handleChange}
                            />
                            <TextField label='Name' placeholder='Enter Name' fullWidth  type ="name" name="name" id="name"
                                onChange={handleChange}
                            />
                            <TextField label='Surname' placeholder='Enter surname' fullWidth  type ="surname" name="surname" id="surname"
                                onChange={handleChange}
                            />
                            <TextField label='Location' placeholder='Enter location' fullWidth  type ="location" name="location" id="location"
                                onChange={handleChange}
                            />
                            <TextField label='Age' placeholder='Enter age' fullWidth  type ="age" name="age" id="age"
                                onChange={handleChange}
                            />
                            <TextField label='Gender' placeholder='Enter gender' fullWidth  type ="gender" name="gender" id="gender"
                                onChange={handleChange}
                            />

                        <Button 
                            type='submit' color='primary' variant="contained" style={btnstyle} fullWidth onClick={handleSubmitClick}>
                            Register
                        </Button>
                        <Typography >
                            <Link href="#" >
                                Forgot password ?
                            </Link>
                        </Typography>
                        <Typography >
                            <Link href="/Login" >
                                Already have an account ?
                            </Link>
                        </Typography>
            </Paper>

        </Grid>
    )
}
export default RegistrationForm;