import React from "react"

import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';

import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

import {Link} from 'react-router-dom';

import {CountryDropdown, RegionDropdown, CountryRegionData} from 'react-country-region-selector';

import './EquipmentInformation.css';
import {width} from "@mui/system";
import {Map, Draggable, Marker} from "pigeon-maps";

import {MenuItem} from "@mui/material";
import {Select} from "@mui/material";
import axios from 'axios';

import {Card} from "react-bootstrap";


import {withRouter} from "react-router";
import {createEquipmentDiscussion, getEquipmentDiscussions} from "../../services/Equipments";


const baseURL = "/equipments/"


class EquipmentInformation extends React.Component {

    constructor() {
        super()
        this.state = {
            identifier: "",
            sporttype: "",
            anchor: [41.084, 29.051],
            anchor2: [41.085, 29.052],
            country: '',
            useMap: false,
            latitude: 0.1,
            longitude: 0.1,
            region: '',
            equipments: [],
            sharedContent: "",
            comment: '',
            comments: [],
        }

        this.handleChange = this.handleChange.bind(this);
        this.handleMapChange = this.handleMapChange.bind(this);
        this.handleMapChange2 = this.handleMapChange2.bind(this);

        this.selectCountry = this.selectCountry.bind(this);
        this.selectRegion = this.selectRegion.bind(this);

    }


    componentDidMount() {
        const user = JSON.parse(localStorage.getItem('user')).token;


        axios
            .get(baseURL + this.props.equipment_id, {headers: {'Authorization': `Token ${user}`}}).then((response) => {

                // console.log(response.data)
                // console.log(response.data["@id"])
                // console.log(`Token ${user}`)

                if (response.status === 200 || response.status === 201) {
                    this.setState({name: response.data.name});
                    this.setState({sporttype: response.data.sport.name});
                    this.setState({description: response.data.description});
                    if (response.data.additionalProperty[1]) {
                        this.setState({sharedContent: response.data.additionalProperty[1].value});
                    }

                    this.setState({latitude: response.data.geo.latitude});
                    this.setState({longitude: response.data.geo.longitude});

                } else {
                    alert(response.message.name[0])
                    //alert('Not valid info for an event')
                }
            }
        ).catch((error) => {
            console.log(error)
            alert('Incorrect input. Try again')
        })

        this.getDiscussions()
    }


    getDiscussions() {
        getEquipmentDiscussions(this.props.equipment_id).then((response) => {
            if (response.additionalProperty && response.additionalProperty.value) {
                this.setState({comments: response.additionalProperty.value})
            }
        })
    }

    createDiscussion = (e) => {
        e.preventDefault();
        createEquipmentDiscussion(this.props.equipment_id, this.state.comment).then((response) => {
            this.setState({comment: ''})
            this.getDiscussions();
        })

    }

    selectCountry(val) {
        this.setState({country: val});
    }

    selectRegion(val) {
        //console.log(this.state)
        this.setState({region: val});
    }

    handleChange(event) {
        this.setState({
            [event.target.id]: event.target.checked
        });
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


        //const resultingEquipments = this.state.equipments.map(event => <EquipmentInfo name={event.name} description={event.description} id={event.event_id} /> )
        let title = "";

        const {country, region} = this.state;

        const paperStyle = {padding: 30, width: 480, margin: "20px auto"}
        const btnstyle = {margin: '8px 0'}

        let photo;

        if (!this.state.sharedContent == "") {
            photo =
                <div>
                    <p style={{fontSize: 30}}>
                        <hr className='hrElements'/>
                        Image of the equipment:
                    </p>

                    <Card>
                        <Card.Body><img src={this.state.sharedContent}
                                        alt="Photo of the sport equipment"></img></Card.Body>
                    </Card>

                </div>
        }

        return (

            <div style={{marginLeft: 145, marginRight: 65}}>


                <h1 id="title">Equipment Information Page<br/></h1>

                <form onSubmit={this.handleSubmit}>
                    <Grid>


                        <p style={{fontSize: 30}}>
                            <hr className='hrElements'/>
                            Name:
                        </p>

                        <Card>
                            <Card.Body>{this.state.name}</Card.Body>
                        </Card>

                        <p style={{fontSize: 30}}>
                            <hr className='hrElements'/>
                            Sport Type:
                        </p>

                        <Card>
                            {/*From https://flexiple.com/javascript-capitalize-first-letter/ */}
                            <Card.Body>{this.state.sporttype.charAt(0).toUpperCase() + this.state.sporttype.slice(1)}</Card.Body>
                        </Card>


                        <p style={{fontSize: 30}}>
                            <hr className='hrElements'/>
                            Description:
                        </p>

                        <Card>
                            <Card.Body>{this.state.description}</Card.Body>
                        </Card>

                        <p style={{fontSize: 30}}>
                            <hr className='hrElements'/>
                            Location of the equipment:
                        </p>

                        <Map height={300} width={1450} defaultCenter={[41.084, 29.051]} defaultZoom={6}>
                            <Marker
                                width={50}
                                anchor={[this.state.latitude, this.state.longitude]}

                            />
                        </Map>


                        {photo}


                        <br/>

                        <Typography>
                            <Link to="/">
                                Return To Home Page
                            </Link>
                        </Typography>

                    </Grid>

                </form>

                <h1 id="title2">{title} <br/></h1>
                <br/><br/>

                <br/><br/>


                {
                    this.state.comments.map((comment, i) => <p key={comment['@id']}>{comment.text}</p>)
                }


                <form>
                    <label>Type your comment here:</label>
                    <textarea
                        className={'col-lg-12'}
                        value={this.state.comment}
                        onChange={(e) => this.setState({comment: e.target.value})}
                    />

                    <button onClick={this.createDiscussion} className={'btn btn-success col-lg-12'}>
                        STORE
                    </button>
                </form>
            </div>


        )
    }


}

export default EquipmentInformation;
