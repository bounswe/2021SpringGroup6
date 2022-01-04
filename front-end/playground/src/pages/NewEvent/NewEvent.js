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
            anchor: [41.084, 29.051],
            badge: ""
        }

        this.handleChange = this.handleChange.bind(this);
        this.handleMapChange = this.handleMapChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);

    }


    checkInput() {

        if(parseInt(this.state.max) < parseInt(this.state.min)) {
            alert('Maximum number of players cannot be less than minimum number of players')
            return false;
        }

        if(parseInt(this.state.maxSkillLevel) < parseInt(this.state.minSkillLevel)){
            alert('Maximum skill level cannot be less than minimum skill level')
            return false;
        }


        if(parseInt(this.state.min) < 1) {
            alert('Minimum number of players must be greater than 0')
            return false;
        }

        if(parseInt(this.state.max) < 1) {
            alert('Maximum number of players must be greater than 0')
            return false;
        }

        if(parseInt(this.state.maxSpectator) < 0) {
            alert('Maximum number of sprectators cannot be negative')
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
                latitude : (Math.round(this.state.anchor[0] * 100) / 100).toFixed(4),
                longitude : (Math.round(this.state.anchor[1] * 100) / 100).toFixed(4),
                minimumAttendeeCapacity: this.state.min,
                maximumAttendeeCapacity : this.state.max,
                maxSpectatorCapacity : this.state.maxSpectator,
                minSkillLevel : this.state.minSkillLevel,
                maxSkillLevel : this.state.maxSkillLevel,
                acceptWithoutApproval : this.state.acceptNecessary,
                duration: this.state.duration
            }       
            
            console.log(info)
            console.log(`Token ${user}`)
                      
            axios
            .post(baseURL, info,  {headers:{'Authorization': `Token ${user}`}}).then((response) => {
                console.log(response)
                console.log(response.data)
                console.log(response.data["@id"])
                console.log(`Token ${user}`)
                if(response.status === 200 || response.status === 201) {


                    let baseURL2 = baseURL + '/' + response.data["@id"] + '/badges';

                    let info2 = { badge : this.state.badge }

                    axios.post(baseURL2, info2, {headers:{'Authorization': `Token ${user}`}}).then((response) => {
                        if(response.status === 200 || response.status === 201) {

                        }
                    }).catch((error) => {
                        
                    })
                    

                    alert('The event is now opened.')
                    window.location.href = '/event/' + response.data["@id"]
                } else {
                    alert(response.message.name[0])
                    //alert('Not valid info for an event')
                }
            }
            ).catch((error) => {
                console.log(error)
                alert('Incorrect input. Try again')
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
        let badgeOptions = <Select style={{width: 420}}
                            labelId="badge"
                            id="badge"
                            
                            label="Select Badge"
                            onChange={event => { 
                                const { value } = event.target;
                                this.setState({ badge: value });
                            }}      
                        >
                            <MenuItem value={'leadership'}>Leadership</MenuItem>
                            <MenuItem value={'friendliness'}>Friendliness</MenuItem>
                            <MenuItem value={'greed'}>Greed</MenuItem>
                            <MenuItem value={'encouraging'}>Encouraging</MenuItem>
                            <MenuItem value={'clumsiness'}>Clumsiness</MenuItem>
                            <MenuItem value={'flamboyant'}>Flamboyant</MenuItem>
                            <MenuItem value={'competitive'}>Competitive</MenuItem>
                            <MenuItem value={'creativity'}>Creativity</MenuItem>
                            <MenuItem value={'nature lover'}>Nature Lover</MenuItem>
                            <MenuItem value={'kindness'}>Kindness</MenuItem>                                                              
                        </Select>;
        if (this.state.sporttype === 'soccer') {
            badgeOptions = <Select style={{width: 420}}
                            labelId="badge"
                            id="badge"
                            
                            label="Select Badge"
                            onChange={event => { 
                                const { value } = event.target;
                                this.setState({ badge: value });
                            }}      
                        >
                            <MenuItem value={'freekick master'}>Freekick Master</MenuItem>
                            <MenuItem value={'football supporter'}>Football Supporter</MenuItem>                                                             
                        </Select>
        }


        if (this.state.sporttype === 'basketball') {
            badgeOptions = <Select style={{width: 420}}
                            labelId="badge"
                            id="badge"
                            
                            label="Select Badge"
                            onChange={event => { 
                                const { value } = event.target;
                                this.setState({ badge: value });
                            }}      
                        >
                            <MenuItem value={'three pointer'}>Three Pointer</MenuItem>
                            <MenuItem value={'sixth man'}>Sixth Man</MenuItem>                                                                
                        </Select>
        }

        const paperStyle={padding :30,width:480, margin:"20px auto"}
        const btnstyle={margin:'8px 0'}

        return (
            
            <div>

                
                <h1 id="title"> <br />New Event Page</h1>

                <form onSubmit={this.handleSubmit}>
                    <Grid>
                        <Paper elevation={10} style={paperStyle} >

                            
                            
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
                                fullWidth required 
                                label="Sport Type"
                                onChange={event => { 
                                    const { value } = event.target;
                                    this.setState({ sporttype: value });
                                  }}      
                            >
                                <MenuItem value={'american_football'}>American_football</MenuItem>
                                <MenuItem value={'athletics'}>Athletics</MenuItem>
                                <MenuItem value={'australian_football'}>Australian_football</MenuItem>
                                <MenuItem value={'badminton'}>Badminton</MenuItem>
                                <MenuItem value={'baseball'}>Baseball</MenuItem>
                                <MenuItem value={'basketball'}>Basketball</MenuItem>
                                <MenuItem value={'climbing'}>Climbing</MenuItem>
                                <MenuItem value={'cricket'}>Cricket</MenuItem>
                                <MenuItem value={'cycling'}>Cycling</MenuItem>
                                <MenuItem value={'darts'}>Darts</MenuItem>
                                <MenuItem value={'esports'}>Esports</MenuItem>
                                <MenuItem value={'equestrian'}>Equestrian</MenuItem>
                                <MenuItem value={'extreme_sports'}>Extreme_sports</MenuItem>
                                <MenuItem value={'field_hockey'}>Field_hockey</MenuItem>
                                <MenuItem value={'fighting'}>Fighting</MenuItem>
                                <MenuItem value={'golf'}>Golf</MenuItem>
                                <MenuItem value={'gymnastics'}>Gymnastics</MenuItem>
                                <MenuItem value={'handball'}>Handball</MenuItem>
                                <MenuItem value={'ice_hockey'}>Ice_hockey</MenuItem>
                                <MenuItem value={'motorsport'}>Motorsport</MenuItem>
                                <MenuItem value={'multi-sports'}>Multi-sports</MenuItem>
                                <MenuItem value={'netball'}>Netball</MenuItem>                                                         
                                <MenuItem value={'rugby'}>Rugby</MenuItem>                                                    
                                <MenuItem value={'shooting'}>Shooting</MenuItem>
                                <MenuItem value={'snooker'}>Snooker</MenuItem> 
                                <MenuItem value={'soccer'}>Soccer</MenuItem>                                                                               
                                <MenuItem value={'table_tennis'}>Table_tennis</MenuItem>
                                <MenuItem value={'tennis'}>Tennis</MenuItem>
                                <MenuItem value={'ultimate_frisbee'}>Ultimate-Frisbee</MenuItem>
                                <MenuItem value={'volleyball'}>Volleyball</MenuItem>
                                <MenuItem value={'watersports'}>Watersports</MenuItem>
                                <MenuItem value={'weightlifting'}>Weightlifting</MenuItem>
                                                                
                            </Select>


                            <br/><br/>
                            <p>Select Badge: (Optional)</p>
                            
                            {badgeOptions}
                            

                            
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
                                placeholder='Enter minimum skill level required (1-5)' 
                                fullWidth required 
                                InputProps={{ inputProps: { min: 1, max: 5 } }}
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
                                placeholder='Enter maximum skill level required (1-5)' 
                                fullWidth required 
                                InputProps={{ inputProps: { min: 1, max: 5 } }}
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
                                fullWidth required 
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