import {React, useState, useEffect, useContext} from 'react';
import axios from 'axios';
import {useParams} from 'react-router-dom'

import './ProfileView.css';
import {UserContext} from '../../UserContext';



import { Card } from 'react-bootstrap'
import SportNames from '../../PermanentComponents/SportNames.js';
import { Button, Input, Label,  UncontrolledCollapse } from 'reactstrap';

import {getOneUserInfo} from '../../services/User';

function Profile() {
    const {user: randomuseridname, setUser} = useContext(UserContext);
    const user_id = parseInt(useParams().id);

    if(user_id == randomuseridname.user_id)
        window.location.href = '/profile'

    // const getUserInformation = () => {
    //     if(randomuseridname.profile) {
    //         return {...randomuseridname.profile}
    //     }
    //     getUserInfo(randomuseridname.user_id)
    //     .then(function (response) {
    //         if(response.status === 200){
    //             // setUser(prevState => ({
    //             //     ...prevState,
    //             //     ...response.data
    //             // }));
    //             // prepare profile info object, not ready yet
    //             const {user_id, knowsAbout,/* @context, @id, @type,*/ ...profile} = response.data;
    //             profile.sports = response.data.knowsAbout.map((element) => ({
    //                 sport: element.name, 
    //                 skill_level: element.value})) || [];
    //             delete profile["@context"];
    //             delete profile["@id"];
    //             delete profile["@type"];
    //             return {...profile}
    //         } else{
    //             console.log("Some error ocurred");
    //             return {
    //                 email: '',
    //                 identifier: '',
    //                 name: '',
    //                 familyName: '',
    //                 birthDate : '',
    //                 gender : '',
    //                 sports: []
    //             }
    //         }
    //     })
    //     .catch(function (error) {
    //         console.log("Some error ocurred");
    //         console.log(error);
    //         return {
    //             email: '',
    //             identifier: '',
    //             name: '',
    //             familyName: '',
    //             birthDate : '',
    //             gender : '',
    //             sports: []
    //         }
    //     });
    // }
    
    const [profileInfo, setProfileInfo] = useState({});

    useEffect(() => {
        if(profileInfo.identifier)
            return
        getOneUserInfo(user_id)
        .then(function (response) {
            console.log('response\n', response.status);
            if(response.status === 200){
                const {user_id, knowsAbout,/* @context, @id, @type,*/ ...profile} = response.data;
                profile.sports = response.data.knowsAbout.map((element) => ({
                    sport: element.name, 
                    skill_level: element.value})) || [];
                delete profile["@context"];
                delete profile["@id"];
                delete profile["@type"];
                setProfileInfo(profile);
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

    function validateEmail(email) {
        const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }

    function handleChange(info) {
        setProfileInfo((prev) => ({...prev, [info.field]: info.value}))
    }

    function handleSportsChange({sport_name, skill_level}) {
        if (skill_level === 0) return;
        let flag = false;
        const tempInfo = profileInfo.sports.map((sport) => {
            if (sport.sport === sport_name) {
                sport.skill_level = Number(skill_level);
                flag = true;
            }
            return sport
        });
        if (flag) {
            setProfileInfo((prev) => ({...prev, sports: tempInfo}))
        } else {
            setProfileInfo((prev) => ({...prev, sports: [...prev.sports, {sport: sport_name, skill_level: skill_level}]}))
        }
    }

    function formSubmit() {
        const toBeSent = {};
        for (let key in profileInfo) {
            if (profileInfo[key]){
                if (key !== 'sports' || (key === 'sports' && profileInfo[key].length > 0))
                    toBeSent[key] = profileInfo[key]
            }
        }
        axios.put(`/users/${randomuseridname.user_id}`, toBeSent, {headers:{'Authorization': `Token ${randomuseridname.token}`}})
        .then(function (response) {
            if(response.status === 200){
                alert('Saved Successfully!');
                setUser((prev) => ({...prev, profile: {...toBeSent, sports: toBeSent.sports || []}}));
                localStorage.setItem("user",
                    JSON.stringify({...JSON.parse(localStorage.getItem('user')), 
                        profile: {...toBeSent}}));
            } else{
                alert("Please try again.");
            }
        })
        .catch(function (error) {
            console.log('error\n', error);
            alert("There is an error. Please try again.");
        });
    }

    return (
    <>
    {profileInfo.identifier &&
    <div style={{minWidth: '45%', padding: '4rem 0'}}>
        <div className="profile-title">
            <span>Profile Settings</span>
            {/* <Button 
                disabled={!validateEmail(profileInfo.email)}
                onClick={() => {formSubmit()}}
            >
                Save Changes
            </Button> */}
            {/* <Button 
                onClick={() => {}}
            >
                Block
            </Button> */}
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

            <div className="lowerInput" style={{}}>
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
            </div>

            <div className="lowerInput" style={{}}>
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
            </div>

            <div className="lowerInput" style={{}}>
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
            </div>

            <div className="lowerInput" style={{}}>
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
            </div>

            <div className="lowerInput" style={{}}>
                <Label for="Gender">
                    {`Gender ${profileInfo.gender ? `: ${profileInfo.gender}` : ''}`}
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
        </Card>
    </div>}
    </>
    )
}

export default Profile;
