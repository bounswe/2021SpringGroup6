import React from "react"

import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import { Link } from 'react-router-dom';

import './SearchPage.css';
import { width } from "@mui/system";
import { Map, Draggable } from "pigeon-maps";


class SearchPage extends React.Component {

    constructor() {
        super()
        this.state = {
            sporttype: "",
            minSkillLevel: -1,
            startingDate: "",
            endingDate: "",
            anchor: [41.084, 29.051],
            maxDistance: -1,
            startTime: "",
            endTime: "",
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

                
                <h1 id="title">Search Event Page <br /></h1>

                <form>
                    <Grid>
                        <Paper elevation={10} style={paperStyle}>

                            
                            
                            <TextField style= {{width:420}}
                                label='Event Name' 
                                placeholder='Enter event name' 

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

                            

                            <TextField className="lowerInput" style= {{width:420}}
                                label='Minimum Skill Level' 
                                placeholder='Enter minimum skill level required (0-5)' 
 
                                type="number" 
                                name="minSkillLevel" 
                                id="minSkillLevel"   
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ minSkillLevel: value });
                                  }}                                              
                            />


                            

                            <TextField  className="lowerInput"
                                
                                placeholder='Enter starting date' 
                                fullWidth required 
                                type="date" 
                                name="date" 
                                id="startingDate"     
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ startingDate: value });
                                  }}                                               
                            />


                            <TextField  className="lowerInput"
                                
                                
                                placeholder='Enter starting time info' 
                                fullWidth required 
                                type="time" 
                                name="startTime" 
                                id="startTime"        
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ startTime: value });
                                  }}                                         
                            />




                            <TextField  className="lowerInput"
                                placeholder='Enter ending date' 
                                fullWidth required 
                                type="date" 
                                name="date" 
                                id="endingDate"     
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ endingDate: value });
                                  }}                                               
                            />

                            <TextField  className="lowerInput"
                                
                                
                                placeholder='Enter ending time info' 
                                fullWidth required 
                                type="time" 
                                name="endTime" 
                                id="endTime"        
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ endTime: value });
                                  }}                                         
                            />


                            <br /><br />
                            <p>Select the center of the search and the maximum distance in terms of meters.</p>
                            

                            {/* From https://static3.depositphotos.com/1000868/261/v/950/depositphotos_2614173-stock-illustration-beach-ball.jpg */}
                            <div> 
                                <Map height={300} defaultCenter={[41.084, 29.051]} defaultZoom={17}>
                                    <Draggable offset={[60, 87]} anchor={this.state.anchor} onDragEnd={this.handleMapChange}>
                                        <img src="https://static3.depositphotos.com/1000868/261/v/950/depositphotos_2614173-stock-illustration-beach-ball.jpg" width={40} height={37} alt="Pigeon!" />
                                        {/*console.log(this.state.anchor)*/}
                                    </Draggable>
                                </Map>
                            </div>
                            
                            <TextField className="lowerInput" style= {{width:420}}
                                label='Maximum Distance (in terms of meters)' 
                                placeholder='Enter maximum distance (in terms of meters)' 
 
                                type="number" 
                                name="maxDistance" 
                                id="maxDistance"   
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ maxDistance: value });
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
                            <Button type='submit' color='primary' variant="contained" style={btnstyle} fullWidth>Search For Corresponding Events</Button>
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

export default SearchPage