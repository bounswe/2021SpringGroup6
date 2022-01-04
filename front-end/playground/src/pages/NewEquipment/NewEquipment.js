import React from "react"

import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import { MenuItem } from "@mui/material";
import Typography from '@mui/material/Typography';

import { Link } from 'react-router-dom';
import { Select } from "@mui/material";

import {UserContext} from '../../UserContext';

import { Map, Draggable } from "pigeon-maps";
import axios from 'axios';


import './NewEquipment.css';


const baseURL = "/equipments";



class NewEquipment extends React.Component {
    
    constructor() {
        super()
        
        this.state = {
            name: "",
            sporttype: "none",
            description: "",
            sharedContent: "",
            anchor: [41.084, 29.051]
        }

        
        this.handleMapChange = this.handleMapChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);

    }





    checkInput() {     
        
        // If some control needed, it can be added here.
        return true;

    }

    handleMapChange(value) {
        console.log(value)
        console.log(this.state)
        this.setState({
            anchor: value
          });
    }


    checkInput() {

        // Fill if needed
        
        return true;

    }



    handleSubmit(event) {
        event.preventDefault();

        const {user, setUser} =this.context;

        let res = this.checkInput();

        if(res) {  

            const user = JSON.parse(localStorage.getItem('user')).token;


            let info;

            if(this.state.sharedContent === "") {
                info =       {
                
                    name : this.state.name,
                    sport : this.state.sporttype,
                    description : this.state.description,
                    latitude : (Math.round(this.state.anchor[0] * 100) / 100).toFixed(4),
                    longitude : (Math.round(this.state.anchor[1] * 100) / 100).toFixed(4)
                }      
            } else {
                info =       {
                
                    name : this.state.name,
                    sport : this.state.sporttype,
                    description : this.state.description,
                    sharedContent : this.state.sharedContent,
                    latitude : (Math.round(this.state.anchor[0] * 100) / 100).toFixed(4),
                    longitude : (Math.round(this.state.anchor[1] * 100) / 100).toFixed(4)
                }      
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

                    alert('The equipment is now opened.')
                    window.location.href = '/equipment/' + response.data["@id"]
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



    render() {

        const paperStyle={padding :30,width:480, margin:"20px auto"}
        const btnstyle={margin:'8px 0'}

        return (
            
            <div>

                
                <h1 id="title"> <br />New Equipment Page</h1>

                <form onSubmit={this.handleSubmit}>
                    <Grid>
                        <Paper elevation={10} style={paperStyle} >

                            
                            
                            <TextField 
                                label='Equipment Name' 
                                placeholder='Enter equipment name' 
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

                            
                            

                            <TextField  className="lowerInput"
                                label='Description' 
                                placeholder='Enter description about the equipment' 
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



                            <TextField style= {{width:420}} className="lowerInput"
                                label='Shared Content (Optional)' 
                                placeholder='Enter URL of the photo of the equipment'  
                                multiline
                                type="text" 
                                name="sharedContent" 
                                id="sharedContent"   
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ sharedContent: value });
                                  }}                                                      
                            />

                        
                            <p> <br/>Put the ball to the location of the equipment please!</p>
                            

                                {/* From https://static3.depositphotos.com/1000868/261/v/950/depositphotos_2614173-stock-illustration-beach-ball.jpg */}
                            <div> 
                                <Map height={300} defaultCenter={[41.084, 29.051]} defaultZoom={17}>
                                    <Draggable offset={[60, 87]} anchor={this.state.anchor} onDragEnd={this.handleMapChange}>
                                        <img src="https://static3.depositphotos.com/1000868/261/v/950/depositphotos_2614173-stock-illustration-beach-ball.jpg" width={40} height={37} alt="Pigeon!" />
                                        {/*console.log(this.state.anchor)*/}
                                    </Draggable>
                                </Map>
                            </div>



                            <Button type='submit' color='primary' variant="contained" style={btnstyle} fullWidth>Open New Equipment</Button>
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


NewEquipment.contextType = UserContext



export default NewEquipment