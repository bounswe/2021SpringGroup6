import React from "react"

import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import { Link } from 'react-router-dom';

import { Wrapper, Status } from "@googlemaps/react-wrapper";
import MyMap from "../SelectPointFromMap/SelectPointFromMap.js"
import { Map, Draggable } from "pigeon-maps";

import './NewEvent.css';


class NewEvent extends React.Component {

    constructor() {
        super()
        this.state = {
            identifier: "",
            sporttype: "",
            min: -1,
            max: -1,
            maxSpectator: -1,
            minSkillLevel: -1,
            description: "",
            date: "",
            time: "",
            anchor: [41.084, 29.051]
        }

        this.handleChange = this.handleChange.bind(this);
        this.handleMapChange = this.handleMapChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);

    }


    handleSubmit() {
        
    }


    handleChange(event) {
        console.log(event)
        this.setState({
            [event.target.id]: event.target.checked
          });
        console.log(this.state)
    }

    handleMapChange(value) {
        console.log(value)
        console.log(this.state)
        this.setState({
            anchor: value
          });
    }


    render() {

        const paperStyle={padding :30,width:480, margin:"20px auto"}
        const btnstyle={margin:'8px 0'}

        return (
            
            <div>

                
                <h1 id="title"> <br />New Event Page</h1>

                <form>
                    <Grid>
                        <Paper elevation={10} style={paperStyle}>

                            
                            
                            <TextField 
                                label='Event Name' 
                                placeholder='Enter event name' 
                                fullWidth required 
                                type="identifier" 
                                name="identifier" 
                                id="identifier" 
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ identifier: value });
                                  }}      
                            />

                            <TextField  className="lowerInput"
                                label='Sport Type' 
                                placeholder='Enter type of the sport for the event' 
                                fullWidth required
                                type="text" 
                                name="sporttype" 
                                id="sporttype"   
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ sporttype: value });
                                  }}                                                  
                            />

                            <TextField className="lowerInput"
                                label='Minimum Number Of Players' 
                                placeholder='Enter minimum number of players' 
                                fullWidth required 
                                type="number" 
                                name="min" 
                                id="min" 
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ min: value });
                                  }}  
                                                        
                            />


                            <TextField className="lowerInput"
                                label='Maximum Number Of Players' 
                                placeholder='Enter maximum number of players' 
                                fullWidth required 
                                type="number" 
                                name="max" 
                                id="max"      
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ max: value });
                                  }}                                                 
                            />


                            <TextField className="lowerInput"
                                label='Maximum Number Of Spectators' 
                                placeholder='Enter maximum number of spectators' 
                                fullWidth required 
                                type="number" 
                                name="maxSpectator" 
                                id="maxSpectator" 
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ maxSpectator: value });
                                  }}                                                        
                            />

                            <TextField className="lowerInput"
                                label='Minimum Skill Level' 
                                placeholder='Enter minimum skill level required (0-5)' 
                                fullWidth required 
                                type="number" 
                                name="minSkillLevel" 
                                id="minSkillLevel"   
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ minSkillLevel: value });
                                  }}                                              
                            />


                            <TextField  className="lowerInput"
                                label='Description' 
                                placeholder='Enter description about the event' 
                                fullWidth required 
                                multiline
                                type="text" 
                                name="description" 
                                id="description"   
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ description: value });
                                  }}                                                      
                            />

                            <TextField  className="lowerInput"
                                
                                placeholder='Enter date' 
                                fullWidth required 
                                type="date" 
                                name="date" 
                                id="date"     
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ date: value });
                                  }}                                               
                            />


                            <TextField  className="lowerInput"
                                
                                
                                placeholder='Enter time info about the event' 
                                fullWidth required 
                                type="time" 
                                name="time" 
                                id="time"        
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ time: value });
                                  }}                                         
                            />


                            <FormControlLabel
                                control={
                                <Checkbox
                                    name="checkedB"
                                    color="primary"
                                />
                                }
                                label="Check me"
                            />

                                {/* From https://static3.depositphotos.com/1000868/261/v/950/depositphotos_2614173-stock-illustration-beach-ball.jpg */}
                            <div> 
                                <Map height={300} defaultCenter={[41.084, 29.051]} defaultZoom={17}>
                                    <Draggable offset={[60, 87]} anchor={this.state.anchor} onDragEnd={this.handleMapChange}>
                                        <img src="https://static3.depositphotos.com/1000868/261/v/950/depositphotos_2614173-stock-illustration-beach-ball.jpg" width={40} height={37} alt="Pigeon!" />
                                        {/*console.log(this.state.anchor)*/}
                                    </Draggable>
                                </Map>
                            </div>



                            <Button type='submit' color='primary' variant="contained" style={btnstyle} fullWidth>Start New Event</Button>
                            <Typography >
                                <Link to="/" >
                                    Return To Home Page
                                </Link>
                            </Typography>
                            
                                
                        
                        </Paper>
                    </Grid>
                
                </form>

            </div>                

        )
    }

}

export default NewEvent