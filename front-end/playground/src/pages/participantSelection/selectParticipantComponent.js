import React, { useState } from 'react'
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import { Link } from 'react-router-dom';
import ListItem from '@mui/material/ListItem';
import List from '@mui/material/List';
import Input from '@mui/material/Input';

import './selectParticipantComponent.css'



function selectParticipantComponent({selectParticipant, error}) {

    const [details, setDetails] = useState({value:"", selectedParticipant :[]});

    const submitHandler = async e => {
        e.preventDefault();

        await selectParticipant(details);

        console.log('\nlocal\n', JSON.parse(localStorage.getItem('user')));
    }
    const paperStyle={padding :30,width:480, margin:"20px auto"}

    return (
        <form onSubmit={submitHandler}>
            <Grid>
                <Paper elevation={10} style={paperStyle}>

                    <Grid align='center'>
                        { (error !=="") ? ( <div className="error">{error}</div> ) : ""}
                    </Grid>
                    <Input 
                        type='text' 
                        fullWidth required 
                        onChange={e => setDetails({...details, identifier: e.target.value})} 
                        value={details.value} 
                    />
                    <Button type='submit' color='primary'
                        onClick={e => setDetails({...details, identifier: e.target.selectedParticipant.concat(e.target.value)})} 
                        value={details.selectedParticipant}
                    >
                    Add Participant
                    </Button>
                    <Button type='submit' color='primary'
                        onClick={e => setDetails({...details, identifier: e.target.selectedParticipant.splice(0, e.target.selectedParticipant.length)})} 
                    >
                    Clear All Participant
                    </Button>            
                </Paper>
                <List>
                    {details.selectedParticipant.map((item, index) => (
                        <ListItem key={item}>{item}
                            <Button type='button' color='primary'
                                onClick={e => setDetails({...details, identifier: e.target.selectedParticipant.filter((item, j) => index !== j)})} 
                            >
                            X
                            </Button>
                        </ListItem>
                    ))}
                </List>
                <Button type='submit' color='primary'
                    onClick={e => setDetails({...details, identifier: e.target.selectedParticipant.filter((item, j) => index !== j)})} 
                >
                </Button>

            </Grid>
           
        </form>
    )
}

export default selectParticipantComponent;
