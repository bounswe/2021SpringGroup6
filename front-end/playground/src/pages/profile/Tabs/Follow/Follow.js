import {React, useState, useEffect, useContext} from 'react';
import {Link} from 'react-router-dom'
// import { Card } from 'react-bootstrap'
import './Follow.css';
import {
  Tabs, 
  Tab, 
  TabContainer, 
  TabContent, 
  TabPane, 
  Nav, 
  NavItem, 
  NavLink,
  CardGroup,
  Card, 
  CardImg, 
  CardBody, 
  CardTitle, 
  CardText,
  ButtonGroup,
  Button,
  Badge
} from 'reactstrap';

import {getUserBadges, getFollowings, getFollowers, getBlockeds} from '../../../../services/User';

function Follow_Block() {
    const [followingUsers, setFollowingUsers] = useState([]);
    const [blockedUsers, setBlockedUsers] = useState([]);
    const [followers, setFollowers]= useState([]);
    
    
    useEffect(() => {
        if (!(followingUsers.length > 0)) {
            getFollowings()
            .then((response) => {
                setFollowingUsers(response.items);
            })
            .catch((error) => {
                alert('A problem occured. You are redirecting to home page. Please try again later.');
                window.location.href = '/'
            });
        }
        if (!(blockedUsers.length > 0)) {
            getBlockeds()
            .then((response) => {
                setBlockedUsers(response.items);
            })
            .catch((error) => {
                alert('A problem occured. You are redirecting to home page. Please try again later.');
                window.location.href = '/'
            });
        }
        if (!(followers.length > 0)) {
            getFollowers()
            .then((response) => {
                setFollowers(response.items);
            })
            .catch((error) => {
                alert('A problem occured. You are redirecting to home page. Please try again later.');
                window.location.href = '/'
            });
        }
    }, []);

    return (
    <div className="pp-badges-container">
        <Card style={{margin: '1rem'}} className="">
            <CardBody>
                <CardTitle tag="h5">
                    Users You Are Following
                </CardTitle>
                <div className="pp-badges-category-container">
                {followingUsers.length > 0 ? followingUsers.map(user => {
                    return (
                        <>
                            <Link to={`/profile/${user.object['@id']}`} >
                                <Badge className="badge-pill" pill color="primary">
                                    {user.object.identifier}
                                </Badge>
                            </Link>
                            {/* <CardComponent event={event}/> */}
                        </>
                    )
                }) : <div>You are not following any user.</div>
                }
                </div>
            </CardBody>
        </Card>
        <Card style={{margin: '1rem'}} className="">
            <CardBody>
                <CardTitle tag="h5">
                    Users You Blocked
                </CardTitle>
                <div className="pp-badges-category-container">
                {blockedUsers.length > 0 ? blockedUsers.map(user => {
                    return (
                        <>
                            <Link to={`/profile/${user.object['@id']}`} >
                                <Badge className="badge-pill" pill color="primary">
                                    {user.object.identifier}
                                </Badge>
                            </Link>
                            {/* <CardComponent event={event}/> */}
                        </>
                    )
                }) : <div>You didn't blocked any user.</div>
                }
                </div>
            </CardBody>
        </Card>
        <Card style={{margin: '1rem'}} className="">
            <CardBody>
                <CardTitle tag="h5">
                    Your Followers
                </CardTitle>
                <div className="pp-badges-category-container">
                {followers.length > 0 ? followers.map(user => {
                    return (
                        <>
                            <Link to={`/profile/${user.actor['@id']}`}>
                                <Badge className="badge-pill" pill color="primary">
                                    {user.actor.identifier}
                                </Badge>
                            </Link>
                            {/* <CardComponent event={event}/> */}
                        </>
                    )
                }) : <div>You have no followers.</div>
                }
                </div>
            </CardBody>
        </Card>
    </div>
    )
}

export default Follow_Block;
