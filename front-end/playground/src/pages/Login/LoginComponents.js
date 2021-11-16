import React, { useState } from 'react'
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import { Link } from 'react-router-dom';

import './LoginComponents.css'



function LoginComponents({Login, error}) {

    const [details, setDetails] = useState({identifier:"", password :""});

    const submitHandler = async e => {
        e.preventDefault();

        await Login(details);

        console.log('\nlocal\n', localStorage.getItem('user'));
    }
    const paperStyle={padding :30,width:480, margin:"20px auto"}
    const btnstyle={margin:'8px 0'}

    return (
        <form onSubmit={submitHandler}>
            <Grid>
                <Paper elevation={10} style={paperStyle}>

                    <Grid align='center'>
                        { (error !=="") ? ( <div className="error">{error}</div> ) : ""}
                    </Grid>
                    <TextField 
                        label='User Name' 
                        placeholder='Enter user name' 
                        fullWidth required 
                        type="identifier" 
                        name="identifier" 
                        id="identifier" 
                        onChange={e => setDetails({...details, identifier: e.target.value})} 
                        value={details.identifier} 
                    />
                    <TextField className="lowerInput"
                        label='Password' 
                        placeholder='Enter password' 
                        fullWidth required 
                        type="password" 
                        name="password" 
                        id="password" 
                        onChange={e => setDetails({...details, password: e.target.value})} 
                        value={details.password}
                    />
                    <FormControlLabel
                        control={
                        <Checkbox
                            name="checkedB"
                            color="primary"
                        />
                        }
                        label="Remember me"
                    />
                    <Button type='submit' color='primary' variant="contained" style={btnstyle} fullWidth>Log In</Button>
                    <Typography >
                        <Link to="/forgot-password" >
                            Forgot password ?
                        </Link>
                    </Typography>
                    <Typography >
                        <Link to="/register" >
                            Create New Account
                        </Link>
                    </Typography>
                        
                
                </Paper>
            </Grid>
           
        </form>
    )
}

export default LoginComponents;
