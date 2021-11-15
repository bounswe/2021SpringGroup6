import React, { useState } from 'react'
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';



function LoginComponents({Login, error}) {

    const [details, setDetails] = useState({identifier:"", password :""});

    const submitHandler = e => {
        e.preventDefault();

        Login(details)
    }
    const paperStyle={padding :20,height:'40vh',width:380, margin:"20px auto"}
    const btnstyle={margin:'8px 0'}

    return (
        <form onSubmit={submitHandler}>
            <Grid>
                <Paper elevation={10} style={paperStyle}>

                    <Grid align='center'>
                        { (error !=="") ? ( <div className="error">{error}</div> ) : ""}
                    </Grid>
                    <TextField label='Identifier' placeholder='Enter identifier' fullWidth required type ="identifier" name="identifier" id="identifier" onChange={e => setDetails({...details, identifier: e.target.value})} value={details.identifier} />
                    <TextField label='Password' placeholder='Enter password' fullWidth required type ="password" name="password" id="password" onChange={e => setDetails({...details, password: e.target.value})} value={details.password} />
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
                        <Link href="#" >
                            Forgot password ?
                        </Link>
                    </Typography>
                    <Typography >
                        <Link href="/Register" >
                            Create New Account
                        </Link>
                    </Typography>
                        
                
                </Paper>
            </Grid>
           
        </form>
    )
}

export default LoginComponents;
