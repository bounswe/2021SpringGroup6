import React, { useState } from 'react'
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

import './RegisterComponents.css'

import { Link } from 'react-router-dom'



function RegisterComponents({Register, error}) {

    const [details, setDetails] = useState({email:"", password :"", identifier:"", name:"", surname:"", birthdate:"", gender:"" });

    const submitHandler = e => {
        e.preventDefault();

        Register(details)
        
        window.location.href = '/login'
    }
    const paperStyle={padding :30, width:480, margin:"3rem auto"}
    const btnstyle={margin:'8px 0'}

    return (
        <form onSubmit={submitHandler}>
            <Grid>
                <Paper elevation={10} style={paperStyle}>

                    <Grid align='center'>
                        { (error !=="") ? ( <div className="error">{error}</div> ) : ""}
                    </Grid>
                    <TextField label='E-mail' placeholder='Enter e-mail' fullWidth required type ="email" name="email" id="email"  onChange={e => setDetails({...details, email: e.target.value})} value={details.email} />
                    <TextField className="lowerInput"  label='Password' placeholder='Enter password' fullWidth required type ="password" name="password" id="password" onChange={e => setDetails({...details, password: e.target.value})} value={details.password} />
                    <TextField className="lowerInput"  label='Identifier' placeholder='Enter User Name' fullWidth required type ="identifier" name="identifier" id="identifier" onChange={e => setDetails({...details, identifier: e.target.value})} value={details.identifier} />
                    <TextField className="lowerInput"  label='Name' placeholder='Enter name' fullWidth  type ="name" name="name" id="name" onChange={e => setDetails({...details, name: e.target.value})} value={details.name} />
                    <TextField className="lowerInput"  label='Surname' placeholder='Enter surname' fullWidth  type ="surname" name="surname" id="surname" onChange={e => setDetails({...details, surname: e.target.value})} value={details.surname} />
                    <TextField className="lowerInput"  label='Birth Date' placeholder='Enter birthdate' fullWidth  type ="birthdate" name="birthdate" id="birthdate" onChange={e => setDetails({...details, birthdate: e.target.value})} value={details.birthdate} />
                    <TextField className="lowerInput"  label='Gender' placeholder='Enter gender' fullWidth  type ="gender" name="gender" id="gender" onChange={e => setDetails({...details, gender: e.target.value})} value={details.gender} />

                    <Button type='submit' color='primary' variant="contained" style={btnstyle} fullWidth>Sign Up</Button>
                    <Typography >
                        <Link to="/forgot-password" >
                            Forgot password ?
                        </Link>
                    </Typography>
                    <Typography >
                        <Link to="/login" >
                            Already have an account ?
                        </Link>
                    </Typography>
                        
                
                </Paper>
            </Grid>
           
        </form>
    )
}

export default RegisterComponents;
