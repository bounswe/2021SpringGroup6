import {React, Fragment, useState, useEffect, useContext} from 'react';
import { Card } from 'react-bootstrap'
import './Profile.css';
import {UserContext} from '../../UserContext';
import axios from 'axios';
import SportNames from '../../PermanentComponents/SportNames.js';
import { Button, Input, Label, Collapse,  UncontrolledCollapse } from 'reactstrap';

function Profile() {
    const {user, setUser} = useContext(UserContext);
    const [profileInfo, setProfileInfo] = useState({
        email: '',
        identifier: '',
        name: '',
        familyName: '',
        birthDate : '',
        gender : '',
        sports: []
    });
    useEffect(() => {
        // set user attributes
        //console.log('\nuser\n', user)
        axios.get(`/users/${user.id}`)
        .then(function (response) {
            if(response.status === 200){
                setUser(prevState => ({
                    ...prevState,
                    ...response.data
                }));
                // prepare profile info object, not ready yet
                const {user_id, knowsAbout,/* @context, @id, @type,*/ ...profile} = response;
                profile.sports = SportNames.map((sport, index) => ({sport: index, skill_level: response.knowsAbout[index]}))
                delete profile["@context"];
                delete profile["@id"];
                delete profile["@type"];

                setProfileInfo(prev => ({...prev, profile}))
                //localStorage.setItem("user",{});
                console.log('\nresponse\n', response)
            } else{
                console.log("Some error ocurred");
            }
        })
        .catch(function (error) {
            console.log(error);
        });
    }, [])

    function validateEmail(email) {
        const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }

    function handleChange(info) {
        setProfileInfo((prev) => ({...prev, [info.field]: info.value}))
    }

    function handleSportsChange(info) {
        console.log('\nsport\n', info.field, info.value, typeof info.value);
    }

    function formSubmit() {
        axios.put(`/users/${user.id}`, profileInfo)
        .then(function (response) {
            if(response.status === 200){
                alert('Saved Successfully!')
            } else{
                alert("Please try again.");
            }
        })
        .catch(function (error) {
            alert("There is an error. Please try again.");
            console.log(error);
        });
    }

    return (
    <div style={{minWidth: '45%', padding: '4rem 0'}}>
        <div className="profile-title">
            <span>Profile Settings</span>
            <Button 
                disabled={!validateEmail(profileInfo.email)}
                onClick={() => {formSubmit()}}
            >
                Save Changes
            </Button>
        </div>
        <Card style={{minWidth: '30%', padding: '2rem 3rem'}}>
            <div style={{}}>
                <Label for="userName">
                    User Name
                </Label>
                <Input
                    id="userName"
                    name="UserName"
                    placeholder="Your User Name"
                    value={profileInfo.identifier}
                    onChange={(event) => {
                        handleChange({field: 'identifier', value: event.target.value})
                    }}
                    type="text"
                    
                />
            </div>

            <div className="lowerInput" style={{}}>
                <Label for="Email">
                    Email
                </Label>
                <Input
                    valid={validateEmail(profileInfo.email)}
                    invalid={!validateEmail(profileInfo.email)}
                    id="Email"
                    name="Email"
                    placeholder="Your Email"
                    value={profileInfo.email}
                    onChange={(event) => {
                        handleChange({field: 'email', value: event.target.value})
                    }}
                    type="email"
                    
                />
            </div>

            <div className="lowerInput" style={{}}>
                <Label for="Name">
                    Name
                </Label>
                <Input
                    id="Name"
                    name="Name"
                    placeholder="Your Name"
                    value={profileInfo.name}
                    onChange={(event) => {
                        handleChange({field: 'name', value: event.target.value})
                    }}
                    type=""
                    
                />
            </div>

            <div className="lowerInput" style={{}}>
                <Label for="Surname">
                    Surname
                </Label>
                <Input
                    id="Surname"
                    name="Surname"
                    placeholder="Your Surname"
                    value={profileInfo.familyName}
                    onChange={(event) => {
                        handleChange({field: 'familyName', value: event.target.value})
                    }}
                    type=""
                    
                />
            </div>

            <div className="lowerInput" style={{}}>
                <Label for="BirthDate">
                    BirthDate
                </Label>
                <Input
                    id="BirthDate"
                    name="BirthDate"
                    placeholder="Your Birth Date"
                    value={profileInfo.birthDate}
                    onChange={(event) => {
                        handleChange({field: 'birthDate', value: event.target.value})
                    }}
                    type="date"
                    
                />
            </div>

            <div className="lowerInput" style={{}}>
                <Label for="Gender">
                    Gender
                </Label>
                <Input
                    id="Gender"
                    name="Gender"
                    placeholder=""
                    value={profileInfo.gender}
                    onChange={(event) => {
                        handleChange({field: 'gender', value: event.target.value})
                    }}
                    type="select"
                >
                    <option>
                        Other
                    </option>
                    <option>
                        Male
                    </option>
                    <option>
                        Female
                    </option>
                </Input>
            </div>
        </Card>

        <Card style={{minWidth: '30%', padding: '20px', marginTop: '20px'}}>
            <Button
                color="primary"
                //onClick={function noRefCheck(){}}
                id="toggler"
                style={{
                marginBottom: '1rem'
                }}
            >
                Sports
            </Button>
            <UncontrolledCollapse toggler="#toggler">
                {SportNames.map((sport, index) => (
                    <div key={sport} className="lowerInput" style={{}}>
                        <Label for={sport}>
                            {sport}
                        </Label>
                        <Input
                            id={sport}
                            name={sport}
                            //value={profileInfo.sports[index]}
                            onChange={(event) => {
                                handleSportsChange({field: 'sport', value: event.target.value})
                            }}
                            type="select"
                        >   
                            <option>
                                {0}
                            </option>
                            <option>
                                {1}
                            </option>
                            <option>
                                {2}
                            </option>
                            <option>
                                {3}
                            </option>
                            <option>
                                {4}
                            </option>
                            <option>
                                {5}
                            </option>
                        </Input>
                    </div>
                ))}
            </UncontrolledCollapse>
        </Card>
    </div>
    )
}

export default Profile;
