import React from "react"
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Container from 'react-bootstrap/Container';
import './Header.css';
import { Link } from "react-router-dom";

import gif from '../images/squadgamegif_circle_black.gif'

function Header() {
    return (
       <div className = 'page'>
           {/* From https://react-bootstrap.github.io/components/navbar/ */}
           <Navbar className="header header-container" expand="lg">
                <Container style={{}}>
                    <Link to="/"
                        style={{color: '#ed1b76', textDecoration: 'unset', fontSize: '20px', marginRight: '10px'}}
                    >
                        <img src={gif} width="30" alt="logo" style={{marginRight: '0.3rem'}} />
                        Squad Game
                    </Link>
                    <Navbar.Toggle className="navbar-collapse-custom" aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav" style={{color: 'white'}}>
                        <Nav className="me-auto">
                            <Link to="/" className="header-link">
                                {/* <Link to="/home"
                                    style={{color: 'white', textDecoration: 'unset'}}
                                >
                                    Home
                                </Link> */}
                                Home
                            </Link>
                            <NavDropdown title="Events" id="basic-nav-dropdown">
                            <NavDropdown.Item href="/new-event">New Event</NavDropdown.Item>
                            <NavDropdown.Divider />
                            <NavDropdown.Item href="/search-page">Search Event</NavDropdown.Item>

                            </NavDropdown>
                            <NavDropdown title="Equipments" id="basic-nav-dropdown">
                            <NavDropdown.Item href="/new-equipment">New Equipment</NavDropdown.Item>
                            <NavDropdown.Divider />
                            <NavDropdown.Item href="/search-equipment-page">Search Equipment</NavDropdown.Item>
                            </NavDropdown>
                            <NavDropdown title="Badges" id="basic-nav-dropdown">
                            <NavDropdown.Item href="/badges">Available Badges</NavDropdown.Item>
                            </NavDropdown>

                            <Link to="notifications" className="header-link">
                                {/* <Link to="/home"
                                    style={{color: 'white', textDecoration: 'unset'}}
                                >
                                    Home
                                </Link> */}
                                Notifications
                            </Link>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
       </div>
    )
}

export default Header;
