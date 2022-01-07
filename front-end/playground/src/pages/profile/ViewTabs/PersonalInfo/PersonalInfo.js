import {React, useState, useEffect, useContext} from 'react';
import axios from 'axios';
import {useParams} from 'react-router-dom'

import './PersonalInfo.css';
import {UserContext} from '../../../../UserContext';



import { Card } from 'react-bootstrap'
import SportNames from '../../../../PermanentComponents/SportNames.js';
import { Button, Input, Label,  UncontrolledCollapse } from 'reactstrap';

import {getOneUserInfo, blockUser} from '../../../../services/User';

function PersonalInfo(props) {
    const {user: randomuseridname, setUser} = useContext(UserContext);
    const user_id = parseInt(useParams().id);

    const {setBadgeVisibility, setCreatedEventVisibility} = props

    if(user_id == randomuseridname.user_id)
        window.location.href = '/profile'
    
    const [profileInfo, setProfileInfo] = useState({});

    useEffect(() => {
        if(profileInfo.identifier)
            return
        getOneUserInfo(user_id)
        .then(function (response) {
            if(response.status === 200){
                const {user_id, knowsAbout,/* @context, @id, @type,*/ ...profile} = response.data;
                profile.sports = response.data.knowsAbout.map((element) => ({
                    sport: element.name, 
                    skill_level: element.value})) || [];
                delete profile["@context"];
                delete profile["@id"];
                delete profile["@type"];
                setProfileInfo(profile);
                setBadgeVisibility(response.data.badge_visibility);
                setCreatedEventVisibility(response.data.created_events_visibility);
            } else{
                console.log("Some error ocurred");
                setProfileInfo({
                    email: '',
                    identifier: '',
                    name: '',
                    familyName: '',
                    birthDate : '',
                    gender : '',
                    sports: []
                })
            }
        })
        .catch(function (error) {
            console.log("Some error ocurred");
            console.log(error);
            setProfileInfo({
                    email: '',
                    identifier: '',
                    name: '',
                    familyName: '',
                    birthDate : '',
                    gender : '',
                    sports: []
            })
        });
    }, [])

    return (
    <>
    {profileInfo.identifier &&
    <div style={{minWidth: '45%', padding: '4rem 0', maxWidth: '600px', margin: 'auto'}}>
        <div className="profile-title">
            <span>Profile Information</span>
            <div>
                <Button 
                    onClick={() => {}}
                    style={{marginRight: '0.4rem'}}
                >
                    Follow
                </Button>
                <Button 
                    onClick={() => {blockUser(user_id)}}
                >
                    Block
                </Button>
            </div>
        </div>
        <Card style={{minWidth: '30%', padding: '2rem 3rem'}}>
            <div style={{}}>
                <Label for="userName">
                    User Name
                </Label>
                <Input
                    disabled={true}
                    id="userName"
                    name="UserName"
                    placeholder="Unknown"
                    value={profileInfo.identifier}
                    onChange={(event) => {
                        // handleChange({field: 'identifier', value: event.target.value})
                    }}
                    type="text"
                    
                />
            </div>

            {profileInfo.email_visibility && profileInfo.email && <div className="lowerInput" style={{}}>
                <Label for="Email">
                    Email
                </Label>
                <Input
                    disabled={true}
                    // valid={validateEmail(profileInfo.email)}
                    // invalid={!validateEmail(profileInfo.email)}
                    id="Email"
                    name="Email"
                    placeholder="Unknown"
                    value={profileInfo.email}
                    onChange={(event) => {
                        // handleChange({field: 'email', value: event.target.value})
                    }}
                    type="email"
                    
                />
            </div>}

            {profileInfo.name_visibility && profileInfo.name && <div className="lowerInput" style={{}}>
                <Label for="Name">
                    Name
                </Label>
                <Input                    
                    disabled={true}
                    id="Name"
                    name="Name"
                    placeholder="Unknown"
                    value={profileInfo.name}
                    onChange={(event) => {
                        // handleChange({field: 'name', value: event.target.value})
                    }}
                    type=""
                    
                />
            </div>}

            {profileInfo.familyName_visibility && profileInfo.familyName && <div className="lowerInput" style={{}}>
                <Label for="Surname">
                    Surname
                </Label>
                <Input
                    disabled={true}
                    id="Surname"
                    name="Surname"
                    placeholder="Unknown"
                    value={profileInfo.familyName}
                    onChange={(event) => {
                        // handleChange({field: 'familyName', value: event.target.value})
                    }}
                    type=""
                    
                />
            </div>}

            {profileInfo.birthDate_visibility && profileInfo.birthDate && <div className="lowerInput" style={{}}>
                <Label for="BirthDate">
                    Birth Date
                </Label>
                <Input
                    disabled={true}
                    id="BirthDate"
                    name="BirthDate"
                    placeholder="Your Birth Date"
                    value={profileInfo.birthDate}
                    onChange={(event) => {
                        // handleChange({field: 'birthDate', value: event.target.value})
                    }}
                    type="date"
                    
                />
            </div>}

            {profileInfo.gender_visibility && profileInfo.gender && <div className="lowerInput" style={{}}>
                <Label for="Gender">
                    Gender
                </Label>
                <Input
                    disabled={true}
                    id="Gender"
                    name="Gender"
                    placeholder="Unknown"
                    value={profileInfo.gender}
                    onChange={(event) => {
                        // handleChange({field: 'gender', 
                        //     value: event.target.value === 'other' ? 'decline_to_report' : event.target.value})
                    }}
                    type="select"
                >
                    <option>
                        other
                    </option>
                    <option>
                        male
                    </option>
                    <option>
                        female
                    </option>
                </Input>
            </div>}
        </Card>

        {profileInfo.skill_level_visibility && <Card style={{minWidth: '30%', padding: '20px', marginTop: '20px'}}>
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
                {SportNames.map((sport, index) => {
                    let level = profileInfo.sports.filter((usersport, index) => {return (usersport.sport === sport)});
                    level = level.length === 0 ? 0 : Number(level[0].skill_level);
                    return (<div key={sport} className="lowerInput" style={{}}>
                        <Label for={sport}>
                            {`${sport}`}
                        </Label>
                        <Input
                            disabled={true}
                            id={sport}
                            name={sport}
                            defaultValue={level}
                            onChange={(event) => {
                                // handleSportsChange({sport_name: sport, skill_level: Number(event.target.value)})
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
                    </div>)
                })}
            </UncontrolledCollapse>
        </Card>}
    </div>}
    </>
    )
}

export default PersonalInfo;
