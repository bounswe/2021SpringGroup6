import {React, Fragment, useContext, useState, useEffect, useRef} from 'react';
import Nav from 'react-bootstrap/Nav';
import { Link } from 'react-router-dom';
import {Transition} from 'react-transition-group';
import './SidebarComponent.css';
import {UserContext} from '../UserContext'
import {MdArrowForwardIos, MdArrowBackIos} from 'react-icons/md'
import UseWindowSize from './WindowSizing'


function SidebarComponent(props) {
    const {user, setUser} = useContext(UserContext);
    const sidebarRef = useRef(null);
    const [window_width, window_height] = UseWindowSize();
    const [toggle, setToggle] = useState(window_width > 480);

    useEffect(() => {
        if (window_width < 480) {
            setToggle(false)
        } else if (window_width < 720) {

        } else {
            setToggle(true);
        }
    }, [window_width]);

    const sidebarWidth = (sidebarRef.current && sidebarRef.current.clientWidth) || '140px';
    const transitionDuration = 300;
    const linkStyle = {
        transition: `width ${transitionDuration}ms linear`,
        width: '0'
    }
    const transitionStyles = {
        entering: { width: '0' },
        entered:  { width: sidebarWidth },
        exiting:  { width: sidebarWidth },
        exited:   { width: '0' },
    };
    const linkToggleStyle = {
        transition: `left ${transitionDuration}ms linear`,
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
                    <Nav id="sidebar"                        
                        className={`d-md-block sidebar`}
                        activeKey="/home"
                        style={{...linkStyle, ...transitionStyles[state]}}
                        onSelect={selectedKey => {
                            if (selectedKey === "logout") {
                                setUser({identifier: ""});
                                localStorage.setItem("user",JSON.stringify({identifier: ""}));
                            }
                        }}
                    >
                        <Nav.Item>
                            <Link to="/profile" className="sidebar-link">
                                    Profile <hr />
                            </Link>
                        </Nav.Item>
                        <Nav.Item>
                            <Link to="/event" className="sidebar-link" >
                                Events <hr />
                            </Link>
                        </Nav.Item>
                        <Nav.Item>
                            <Link to="/" className="sidebar-link" >
                                Badges <hr />
                            </Link>
                        </Nav.Item>
                        <Nav.Item>
                            <Link to="/" className="sidebar-link" >
                                Equipments <hr />
                            </Link>
                        </Nav.Item>
                        <Nav.Item>
                            <Link to="" className="sidebar-link" onClick={() => {
                                setUser({identifier: ""});
                                localStorage.setItem("user",JSON.stringify({identifier: ""}));
                            }} >
                                Logout <hr />
                            </Link>
                        </Nav.Item>
                        <Nav.Item>
                            <Link to="/" className="sidebar-link redundant" >
                                Equipmentsssssss <hr />
                            </Link>
                        </Nav.Item>
                    </Nav>
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