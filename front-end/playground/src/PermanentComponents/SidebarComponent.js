import {React, Fragment, useContext, useState} from 'react';
import Nav from 'react-bootstrap/Nav';
import { Link } from 'react-router-dom';
import {Transition} from 'react-transition-group';
import './SidebarComponent.css';
import {UserContext} from '../UserContext'
import {MdArrowForwardIos, MdArrowBackIos} from 'react-icons/md'


function SidebarComponent(props) {
    const {user, setUser} = useContext(UserContext);
    const [toggle, setToggle] = useState(true);
    const sidebarWidth = '170px', transitionDuration = '300ms';
    const linkStyle = {
        transition: `width ${transitionDuration} linear`,
        width: '0'
    }
    const transitionStyles = {
        entering: { width: '0' },
        exiting:  { width: sidebarWidth },
        entered:  { width: sidebarWidth },
        exited:   { width: '0' },
    };
    const linkToggleStyle = {
        transition: `left ${transitionDuration} linear`,
    }
    const transitionToggleStyles = {
        entering: {left: '0'},
        exiting: {left: sidebarWidth},
        entered: {left: sidebarWidth},
        exited: {left: '0'},
    }

    return(
        <Fragment>
            {/* From https://stackoverflow.com/questions/60482018/make-a-sidebar-from-react-bootstrap */}
            <Transition in={toggle} timeout={0}>
            {(state) => (
            <>
                <div className="sidebar" style={{...linkStyle, ...transitionStyles[state]}}>
                    <Nav id="sidebar"                        
                        className={`d-md-block`}
                        activeKey="/home"
                        onSelect={selectedKey => {
                            if (selectedKey === "logout") {
                                setUser({identifier: ""});
                                localStorage.setItem("user",JSON.stringify({identifier: ""}));
                            }
                        }}
                    >
                        <Nav.Item>
                            <Nav.Link href="profile" className="sidebar-link" >
                                {/* <Link to="profile" style={{color: 'inherit', textDecoration: 'inherit'}}>
                                    Profile <hr />
                                </Link> */}
                                Profile <hr />
                            </Nav.Link>
                        </Nav.Item>
                        <Nav.Item>
                            <Nav.Link href="event" className="sidebar-link" >Events <hr /></Nav.Link>
                        </Nav.Item>
                        <Nav.Item>
                            <Nav.Link eventKey="Badges" className="sidebar-link" >Badges <hr /></Nav.Link>
                        </Nav.Item>
                        <Nav.Item>
                            <Nav.Link eventKey="Equipments" className="sidebar-link" >Equipments <hr /></Nav.Link>
                        </Nav.Item>
                        <Nav.Item>
                            <Nav.Link eventKey="logout" className="sidebar-link" >Logout <hr /></Nav.Link>
                        </Nav.Item>
                    </Nav>
                </div>
                <div className={`sidebar-toggle`} style={{...linkToggleStyle, ...transitionToggleStyles[state]}}>
                    <div 
                        className={`sidebar-toggle-icon-wrapper sidebar-toggle-icon-${toggle ? 'left' : 'right'}`}
                        onClick={() => {setToggle((prev) => (!prev))}}    
                    >
                        {/* <MdArrowBackIos className="sidebar-toggle-icon" onClick={() => {setToggle((prev) => (!prev))}} /> */}
                        { toggle ? 
                            <MdArrowBackIos className="sidebar-toggle-icon" /> 
                            : 
                            <MdArrowForwardIos className="sidebar-toggle-icon" />}
                    </div>
                </div>
            </>
            )}
            </Transition>
        </Fragment>
    )
}

export default SidebarComponent