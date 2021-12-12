import React from "react"

import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import { Link } from 'react-router-dom';

import { CountryDropdown, RegionDropdown, CountryRegionData } from 'react-country-region-selector';

import './SearchPage.css';
import { width } from "@mui/system";
import { Map, Draggable } from "pigeon-maps";
import { MenuItem } from "@mui/material";
import { Select } from "@mui/material";
import axios from 'axios';

import EventInfo from "./EventInfo";

const baseURL = "/events/searches";

class SearchPage extends React.Component {

    
    constructor() {
        super()
        this.state = {
            identifier: "",
            sporttype: "",
            minSkillLevel: -1,
            maxSkillLevel: -1,
            startingDate: "",
            endingDate: "",
            anchor: [41.084, 29.051],
            anchor2: [41.085, 29.052],
            startTime: "",
            endTime: "",
            country: '', 
            useMap: false,
            region: '' ,
            events: []
        }

        this.handleChange = this.handleChange.bind(this);
        this.handleMapChange = this.handleMapChange.bind(this);
        this.handleMapChange2 = this.handleMapChange2.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.selectCountry = this.selectCountry.bind(this);
        this.selectRegion = this.selectRegion.bind(this);
    }


    selectCountry (val) {
        this.setState({ country: val });
      }
    
      selectRegion (val) {
        //console.log(this.state)
        this.setState({ region: val });
      }


    handleSubmit(event) {
        event.preventDefault();



        let info = {}

        if(this.state.identifier !== "") {
            info.nameContains = this.state.identifier
        }

        if(this.state.sporttype !== "") {
            info.sport = this.state.sporttype
        }

        if(parseInt(this.state.maxSkillLevel) !== -1 && parseInt(this.state.minSkillLevel) !== -1 ) {
            if( this.state.maxSkillLevel < this.state.minSkillLevel) {
                alert('Max skill level cannot be less than min skill level')
                return
            } else {
                info.skillLevel = []
                let minVal = parseInt(this.state.minSkillLevel);
                while(minVal < parseInt(this.state.maxSkillLevel) + 1) {
                    info.skillLevel.push(minVal);
                    minVal += 1;
                }

            }
            
        } else if (parseInt(this.state.maxSkillLevel) !== -1) {
            info.skillLevel = []
            let minVal = 1;
                while(minVal < parseInt(this.state.maxSkillLevel) + 1) {
                    info.skillLevel.push(minVal);
                    minVal += 1;
                }
        } else if (parseInt(this.state.minSkillLevel) !== -1) {
            info.skillLevel = []
            let minVal = parseInt(this.state.minSkillLevel);
            while(minVal < 6) {
                info.skillLevel.push(minVal);
                minVal += 1;
            }
        }



        



        if(this.state.startingDate !== "" && this.state.endingDate!=="") {
            if(this.state.endingDate < this.state.startingDate) {
                
                alert('Starting date cannot be later than the ending date')
                return
            } else {
                info.dateBetweenStart = this.state.startingDate;
                info.dateBetweenEnd = this.state.endingDate;
            }
        } else if (this.state.startingDate !== "") {
            alert('Date must be given as a 2 sided interval')
            return
        } else if (this.state.endingDate !== "") {
            alert('Date must be given as a 2 sided interval')
            return
        }


        if(this.state.startTime !== "" && this.state.endTime !== "") {
            if(this.state.startTime > this.state.endTime) {
                
                alert('Start time cannot be later than the end time')
                return
            } else {
                info.timeBetweenStart = this.state.startTime
                info.timeBetweenEnd = this.state.endTime
            }
        } else if (this.state.startTime !== "") {
            alert('Time must be given as a 2 sided interval')
            return
        } else if (this.state.endTime !== "") {
            alert('Time must be given as a 2 sided interval')
            return
        }

        

        if(this.state.useMap ===true) {
            if(this.state.anchor[0] < this.state.anchor2[0] && this.state.anchor[1] < this.state.anchor2[1]) {
                info.latitudeBetweenStart = (Math.round(this.state.anchor[0] * 100) / 100).toFixed(4)
                info.latitudeBetweenEnd = (Math.round(this.state.anchor2[0] * 100) / 100).toFixed(4)
                info.longitudeBetweenStart = (Math.round(this.state.anchor[1] * 100) / 100).toFixed(4)
                info.longitudeBetweenEnd = (Math.round(this.state.anchor2[1] * 100) / 100).toFixed(4)
            } else {
                alert('The positions of the markers used to draw rectangle are problematic. Check the description again please')
                return
            }
        } else {
            const { country, region } = this.state;
            if(country !== "" && region !=="") {
                info.country = country
                info.city = region
            } else if (country !== "") {
                info.country = country;
            }
        }
        



        const user = JSON.parse(localStorage.getItem('user')).token;

        axios
            .post(baseURL, info,  {headers:{'Authorization': `Token ${user}`}}).then((response) => {
                
                if(response.status === 200 || response.status === 201) {
                    //console.log(response)
                    console.log(response.data.items)
                    this.setState({ events: response.data.items });
                    /*this.props.history.push({
                        pathname: '/search-results-page',
                        state: { events: response.data.items }
                    })*/
                    //this.context.events = response.data.items
                    alert('Search is successful')

                    //window.location.href = '/search-results-page'
                } else {
                    alert(response.message)
                    //alert('Not valid info for an event')
                }
            }
            ).catch((error) => {
                alert('There is an error. Try again later')
            })
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

    handleMapChange2(value) {
        console.log(value)
        console.log(this.state)
        this.setState({
            anchor2: value
          });
    }




    render() {


        const resultingEvents = this.state.events.map(event => <EventInfo name={event.name} description={event.description} id={event.event_id} /> )
        let title = "";
        if(resultingEvents.length < 1) {
            title = "No event found"
        } else {
            title = "Search Results"
        }
        const { country, region } = this.state;
            
        const paperStyle={padding :30,width:480, margin:"20px auto"}
        const btnstyle={margin:'8px 0'}

        return (
            
            <div>

                
                <h1 id="title">Search Event Page <br /></h1>

                <form onSubmit={this.handleSubmit}>
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

                            <br /><br />
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
                                <MenuItem value={'volleyball'}>Volleyball</MenuItem>
                                <MenuItem value={'watersports'}>Watersports</MenuItem>
                                <MenuItem value={'weightlifting'}>Weightlifting</MenuItem>
                                
                            </Select>

                            

                            <TextField style= {{width:420}} className="lowerInput" style= {{width:420}}
                                label='Minimum Skill Level' 
                                placeholder='Enter minimum skill level required (1-5)' 
                                InputProps={{ inputProps: { min: 1, max: 5 } }}
                                type="number" 
                                name="minSkillLevel" 
                                id="minSkillLevel"   
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ minSkillLevel: value });
                                  }}                                              
                            />


                            <TextField style= {{width:420}} className="lowerInput" style= {{width:420}}
                                label='Maximum Skill Level' 
                                placeholder='Enter maximum skill possible (1-5)' 
                                InputProps={{ inputProps: { min: 1, max: 5 } }}
                                type="number" 
                                name="maxSkillLevel" 
                                id="maxSkillLevel"   
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ maxSkillLevel: value });
                                  }}                                              
                            />


                            <p><br/>Date interval</p>
                            <p>Earliest:</p>

                            <TextField style= {{width:420}}  className="lowerInput"
                                
                                placeholder='Enter starting date' 
                                
                                type="date" 
                                name="date" 
                                id="startingDate"     
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ startingDate: value });
                                  }}                                               
                            />


                            <p><br />Latest:</p>



                            <TextField style= {{width:420}}  className="lowerInput"
                                placeholder='Enter ending date' 
                                
                                type="date" 
                                name="date" 
                                id="endingDate"     
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ endingDate: value });
                                  }}                                               
                            />

                            <p> <br/>Time interval</p>
                            <p>Earliest:</p>
                            <TextField style= {{width:420}}  className="lowerInput"
                                
                                
                                placeholder='Enter starting time info' 
                                
                                type="time" 
                                name="startTime" 
                                id="startTime"        
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ startTime: value });
                                  }}                                         
                            />

                            <p><br />Latest:</p>

                            <TextField style= {{width:420}}  className="lowerInput"
                                
                                
                                placeholder='Enter ending time info' 
                                
                                type="time" 
                                name="endTime" 
                                id="endTime"        
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ endTime: value });
                                  }}                                         
                            />


                            <p><br />You can use either map or country and city search for the location. Select which one to use please.</p>


                            <Select style={{width: 420}}
                                labelId="Use Map For Search"
                                id="useMap"
                                
                                label="Use Map For Search"
                                onChange={event => { 
                                    const { value } = event.target;
                                    this.setState({ useMap: value });
                                  }}      
                            >
                                <MenuItem value={true}>Map</MenuItem>
                                <MenuItem value={false}>Country and City</MenuItem>
                               
                                
                            </Select>



                            <br /><br />
                            <p>Draw the rectangle by putting the red marker to the top right corner of the area in which you are interested in and green marker to the bottom left corner. </p>
                            

                            {/* From https://static3.depositphotos.com/1000868/261/v/950/depositphotos_2614173-stock-illustration-beach-ball.jpg */}
                            <div> 
                                <Map height={300} defaultCenter={[41.084, 29.051]} defaultZoom={16}>
                                    <Draggable offset={[60, 87]} anchor={this.state.anchor} onDragEnd={this.handleMapChange}>
                                        <img src="https://cdn.pixabay.com/photo/2014/04/03/10/03/google-309741_1280.png" width={28} height={37} alt="Pigeon!" />
                                        {/*console.log(this.state.anchor)*/}
                                    </Draggable>
                                    <Draggable offset={[60, 87]} anchor={this.state.anchor2} onDragEnd={this.handleMapChange2}>
                                        <img src="data:image/png;base64,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 " width={40} height={37} alt="Pigeon!" />
                                        {/*console.log(this.state.anchor)*/}
                                    </Draggable>
                                    
                                </Map>
                            </div>
                            
                            {/*<TextField className="lowerInput" style= {{width:420}}
                                label='Maximum Distance (in terms of meters)' 
                                placeholder='Enter maximum distance (in terms of meters)' 
 
                                type="number" 
                                name="maxDistance" 
                                id="maxDistance"   
                                onChange={event => {
                                    const { value } = event.target;
                                    this.setState({ maxDistance: value });
                                  }}                                              
                                />*/}



                            <br />

                            <CountryDropdown style = {{width: 420}}
                            value={country}
                            onChange={this.selectCountry} />

                            <br /><br />

                            <RegionDropdown  style = {{width: 420}}
                            country={country}
                            value={region}
                            onChange={this.selectRegion} />

                            <br />
                            
                            <Button type='submit' color='primary' variant="contained" style={btnstyle} fullWidth>Search For Corresponding Events</Button>
                            <Typography >
                                <Link to="/" >
                                    Return To Home Page
                                </Link>
                            </Typography>
                                
                        
                        </Paper>
                    </Grid>
                
                </form>
                
                <h1 id="title2">{title} <br /></h1>
               
                {resultingEvents}
                <br /><br />
            </div>                

        
        )
    }

}

export default SearchPage