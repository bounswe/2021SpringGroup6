import React from "react"

import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import { MenuItem } from "@mui/material";
import Typography from '@mui/material/Typography';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import { Link } from 'react-router-dom';
import { Select } from "@mui/material";

import {useContext} from 'react';

import {UserContext} from '../../UserContext';

import { Wrapper, Status } from "@googlemaps/react-wrapper";

import { Map, Draggable } from "pigeon-maps";
import axios from 'axios';


import Form from "react-bootstrap/Form"

//import Select from 'react-select'


import './NewEvent.css';

const baseURL = "/events";


class NewEvent extends React.Component {


    
    
    
    constructor() {
        super()
        this.state = {
            name: "",
            sporttype: "none",
            min: -1,
            max: -1,
            maxSpectator: -1,
            minSkillLevel: -1,
            maxSkillLevel: -1,
            description: "",
            date: "",
            time: "",
            duration: -1,
            acceptNecessary: false,
            anchor: [41.084, 29.051]
        }

        this.handleChange = this.handleChange.bind(this);
        this.handleMapChange = this.handleMapChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);

    }


    checkInput() {

        if(this.state.max < this.state.min) {
            alert('Maximum number of players cannot be less than minimum number of players')
            return false;
        }

        if(this.state.maxSkillLevel < this.state.minSkillLevel){
            alert('Maximum skill level cannot be less than minimum skill level')
            return false;
        }


        if(this.state.min < 1) {
            alert('Minimum number of players must be greater than 0')
            return false;
        }

        if(this.state.max < 1) {
            alert('Maximum number of players must be greater than 0')
            return false;
        }

        if(this.state.maxSpectator < 0) {
            alert('Maximum number of sprectators cannot be negative')
            return false;
        }

        if(this.state.minSkillLevel < 1 || this.state.minSkillLevel >5) {
            alert('Min skill level must be in the scope of 1-5')
            return false;
        }
        
        return true;

    }


    handleSubmit(event) {
        event.preventDefault();

        const {user, setUser} =this.context;


        let res = this.checkInput();
        if(res) {  

            const user = JSON.parse(localStorage.getItem('user')).token;
            let info =       {
                
                name : this.state.name,
                sport : this.state.sporttype,
                description : this.state.description,
                startDate : this.state.date + 'T' + this.state.time + '+03:00',
                latitude : this.state.anchor[0],
                longitude : this.state.anchor[1],
                minimumAttendeeCapacity: this.state.min,
                maximumAttendeeCapacity : this.state.max,
                maxSpectatorCapacity : this.state.maxSpectator,
                minSkillLevel : this.state.minSkillLevel,
                maxSkillLevel : this.state.maxSkillLevel,
                acceptWithoutApproval : this.state.acceptNecessary,
                duration: this.state.duration
            }       
            
            console.log(info)
                      
            axios
            .post(baseURL, info,  {headers:{'Authorization': `Token ${user}`}}).then((response) => {
                if(response.status === 200 || response.status === 201) {
                    alert('The event is now opened.')
                    window.location.href = '/'
                } else {
                    alert(response.message)
                    //alert('Not valid info for an event')
                }
            }
            ).catch((error) => {
                alert('There is an error. Try again later')
            })
            
        }
    }


    handleChange(event) {
        const user = JSON.parse(localStorage.getItem('user'));
        console.log(user)
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

                <form onSubmit={this.handleSubmit}>
                    <Grid>
                        <Paper elevation={10} style={paperStyle}>

                            
                            
                            <TextField 
                                label='Event Name' 
                                placeholder='Enter event name' 
                                fullWidth required 
                                type="identifier" 
                                name="name" 
                                id="name" 
                                onChange={event => {
                                    const user = JSON.parse(localStorage.getItem('user')).token;
                                    //console.log(user)
                                    const { value } = event.target;
                                    this.setState({ name: value });
                                  }}      
                            />

                            <br/><br/>
                            <p>Sport Type: </p>
                            
                            

                            <Select style={{width: 420}}
                                labelId="Sport Type"
                                id="sportType"
                                
                                label="Sport Type"
                                onChange={event => { 
                                    const { value } = event.target;
                                    this.setState({ sporttype: value });
                                  }}      
                            >
                                <MenuItem value={'soccer'}>Soccer</MenuItem>
                                <MenuItem value={'motorsport'}>motorsport</MenuItem>
                                <MenuItem value={'fighting'}>fighting</MenuItem>
                                <MenuItem value={'baseball'}>baseball</MenuItem>
                                <MenuItem value={'basketball'}>basketball</MenuItem>
                                <MenuItem value={'american_football'}>american_football</MenuItem>
                                <MenuItem value={'ice_hockey'}>ice_hockey</MenuItem>
                                <MenuItem value={'golf'}>golf</MenuItem>
                                <MenuItem value={'rugby'}>rugby</MenuItem>
                                <MenuItem value={'tennis'}>tennis</MenuItem>
                                <MenuItem value={'cricket'}>cricket</MenuItem>
                                <MenuItem value={'cycling'}>cycling</MenuItem>
                                <MenuItem value={'australian_football'}>australian_football</MenuItem>
                                <MenuItem value={'esports'}>esports</MenuItem>
                                <MenuItem value={'volleyball'}>volleyball</MenuItem>
                                <MenuItem value={'netball'}>netball</MenuItem>
                                <MenuItem value={'handball'}>handball</MenuItem>
                                <MenuItem value={'snooker'}>snooker</MenuItem> 
                                <MenuItem value={'field_hockey'}>field_hockey</MenuItem>
                                <MenuItem value={'darts'}>darts</MenuItem>
                                <MenuItem value={'athletics'}>athletics</MenuItem>
                                <MenuItem value={'badminton'}>badminton</MenuItem>
                                <MenuItem value={'climbing'}>climbing</MenuItem>
                                <MenuItem value={'equestrian'}>equestrian</MenuItem>
                                <MenuItem value={'gymnastics'}>gymnastics</MenuItem>
                                <MenuItem value={'shooting'}>shooting</MenuItem>
                                <MenuItem value={'extreme_sports'}>extreme_sports</MenuItem>
                                <MenuItem value={'table_tennis'}>table_tennis</MenuItem>
                                <MenuItem value={'multi-sports'}>multi-sports</MenuItem>
                                <MenuItem value={'watersports'}>watersports</MenuItem>
                                <MenuItem value={'weightlifting'}>weightlifting</MenuItem>
                                
                            </Select>

                            
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
                                InputProps={{ inputProps: { min: 0, max: 5 } }}
                                type="number" 
                                name="minSkillLevel" 
                                id="minSkillLevel"   
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ minSkillLevel: value });
                                  }}                                              
                            />

                            <TextField className="lowerInput"
                                label='Maximum Skill Level' 
                                placeholder='Enter maximum skill level required (0-5)' 
                                fullWidth required 
                                InputProps={{ inputProps: { min: 0, max: 5 } }}
                                type="number" 
                                name="maxSkillLevel" 
                                id="maxSkillLevel"   
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ maxSkillLevel: value });
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
                                    console.log(this.state.time)
                                  }}                                         
                            />


                            <TextField  className="lowerInput"                                                             
                                placeholder='Enter duration info about the event as minutes' 
                                fullWidth required 
                                type="number" 
                                name="duration" 
                                id="duration"        
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ duration: value });
                                  }}                                         
                            />

                            <br /><br />
                            <p>Accept Without Approval: </p>


                            <Select style={{width: 420}}
                                labelId="Accept Without Approval"
                                id="acceptNecessary"
                                
                                label="Accept Without Approval"
                                onChange={event => { 
                                    const { value } = event.target;
                                    this.setState({ acceptNecessary: value });
                                  }}      
                            >
                                <MenuItem value={'true'}>Yes</MenuItem>
                                <MenuItem value={'false'}>No</MenuItem>
                               
                                
                            </Select>


                            <p> <br/>Put the ball to the place where event will happen please!</p>
                            

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

NewEvent.contextType = UserContext


export default NewEvent